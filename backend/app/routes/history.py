from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId
from typing import List, Optional
from pydantic import BaseModel

from app.database import interviews_collection, results_collection, questions_answers_collection
from app.models import ResultsResponse, QuestionAnswerDetail
from app.auth import get_current_user

router = APIRouter(tags=["History & Results"])

class HistoryItem(BaseModel):
    id: str
    job_role: str
    interview_type: str
    difficulty: str
    status: str
    date: str
    overall_score: Optional[float] = None
    weak_topics: Optional[List[str]] = []

@router.get("/history", response_model=List[HistoryItem])
def get_interview_history(current_user: dict = Depends(get_current_user)):
    interviews = list(interviews_collection.find({"user_id": current_user["_id"]}).sort("date", -1))
    
    history_list = []
    for interview in interviews:
        iid = interview["_id"]
        result = results_collection.find_one({"interview_id": iid})
        
        overall_score = None
        weak_topics = []
        if result:
            overall_score = result.get("overall_score")
            weak_topics = result.get("weak_topics", [])
            
        history_list.append(HistoryItem(
            id=str(iid),
            job_role=interview["job_role"],
            interview_type=interview["interview_type"],
            difficulty=interview["difficulty"],
            status=interview["status"],
            date=interview["date"],
            overall_score=overall_score,
            weak_topics=weak_topics
        ))
        
    return history_list

@router.get("/results/{interview_id}", response_model=ResultsResponse)
def get_interview_results(interview_id: str, current_user: dict = Depends(get_current_user)):
    try:
        oid = ObjectId(interview_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid interview ID format")
        
    interview = interviews_collection.find_one({"_id": oid, "user_id": current_user["_id"]})
    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")
        
    result = results_collection.find_one({"interview_id": oid})
    if not result:
        raise HTTPException(status_code=404, detail="Results not generated or interview in progress")
        
    # Fetch questions and answers details
    qas = list(questions_answers_collection.find({"interview_id": oid}).sort("question_number", 1))
    
    questions_list = [
        QuestionAnswerDetail(
            question_number=qa["question_number"],
            question=qa["question"],
            type=qa.get("type", "descriptive"),
            options=qa.get("options", []),
            answer=qa.get("answer"),
            technical_score=qa.get("technical_score"),
            communication_score=qa.get("communication_score"),
            relevance_score=qa.get("relevance_score"),
            feedback=qa.get("feedback"),
            weak_topic=qa.get("weak_topic")
        ) for qa in qas
    ]
    
    return ResultsResponse(
        interview_id=interview_id,
        overall_score=result["overall_score"],
        technical_score=result["technical_score"],
        communication_score=result["communication_score"],
        relevance_score=result["relevance_score"],
        weak_topics=result["weak_topics"],
        improvement_plan=result["improvement_plan"],
        questions=questions_list,
        interview_type=interview.get("interview_type", "Technical")
    )
