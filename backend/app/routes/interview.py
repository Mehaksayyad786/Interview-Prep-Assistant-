from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId
from datetime import datetime, timezone
from typing import List

from app.database import interviews_collection, questions_answers_collection, results_collection, users_collection, questions_collection
from app.models import (
    InterviewStartRequest,
    InterviewResponse,
    QuestionResponse,
    AnswerSubmitRequest,
    EvaluationResponse,
    ResultsResponse,
    QuestionAnswerDetail
)
from app.auth import get_current_user
from app.ai import evaluate_answer, generate_results_summary
from app.questions_bank import get_predefined_question_base

router = APIRouter(prefix="/interview", tags=["Interview"])

@router.post("/start", response_model=InterviewResponse)
def start_interview(request: InterviewStartRequest, current_user: dict = Depends(get_current_user)):
    new_interview = {
        "user_id": current_user["_id"],
        "job_role": request.job_role,
        "interview_type": request.interview_type,
        "difficulty": request.difficulty,
        "status": "in_progress",
        "date": datetime.now(timezone.utc).isoformat()
    }
    
    result = interviews_collection.insert_one(new_interview)
    
    return InterviewResponse(
        id=str(result.inserted_id),
        user_id=str(current_user["_id"]),
        job_role=new_interview["job_role"],
        interview_type=new_interview["interview_type"],
        difficulty=new_interview["difficulty"],
        status=new_interview["status"],
        date=new_interview["date"]
    )

@router.get("/question/{interview_id}", response_model=QuestionResponse)
def get_next_question(interview_id: str, current_user: dict = Depends(get_current_user)):
    try:
        oid = ObjectId(interview_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid interview ID format")
        
    interview = interviews_collection.find_one({"_id": oid, "user_id": current_user["_id"]})
    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")
        
    if interview["status"] == "completed":
        return QuestionResponse(
            interview_id=interview_id,
            question_number=20,
            question="Interview is already completed.",
            is_completed=True
        )
        
    # Check existing questions
    existing_qas = list(questions_answers_collection.find({"interview_id": oid}).sort("question_number", 1))
    count = len(existing_qas)
    
    # If the last question is not answered yet, return it
    if count > 0 and existing_qas[-1].get("answer") is None:
        return QuestionResponse(
            interview_id=interview_id,
            question_number=existing_qas[-1]["question_number"],
            question=existing_qas[-1]["question"],
            type=existing_qas[-1].get("type", "descriptive"),
            options=existing_qas[-1].get("options", []),
            is_completed=False
        )
        
    # If we already have 20 answered questions, we are ready to complete
    if count >= 20:
        return QuestionResponse(
            interview_id=interview_id,
            question_number=20,
            question="All questions answered. Please complete the interview.",
            is_completed=True
        )
        
    # Generate new question
    previous_questions_texts = [qa["question"] for qa in existing_qas]
    next_question_num = count + 1
    
    # Retrieve predefined question from MongoDB database
    predefined_q = questions_collection.find_one({
        "job_role": interview["job_role"],
        "interview_type": interview["interview_type"],
        "difficulty": interview["difficulty"],
        "question_number": next_question_num
    })
    
    q_type = "descriptive"
    q_options = []
    if predefined_q:
        question_text = predefined_q["question"]
        q_type = predefined_q.get("type", "descriptive")
        q_options = predefined_q.get("options", [])
    else:
        # Fallback to local python bank if not found
        fallback_obj = get_predefined_question_base(
            job_role=interview["job_role"],
            interview_type=interview["interview_type"],
            difficulty=interview["difficulty"],
            question_number=next_question_num
        )
        question_text = fallback_obj["question"]
        q_type = fallback_obj.get("type", "descriptive")
        q_options = fallback_obj.get("options", [])
    
    # Save the new question
    new_qa = {
        "interview_id": oid,
        "question_number": next_question_num,
        "question": question_text,
        "type": q_type,
        "options": q_options,
        "answer": None,
        "technical_score": None,
        "communication_score": None,
        "relevance_score": None,
        "feedback": None,
        "weak_topic": None
    }
    
    questions_answers_collection.insert_one(new_qa)
    
    return QuestionResponse(
        interview_id=interview_id,
        question_number=next_question_num,
        question=question_text,
        type=q_type,
        options=q_options,
        is_completed=False
    )

@router.post("/answer/{interview_id}", response_model=EvaluationResponse)
def submit_answer(interview_id: str, request: AnswerSubmitRequest, current_user: dict = Depends(get_current_user)):
    try:
        oid = ObjectId(interview_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid interview ID format")
        
    interview = interviews_collection.find_one({"_id": oid, "user_id": current_user["_id"]})
    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")
        
    if interview["status"] == "completed":
        raise HTTPException(status_code=400, detail="Interview is already completed")
        
    # Find the specific question
    qa = questions_answers_collection.find_one({
        "interview_id": oid,
        "question_number": request.question_number
    })
    
    if not qa:
        raise HTTPException(status_code=404, detail="Question not found")
        
    if qa.get("answer") is not None:
        raise HTTPException(status_code=400, detail="Question already answered")
        
    # Call Gemini to evaluate the answer
    evaluation = evaluate_answer(
        question=qa["question"],
        answer=request.answer,
        job_role=interview["job_role"],
        interview_type=interview["interview_type"],
        difficulty=interview.get("difficulty", "Medium"),
        experience_level=current_user.get("experience_level", "Mid-Level"),
        skills=current_user.get("skills", [])
    )
    
    # Save the answer and evaluation
    questions_answers_collection.update_one(
        {"_id": qa["_id"]},
        {"$set": {
            "answer": request.answer,
            "technical_score": evaluation["technical_score"],
            "communication_score": evaluation["communication_score"],
            "relevance_score": evaluation["relevance_score"],
            "feedback": evaluation["feedback"],
            "weak_topic": evaluation.get("weak_topic")
        }}
    )
    
    return EvaluationResponse(
        technical_score=evaluation["technical_score"],
        communication_score=evaluation["communication_score"],
        relevance_score=evaluation["relevance_score"],
        feedback=evaluation["feedback"],
        weak_topic=evaluation.get("weak_topic")
    )

@router.post("/complete/{interview_id}", response_model=ResultsResponse)
def complete_interview(interview_id: str, current_user: dict = Depends(get_current_user)):
    try:
        oid = ObjectId(interview_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid interview ID format")
        
    interview = interviews_collection.find_one({"_id": oid, "user_id": current_user["_id"]})
    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")
        
    # Fetch all questions and answers
    qas = list(questions_answers_collection.find({"interview_id": oid}).sort("question_number", 1))
    
    if len(qas) < 20 or any(qa.get("answer") is None for qa in qas):
        raise HTTPException(
            status_code=400,
            detail="Cannot complete interview. Please answer all 20 questions first."
        )
        
    # Check if results are already generated
    existing_result = results_collection.find_one({"interview_id": oid})
    if existing_result:
        # If already completed, just return the existing results
        questions_list = [
            QuestionAnswerDetail(
                question_number=qa["question_number"],
                question=qa["question"],
                type=qa.get("type", "descriptive"),
                options=qa.get("options", []),
                answer=qa["answer"],
                technical_score=qa["technical_score"],
                communication_score=qa["communication_score"],
                relevance_score=qa["relevance_score"],
                feedback=qa["feedback"],
                weak_topic=qa.get("weak_topic")
            ) for qa in qas
        ]
        
        return ResultsResponse(
            interview_id=interview_id,
            overall_score=existing_result["overall_score"],
            technical_score=existing_result["technical_score"],
            communication_score=existing_result["communication_score"],
            relevance_score=existing_result["relevance_score"],
            weak_topics=existing_result["weak_topics"],
            improvement_plan=existing_result["improvement_plan"],
            questions=questions_list,
            interview_type=interview.get("interview_type", "Technical")
        )
        
    # Calculate average scores
    avg_tech = sum(qa["technical_score"] for qa in qas) / len(qas)
    avg_comm = sum(qa["communication_score"] for qa in qas) / len(qas)
    avg_rel = sum(qa["relevance_score"] for qa in qas) / len(qas)
    overall_score = (avg_tech + avg_comm + avg_rel) / 3
    
    # Generate final summary via Gemini
    summary = generate_results_summary(
        job_role=interview["job_role"],
        interview_type=interview["interview_type"],
        qa_list=qas,
        difficulty=interview.get("difficulty", "Medium"),
        experience_level=current_user.get("experience_level", "Mid-Level"),
        skills=current_user.get("skills", [])
    )
    
    final_result = {
        "interview_id": oid,
        "overall_score": round(overall_score, 1),
        "technical_score": round(avg_tech, 1),
        "communication_score": round(avg_comm, 1),
        "relevance_score": round(avg_rel, 1),
        "weak_topics": summary["weak_topics"],
        "improvement_plan": summary["improvement_plan"]
    }
    
    results_collection.insert_one(final_result)
    
    # Update interview status to completed
    interviews_collection.update_one(
        {"_id": oid},
        {"$set": {"status": "completed"}}
    )
    
    questions_list = [
        QuestionAnswerDetail(
            question_number=qa["question_number"],
            question=qa["question"],
            type=qa.get("type", "descriptive"),
            options=qa.get("options", []),
            answer=qa["answer"],
            technical_score=qa["technical_score"],
            communication_score=qa["communication_score"],
            relevance_score=qa["relevance_score"],
            feedback=qa["feedback"],
            weak_topic=qa.get("weak_topic")
        ) for qa in qas
    ]
    
    return ResultsResponse(
        interview_id=interview_id,
        overall_score=final_result["overall_score"],
        technical_score=final_result["technical_score"],
        communication_score=final_result["communication_score"],
        relevance_score=final_result["relevance_score"],
        weak_topics=final_result["weak_topics"],
        improvement_plan=final_result["improvement_plan"],
        questions=questions_list,
        interview_type=interview.get("interview_type", "Technical")
    )
