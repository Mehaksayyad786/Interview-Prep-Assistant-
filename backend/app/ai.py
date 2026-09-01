import os
import json
import random
import google.generativeai as genai
from app.config import settings

def configure_ai():
    api_key = settings.GEMINI_API_KEY
    if not api_key:
        api_key = os.environ.get("GEMINI_API_KEY", "")
    genai.configure(api_key=api_key)

def get_predefined_question(job_role: str, interview_type: str, question_number: int) -> dict:
    # Legacy wrapper helper
    from app.questions_bank import get_predefined_question_base
    return get_predefined_question_base(job_role, interview_type, question_number)

ROLE_DIFFICULTY_TOPICS = {
    "AI Engineer": {
        "Easy": ["Basic Regression Techniques", "Outlier Identification", "Train/Test Dataset Splitting", "Sigmoid Activation Function", "Supervised Learning Fundamentals"],
        "Medium": ["Transformer Backbone Architectures", "Dropout Regularization in Deep Learning", "Self-Attention Mechanism", "Model Fine-Tuning Techniques", "Hyperparameter Selection"],
        "Hard": ["Direct Preference Optimization (DPO)", "Reinforcement Learning from Human Feedback (RLHF)", "Gradient Drift in Deep Networks", "Advanced Attention Architectures", "High-Dimensional Vector Operations"]
    },
    "Python Developer": {
        "Easy": ["Python Data Types & Mutability", "List Comprehension Syntax", "Basic File I/O Operations", "Standard Library Functions", "String Manipulation Methods"],
        "Medium": ["Decorator Patterns & Implementations", "Generator Functions & Yield keyword", "Context Managers and 'with' blocks", "Exception Handling Best Practices", "Multi-threading vs Multi-processing constraints"],
        "Hard": ["Metaclass Templates & Custom Class Creation", "Java/Python Interoperability & Memory Models", "Garbage Collection & Weak References", "Asynchronous Event Loop (asyncio) internals", "GIL (Global Interpreter Lock) Workarounds"]
    },
    "Data Analyst": {
        "Easy": ["SQL Filtering & WHERE Clauses", "Aggregations using GROUP BY", "Basic JOIN Types", "Excel/Pandas Basic Operations", "Standard Deviation & Mean Concepts"],
        "Medium": ["SQL Window Functions", "Data Normalization Rules", "Time-series Aggregations", "Pandas Merge & GroupBy Operations", "Data Visualization Choices"],
        "Hard": ["Complex Query Optimization & Indexing", "Statistical Significance Testing", "Predictive Analytics Setup", "Advanced ETL Pipeline Design", "Multi-source Data Integration Patterns"]
    },
    "Data Scientist": {
        "Easy": ["Basic Statistics & Measures of Central Tendency", "Linear Regression Assumptions", "Supervised vs Unsupervised Split", "Data Cleansing Steps", "Feature Scaling Techniques"],
        "Medium": ["Random Forest & Decision Tree Hyperparameters", "Feature Selection Methods", "Cross-Validation Techniques", "Handling Imbalanced Datasets", "Dimensionality Reduction using PCA"],
        "Hard": ["Ensemble Boosting Algorithms (XGBoost, LightGBM)", "Gradient Descent Optimization Math", "Markov Chain Models", "Deep Neural Networks for Tabular Data", "Bayesian Inference Models"]
    },
    "Machine Learning Engineer": {
        "Easy": ["Machine Learning Model Evaluation Metrics", "Underfitting vs Overfitting Indicators", "Basic Pipeline Development", "Dataset Storage Formats", "Model Inference Fundamentals"],
        "Medium": ["Model Deployment & Dockerization", "API Endpoint Creation for ML Models", "Feature Store Implementations", "CI/CD for Machine Learning", "Model Versioning Best Practices"],
        "Hard": ["Automated Performance Decay Monitoring", "Production Drift Diagnostics & Retraining Pipelines", "GPU Memory Management & Distributed Training", "Model Quantization & Pruning", "Real-time Low-latency Inference Optimizations"]
    },
    "Java Developer": {
        "Easy": ["Java OOP Fundamentals", "Basic Exception Handling", "Java Collections Framework (ArrayList, HashMap)", "Java Syntax & Compilation", "Access Modifiers"],
        "Medium": ["Garbage Collection Algorithms in JVM", "Abstract Classes vs Interfaces", "Java Multithreading & Runnable interface", "Streams API & Lambda Expressions", "Spring Boot Dependency Injection"],
        "Hard": ["Java Memory Model (JMM) visibility/ordering rules", "Happens-before Guarantees & volatile keyword", "JVM Memory Tuning & OutOfMemory Diagnostics", "Concurrency Utilities (Locks, Semaphores)", "Bytecode Manipulation & Reflection Performance"]
    }
}

HR_TOPICS = {
    "Easy": [
        "Company Motivation & Interest Alignment",
        "Cultural Fit & Personal Core Values",
        "Basic Communication Clarity",
        "Hobbies and Work-Life Balance Expression",
        "Resume and Experience Presentation"
    ],
    "Medium": [
        "Long-term Career Planning & Growth Motivation",
        "Receiving and Incorporating Constructive Feedback",
        "Compensation Expectations Alignment & Value Articulation",
        "Understanding Organizational Structure & Dynamics",
        "Ethics and Professional Conduct"
    ],
    "Hard": [
        "Securing Stakeholder Buy-in & Executive Presence",
        "Managing Long-term Career and Personal Goals alignment",
        "Unpopular Decision-Making & Leadership Philosophy",
        "Handling sudden resource cuts or organizational shifts"
    ]
}

BEHAVIORAL_TOPICS = {
    "Easy": [
        "Handling Basic Disagreements constructively",
        "Teamwork and General Collaboration",
        "Active Listening & Empathy",
        "Basic STAR Method Structure"
    ],
    "Medium": [
        "Conflict Resolution & Collaboration inside Teams",
        "Leadership Initiative & Project Management",
        "Constructive Disagreement with Management",
        "Handling Tight Deadlines & Prioritization",
        "Ownership & Taking Responsibility"
    ],
    "Hard": [
        "Managing Scope Creep & Adjusting Priorities under High Pressure",
        "Negotiation of System Failures & Post-Mortem Accountability",
        "Sudden Team Resource Losses & Gap Management",
        "High-Pressure Scenario Stress Management"
    ]
}

def local_evaluate_answer(question: str, answer: str, job_role: str, interview_type: str, difficulty: str = "Medium", experience_level: str = "Mid-Level", skills: list = []) -> dict:
    from app.database import questions_collection
    predefined_q = questions_collection.find_one({"question": question})
    
    q_type = "descriptive"
    correct_ans = ""
    
    if predefined_q:
        q_type = predefined_q.get("type", "descriptive")
        correct_ans = predefined_q.get("correct_answer", "")
        
    answer_clean = answer.strip().lower()
    
    is_non_tech = interview_type in ["HR", "Behavioral"]
    question_lower = question.lower()
    
    # Check if this specific question is technical in nature (e.g. if a technical FIB/MCQ is in Behavioral pool)
    is_tech_question = not is_non_tech or any(kw in question_lower for kw in [
        "data", "sql", "code", "programming", "python", "java", "architecture", "framework", "api", 
        "database", "validation", "git", "docker", "pipeline", "etl", "machine learning", "neural", 
        "model", "algorithm", "memory", "exception", "concurrency", "thread", "queries", "syntax", "compile"
    ])
    
    # MCQ scoring logic
    if q_type == "mcq" and correct_ans:
        correct_letter = correct_ans.strip().lower()
        is_correct = False
        
        # User answer matches exact letter e.g. "a" or starts with "a)"
        if answer_clean.startswith(correct_letter):
            is_correct = True
        elif len(answer_clean) == 1 and answer_clean == correct_letter:
            is_correct = True
        # Match option string value
        elif predefined_q.get("options"):
            options_list = predefined_q["options"]
            letter_idx = ord(correct_letter) - ord('a')
            if 0 <= letter_idx < len(options_list):
                opt_val = options_list[letter_idx].lower()
                if opt_val in answer_clean:
                    is_correct = True
                    
        if is_correct:
            return {
                "technical_score": random.randint(95, 100),
                "communication_score": random.randint(90, 96),
                "relevance_score": random.randint(96, 100),
                "feedback": f"Correct! You successfully identified option '{correct_ans.upper()}' as the correct answer.",
                "weak_topic": None
            }
        else:
            if is_tech_question:
                topics = ROLE_DIFFICULTY_TOPICS.get(job_role, {}).get(difficulty, [f"{job_role} Core Architecture"])
                weak_topic = topics[0] if len(topics) > 0 else f"{job_role} Core Architecture"
                feedback_detail = f" Reviewing technical choices related to '{weak_topic}' is key for a {job_role}."
            else:
                if interview_type == "HR":
                    topics = HR_TOPICS.get(difficulty, HR_TOPICS["Medium"])
                    weak_topic = topics[0] if len(topics) > 0 else "Cultural Fit & Value Alignment"
                    feedback_detail = " For an HR scenario, aligning with the expected professional option is key to demonstrating organizational awareness."
                else:
                    topics = BEHAVIORAL_TOPICS.get(difficulty, BEHAVIORAL_TOPICS["Medium"])
                    weak_topic = topics[0] if len(topics) > 0 else "Behavioral Response Structure"
                    feedback_detail = " For a behavioral scenario, selecting options that demonstrate collaboration and conflict resolution is key."
                
            return {
                "technical_score": random.randint(15, 30),
                "communication_score": random.randint(70, 80),
                "relevance_score": random.randint(85, 95),
                "feedback": f"Incorrect option selected. The correct answer was option '{correct_ans.upper()}'.{feedback_detail}",
                "weak_topic": weak_topic
            }
            
    # Fill in the blank scoring logic
    elif q_type == "fib" and correct_ans:
        correct_term = correct_ans.strip().lower()
        if correct_term in answer_clean:
            return {
                "technical_score": random.randint(92, 98),
                "communication_score": random.randint(88, 94),
                "relevance_score": random.randint(95, 98),
                "feedback": f"Excellent! You correctly completed the blank with '{correct_ans}'.",
                "weak_topic": None
            }
        else:
            if is_tech_question:
                # Assign a relevant technical topic based on keywords
                if "data" in question_lower or "validation" in question_lower or "quality" in question_lower:
                    weak_topic = "Data Quality & Validation"
                elif "sql" in question_lower or "database" in question_lower:
                    weak_topic = "Database & Query Optimization"
                elif "git" in question_lower or "docker" in question_lower or "pipeline" in question_lower:
                    weak_topic = "DevOps & Pipelines"
                elif "model" in question_lower or "machine learning" in question_lower or "ai" in question_lower:
                    weak_topic = "Machine Learning & AI Concepts"
                else:
                    topics = ROLE_DIFFICULTY_TOPICS.get(job_role, {}).get(difficulty, [f"{job_role} Terminology"])
                    weak_topic = topics[1] if len(topics) > 1 else topics[0] if len(topics) > 0 else f"{job_role} Terminology"
                feedback_detail = f" Reviewing definitions related to '{weak_topic}' under {difficulty} difficulty will help reinforce this concept."
            else:
                if interview_type == "HR":
                    topics = HR_TOPICS.get(difficulty, HR_TOPICS["Medium"])
                    weak_topic = topics[1] if len(topics) > 1 else topics[0] if len(topics) > 0 else "HR Communication"
                    feedback_detail = " Reinforcing core HR alignment concepts will help you answer professional motivation questions more effectively."
                else:
                    topics = BEHAVIORAL_TOPICS.get(difficulty, BEHAVIORAL_TOPICS["Medium"])
                    weak_topic = topics[1] if len(topics) > 1 else topics[0] if len(topics) > 0 else "STAR Framework Terminology"
                    feedback_detail = " Reviewing behavioral response structures and terminology will help you frame your situational examples."
                
            return {
                "technical_score": random.randint(25, 45),
                "communication_score": random.randint(65, 75),
                "relevance_score": random.randint(60, 70),
                "feedback": f"Incorrect. The expected term for the blank was '{correct_ans}'.{feedback_detail}",
                "weak_topic": weak_topic
            }
            
    # Descriptive scoring logic
    else:
        word_count = len(answer_clean.split())
        
        if not is_tech_question:
            if word_count > 45:
                if interview_type == "HR":
                    feedback_msg = f"Excellent response! Your answer is well-articulated and demonstrates strong professional alignment, cultural fit, and maturity expected of a {experience_level} candidate."
                else:
                    feedback_msg = f"Outstanding answer! You have structured your response beautifully, demonstrating strong emotional intelligence and situational awareness appropriate for a {experience_level} candidate using the STAR method."
                return {
                    "technical_score": random.randint(85, 95),
                    "communication_score": random.randint(88, 96),
                    "relevance_score": random.randint(90, 98),
                    "feedback": feedback_msg,
                    "weak_topic": None
                }
            elif word_count > 20:
                if interview_type == "HR":
                    topics = HR_TOPICS.get(difficulty, HR_TOPICS["Medium"])
                    weak_topic = topics[2] if len(topics) > 2 else topics[0] if len(topics) > 0 else "Career Planning Motivation"
                    feedback_msg = f"Good attempt. However, for a {difficulty}-level HR question, your response could highlight company alignment and personal values better. Try explaining your motivations and long-term career goals more explicitly as a {experience_level} candidate."
                else:
                    topics = BEHAVIORAL_TOPICS.get(difficulty, BEHAVIORAL_TOPICS["Medium"])
                    weak_topic = topics[2] if len(topics) > 2 else topics[0] if len(topics) > 0 else "STAR Framework Structure"
                    feedback_msg = f"Good attempt. However, for a {difficulty}-level behavioral question, your response lacks specific detail. As a {experience_level} candidate, try using the STAR method (Situation, Task, Action, Result) to explain the details, your action, and the outcome."
                return {
                    "technical_score": random.randint(65, 75),
                    "communication_score": random.randint(70, 80),
                    "relevance_score": random.randint(75, 85),
                    "feedback": feedback_msg,
                    "weak_topic": weak_topic
                }
            else:
                if interview_type == "HR":
                    topics = HR_TOPICS.get(difficulty, HR_TOPICS["Medium"])
                    weak_topic = topics[3] if len(topics) > 3 else topics[0] if len(topics) > 0 else "Response Elaboration & Context"
                    feedback_msg = f"Your response is too brief. HR questions require explaining your career aspirations, values, and how you align with the organization's culture. Please elaborate with at least 2-3 detailed sentences."
                else:
                    topics = BEHAVIORAL_TOPICS.get(difficulty, BEHAVIORAL_TOPICS["Medium"])
                    weak_topic = topics[3] if len(topics) > 3 else topics[0] if len(topics) > 0 else "Response Elaboration & Context"
                    feedback_msg = f"Your response is too short. Behavioral questions require explaining the specific context, the action you took, and the results of your actions. Please structure your response using the STAR method with at least 2-3 detailed sentences."
                return {
                    "technical_score": random.randint(40, 50),
                    "communication_score": random.randint(50, 60),
                    "relevance_score": random.randint(55, 65),
                    "feedback": feedback_msg,
                    "weak_topic": weak_topic
                }
        else:
            topics = ROLE_DIFFICULTY_TOPICS.get(job_role, {}).get(difficulty, [])
            if word_count > 45:
                feedback_msg = f"Excellent explanation! As a candidate with {experience_level} experience, your description of this concept shows a solid grasp of the underlying principles. Your detailed answer is well-structured and relevant."
                if skills:
                    feedback_msg += f" This aligns well with your experience in {skills[0]}."
                return {
                    "technical_score": random.randint(82, 92),
                    "communication_score": random.randint(84, 92),
                    "relevance_score": random.randint(88, 96),
                    "feedback": feedback_msg,
                    "weak_topic": None
                }
            elif word_count > 20:
                weak_topic = topics[2] if len(topics) > 2 else topics[0] if len(topics) > 0 else f"{job_role} In-Depth Design"
                feedback_msg = f"Good attempt. However, for a {difficulty} difficulty question, your answer lacks depth. As a {experience_level} candidate, you should provide more specific examples or explain the architectural trade-offs in greater detail."
                return {
                    "technical_score": random.randint(68, 78),
                    "communication_score": random.randint(70, 82),
                    "relevance_score": random.randint(75, 86),
                    "feedback": feedback_msg,
                    "weak_topic": weak_topic
                }
            else:
                weak_topic = topics[3] if len(topics) > 3 else topics[0] if len(topics) > 0 else f"{job_role} Basic Syntax/Definitions"
                feedback_msg = f"Your response is too brief for a {job_role} role. At the {experience_level} level, a more comprehensive explanation covering syntax, logic, or best practices is expected."
                return {
                    "technical_score": random.randint(40, 55),
                    "communication_score": random.randint(50, 62),
                    "relevance_score": random.randint(55, 65),
                    "feedback": feedback_msg,
                    "weak_topic": weak_topic
                }

def evaluate_answer(question: str, answer: str, job_role: str, interview_type: str, difficulty: str = "Medium", experience_level: str = "Mid-Level", skills: list = []) -> dict:
    configure_ai()
    
    api_key = settings.GEMINI_API_KEY
    if not api_key:
        api_key = os.environ.get("GEMINI_API_KEY", "")
        
    is_gemini_configured = api_key and not api_key.startswith("YOUR_")
    is_non_tech = interview_type in ["HR", "Behavioral"]
    
    if is_gemini_configured:
        model = genai.GenerativeModel("gemini-3.5-flash")
        if is_non_tech:
            if interview_type == "HR":
                prompt = f"""You are an expert HR interviewer evaluating a candidate's response for a human resources/cultural alignment interview.

Question:
{question}

Candidate's Answer:
{answer}

Context:
- Interview Type: HR (Human Resources & Cultural Fit)
- Interview Difficulty Level: {difficulty}
- Candidate Experience Level: {experience_level}
- Candidate Skills: {", ".join(skills) if skills else "None specified"}

Evaluate the response objectively on:
1. HR correctness and cultural maturity (score from 0-100). Check if they answered logically, professionally, and exhibited good values/character and organizational awareness.
   - Adjust grading rigor based on Interview Difficulty ({difficulty}) and Candidate Experience Level ({experience_level}). For example, expect high professional alignment and long-term planning from Senior candidates.
2. Communication clarity (score from 0-100)
3. Answer relevance to the question asked (score from 0-100)
4. Feedback: Provide a constructive, personalized critique (under 3 sentences). 
   - MUST be highly tailored to the HR and cultural alignment context.
   - **CRITICAL**: Focus entirely on HR-specific aspects such as alignment with company culture/values, motivation, professional commitment, ethics, and career alignment. Do NOT mention the STAR method framework; evaluate overall professional presence and soft skills. Do NOT include technical/coding details.
5. Weak topic: Identify a single specific soft skill/behavioral area that needs improvement. If the answer is perfect, return null.
   - **CRITICAL**: The weak topic MUST be a specific soft skill/HR theme (e.g. "Cultural Value Alignment", "Company Motivation Articulation", "Professional Growth Clarity"), NOT a technical coding topic.

You MUST return your evaluation in this EXACT JSON structure:
{{
  "technical_score": integer,
  "communication_score": integer,
  "relevance_score": integer,
  "feedback": "string",
  "weak_topic": "string or null"
}}
"""
            else:  # Behavioral
                prompt = f"""You are an expert behavioral interviewer evaluating a candidate's response for a situational/behavioral interview.

Question:
{question}

Candidate's Answer:
{answer}

Context:
- Interview Type: Behavioral (Situational & Team Dynamics)
- Interview Difficulty Level: {difficulty}
- Candidate Experience Level: {experience_level}
- Candidate Skills: {", ".join(skills) if skills else "None specified"}

Evaluate the response objectively on:
1. Behavioral correctness and situational maturity (score from 0-100). Check if they answered logically, professionally, and exhibited good teamwork, leadership, and conflict resolution.
   - Adjust grading rigor based on Interview Difficulty ({difficulty}) and Candidate Experience Level ({experience_level}). Expect well-structured situational examples using the STAR method from Senior candidates.
2. Communication clarity (score from 0-100)
3. Answer relevance to the question asked (score from 0-100)
4. Feedback: Provide a constructive, personalized critique (under 3 sentences). 
   - MUST be highly tailored to the Behavioral situational context.
   - **CRITICAL**: Focus entirely on behavioral-specific aspects such as structuring responses using the STAR method (Situation, Task, Action, Result), problem-solving under pressure, teamwork dynamics, and action-oriented results. Do NOT include technical/coding details.
5. Weak topic: Identify a single specific soft skill/behavioral area that needs improvement. If the answer is perfect, return null.
   - **CRITICAL**: The weak topic MUST be a specific behavioral/soft skill theme (e.g. "Detailing STAR Results", "Constructive Conflict Resolution", "Structuring Action Explanations"), NOT a technical coding topic.

You MUST return your evaluation in this EXACT JSON structure:
{{
  "technical_score": integer,
  "communication_score": integer,
  "relevance_score": integer,
  "feedback": "string",
  "weak_topic": "string or null"
}}
"""
        else:
            prompt = f"""You are an expert interviewer evaluating a candidate's response.

Question:
{question}

Candidate's Answer:
{answer}

Context:
- Job Role: {job_role}
- Interview Type: {interview_type}
- Interview Difficulty Level: {difficulty}
- Candidate Experience Level: {experience_level}
- Candidate Skills: {", ".join(skills) if skills else "None specified"}

Evaluate the response objectively on:
1. Technical correctness (score from 0-100). If the question is an MCQ or Fill in the blank, check if they got it right.
   - Adjust grading rigor based on Interview Difficulty ({difficulty}) and Candidate Experience Level ({experience_level}). For example, be more critical of basic errors for Senior candidates on Hard difficulty, and provide guidance appropriate for their level.
2. Communication clarity (score from 0-100)
3. Answer relevance to the question asked (score from 0-100)
4. Feedback: Provide a constructive, personalized critique (under 3 sentences). 
   - MUST be highly tailored to the specific job role ({job_role}), difficulty level ({difficulty}), and candidate experience level ({experience_level}). 
   - Incorporate suggestions referencing the candidate's skills when relevant, advising them how to apply or improve their understanding of this topic.
5. Weak topic: Identify a single specific topic area that needs improvement. If the answer is perfect, return null.
   - The weak topic MUST be highly specific, professional, and unique to the combination of the {job_role} role and {difficulty} difficulty (e.g. instead of a generic "Python Basic Syntax/Definitions" or "AI Engineer Core Architecture", return a specific sub-topic like "Python Memory Management under Hard level" or "Vector Embeddings Optimization").

You MUST return your evaluation in this EXACT JSON structure:
{{
  "technical_score": integer,
  "communication_score": integer,
  "relevance_score": integer,
  "feedback": "string",
  "weak_topic": "string or null"
}}
"""
        try:
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    response_mime_type="application/json"
                )
            )
            data = json.loads(response.text.strip())
            # Ensure scores are within bounds
            for score_field in ["technical_score", "communication_score", "relevance_score"]:
                if score_field in data:
                    data[score_field] = max(0, min(100, int(data[score_field])))
                else:
                    data[score_field] = 50
            return data
        except Exception as e:
            print(f"Gemini API evaluation failed, falling back to local: {e}")
            
    # Local fallback
    return local_evaluate_answer(question, answer, job_role, interview_type, difficulty, experience_level, skills)


def generate_results_summary(job_role: str, interview_type: str, qa_list: list, difficulty: str = "Medium", experience_level: str = "Mid-Level", skills: list = []) -> dict:
    configure_ai()
    
    api_key = settings.GEMINI_API_KEY
    if not api_key:
        api_key = os.environ.get("GEMINI_API_KEY", "")
        
    is_gemini_configured = api_key and not api_key.startswith("YOUR_")
    is_non_tech = interview_type in ["HR", "Behavioral"]
    
    if is_gemini_configured:
        model = genai.GenerativeModel("gemini-3.5-flash")
        qa_formatted = []
        for qa in qa_list:
            qa_formatted.append(f"""
Question: {qa.get('question')}
Candidate's Answer: {qa.get('answer', 'N/A')}
Scores: Technical={qa.get('technical_score', 0)}, Communication={qa.get('communication_score', 0)}, Relevance={qa.get('relevance_score', 0)}
Feedback: {qa.get('feedback', '')}
Weak Topic: {qa.get('weak_topic', 'None')}
""")
        
        qa_text = "\n---\n".join(qa_formatted)
        if is_non_tech:
            prompt = f"""You are a professional HR and behavioral interview coach reviewing a completed session.

Context:
- Interview Type: {interview_type} (Non-technical)
- Difficulty Level: {difficulty}
- Candidate Experience Level: {experience_level}
- Candidate Declared Skills: {", ".join(skills) if skills else "None specified"}

Here is the candidate's performance across the questions:
{qa_text}

Analyze the scores, feedback, and weak topics to:
1. Synthesize a unified list of weak topics where the candidate needs improvement. Limit this to the top 2 or 3 most prominent topics.
   - **CRITICAL**: These weak topics MUST be highly specific soft skill or behavioral themes (e.g., "Conflict Negotiation Nuance", "Articulating Personal Career Values", "Structuring STAR Results"). Do NOT include any technical, code, or programming themes.
2. Create a personalized, actionable improvement plan. Provide exactly 4-5 concrete, practical steps they should take.
   - The action steps MUST be tailored to the candidate's experience level ({experience_level}) and focus on soft skills, behavioral strategies, interview presentation, and situational framing. Do NOT suggest technical learning, coding practice, or engineering design patterns.

You MUST return your analysis in this EXACT JSON structure:
{{
  "weak_topics": ["topic 1", "topic 2"],
  "improvement_plan": [
    "action step 1",
    "action step 2"
  ]
}}
"""
        else:
            prompt = f"""You are a professional interview coach reviewing a completed interview session.

Context:
- Job Role: {job_role}
- Interview Type: {interview_type}
- Difficulty Level: {difficulty}
- Candidate Experience Level: {experience_level}
- Candidate Declared Skills: {", ".join(skills) if skills else "None specified"}

Here is the candidate's performance across the questions:
{qa_text}

Analyze the scores, feedback, and weak topics to:
1. Synthesize a unified list of weak topics where the candidate needs improvement. Limit this to the top 2 or 3 most prominent topics.
   - These weak topics MUST be highly specific, granular, and unique to the job role ({job_role}) and the difficulty level ({difficulty}) of the interview. Avoid generic names.
2. Create a personalized, actionable improvement plan. Provide exactly 4-5 concrete, practical steps they should take.
   - The action steps MUST be tailored to the candidate's experience level ({experience_level}) and difficulty level ({difficulty}).
   - If applicable, mention how they can leverage or build upon their skills ({", ".join(skills) if skills else "existing tech stack"}) to address these weak areas.

You MUST return your analysis in this EXACT JSON structure:
{{
  "weak_topics": ["topic 1", "topic 2"],
  "improvement_plan": [
    "action step 1",
    "action step 2"
  ]
}}
"""
        try:
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    response_mime_type="application/json"
                )
            )
            data = json.loads(response.text.strip())
            return data
        except Exception as e:
            print(f"Gemini API summary failed, falling back to local: {e}")
            
    # Local fallback
    raw_topics = [qa.get("weak_topic") for qa in qa_list if qa.get("weak_topic")]
    weak_topics = list(set([t for t in raw_topics if t]))
    
    if is_non_tech:
        if not weak_topics:
            if interview_type == "HR":
                topics_pool = HR_TOPICS.get(difficulty, HR_TOPICS["Medium"])
            else:
                topics_pool = BEHAVIORAL_TOPICS.get(difficulty, BEHAVIORAL_TOPICS["Medium"])
            weak_topics = [topics_pool[2] if len(topics_pool) > 2 else topics_pool[0]]
            
        if interview_type == "HR":
            if difficulty == "Easy":
                improvement_plan = [
                    f"Research the mission and core values of the companies you are targeting for junior {job_role} positions.",
                    f"Practice articulating your basic career motivations and background as an entry-level {job_role} clearly.",
                    "Prepare standard professional responses regarding punctuality, workplace etiquette, and working under guidance.",
                    f"Refine your {job_role} resume to highlight key projects, tools, and academic qualifications."
                ]
            elif difficulty == "Hard":
                improvement_plan = [
                    f"Define and practice articulating your leadership philosophy and how you mentor junior team members as a senior {job_role}.",
                    f"Develop a clear framework for articulating salary expectations based on market rates and your unique {job_role} capabilities.",
                    "Practice high-level stakeholder management communication and negotiation strategies for complex technical projects.",
                    f"Refine your long-term career roadmap as a senior {job_role}, demonstrating alignment with executive business goals."
                ]
            else:  # Medium
                improvement_plan = [
                    f"Prepare a clear narrative of your career progression and where you see your role as a {job_role} evolving in 5 years.",
                    f"Practice responding to constructive feedback and showing adaptability in professional {job_role} settings.",
                    "Prepare examples of professional disagreements with management and how you resolved them constructively.",
                    "Align your professional values with the target company's engineering and business culture."
                ]
        else:  # Behavioral
            if difficulty == "Easy":
                improvement_plan = [
                    f"Practice structuring situational stories using the STAR method for entry-level {job_role} team projects.",
                    f"Focus on highlighting your teamwork, accountability, and cooperation in helper roles on {job_role} tasks.",
                    "Prepare examples of following guidelines and instructions carefully to resolve basic technical roadblocks.",
                    "Learn to describe the results of your actions quantitatively when explaining simple problem-solving experiences."
                ]
            elif difficulty == "Hard":
                improvement_plan = [
                    f"Prepare senior-level STAR responses detailing how you managed risk, resolved critical system failures, and handled high-pressure delays on {job_role} projects.",
                    f"Practice describing how you managed scope creep, secured stakeholder buy-in, and navigated sudden resource changes as a lead {job_role}.",
                    "Refine your examples of making unpopular technical decisions, outlining the business impact and risk mitigations.",
                    "Highlight post-mortem accountability, root cause analysis, and long-term preventive actions in your situational stories."
                ]
            else:  # Medium
                improvement_plan = [
                    f"Develop detailed STAR stories highlighting your initiative, problem-solving, and task prioritization on {job_role} projects.",
                    f"Practice describing how you handled tight deadlines, managed workloads, and resolved peer conflicts in {job_role} teams.",
                    "Refine your ability to explain the technical actions you took and how they contributed directly to the team's success.",
                    "Prepare stories showing flexibility when adapting to new requirements or adopting new tools in active projects."
                ]
    else:
        if not weak_topics:
            topics_pool = ROLE_DIFFICULTY_TOPICS.get(job_role, {}).get(difficulty, [f"{job_role} Advanced Operations"])
            weak_topics = [topics_pool[4] if len(topics_pool) > 4 else topics_pool[0]]
            
        if difficulty == "Easy":
            improvement_plan = [
                f"Master the foundational syntactical rules and core concepts of {job_role} before attempting advanced projects.",
                f"Practice explaining basic algorithms, queries, or architectures associated with {job_role} roles clearly and concisely.",
                f"Focus on basic debugging and unit testing for {job_role} tasks."
            ]
        elif difficulty == "Hard":
            improvement_plan = [
                f"Research advanced system design, low-level optimization, and distributed systems topics critical for Senior {job_role} roles.",
                f"Practice whiteboarding and explaining complex architectural decisions, memory management models, and data pipelines.",
                f"Conduct mock design reviews focusing on high-concurrency, security, and scalability constraints in {job_role} production environments."
            ]
        else:  # Medium
            improvement_plan = [
                f"Study mid-level architectural patterns, framework constraints, and optimization techniques relevant to a {job_role}.",
                f"Practice detailing technical tradeoffs (e.g., speed vs memory, synchronous vs asynchronous) expected of a professional {job_role}.",
                f"Enhance your troubleshooting skills by analyzing performance bottlenecks in {job_role} applications."
            ]
            
        if skills:
            improvement_plan.append(f"Connect these concepts back to your existing skills like {', '.join(skills[:3])} to build stronger practical analogies.")
        else:
            improvement_plan.append(f"Practice setting up small side projects or code snippets to translate theoretical {job_role} knowledge into practice.")
            
        improvement_plan.append("Work on timing constraints and structured explanations (like the STAR method for behavioral/descriptive questions).")
        
    return {
        "weak_topics": weak_topics,
        "improvement_plan": improvement_plan
    }
