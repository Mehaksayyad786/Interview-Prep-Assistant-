from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

# Auth Models
class UserRegister(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    education: Optional[str] = ""
    skills: List[str] = []
    experience_level: Optional[str] = ""
    preferred_job_role: Optional[str] = ""

class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    education: Optional[str] = None
    skills: Optional[List[str]] = None
    experience_level: Optional[str] = None
    preferred_job_role: Optional[str] = None

# Interview Setup Models
class InterviewStartRequest(BaseModel):
    job_role: str
    interview_type: str
    difficulty: str

class InterviewResponse(BaseModel):
    id: str
    user_id: str
    job_role: str
    interview_type: str
    difficulty: str
    status: str
    date: str

# Live Q&A Models
class AnswerSubmitRequest(BaseModel):
    question_number: int
    answer: str

class QuestionResponse(BaseModel):
    interview_id: str
    question_number: int
    question: str
    type: Optional[str] = "descriptive"
    options: Optional[List[str]] = []
    is_completed: bool = False

class EvaluationResponse(BaseModel):
    technical_score: int
    communication_score: int
    relevance_score: int
    feedback: str
    weak_topic: Optional[str] = None

class QuestionAnswerDetail(BaseModel):
    question_number: int
    question: str
    type: Optional[str] = "descriptive"
    options: Optional[List[str]] = []
    answer: Optional[str] = None
    technical_score: Optional[int] = None
    communication_score: Optional[int] = None
    relevance_score: Optional[int] = None
    feedback: Optional[str] = None
    weak_topic: Optional[str] = None

# Final Results Models
class ResultsResponse(BaseModel):
    interview_id: str
    overall_score: float
    technical_score: float
    communication_score: float
    relevance_score: float
    weak_topics: List[str]
    improvement_plan: List[str]
    questions: List[QuestionAnswerDetail]
    interview_type: Optional[str] = "Technical"
