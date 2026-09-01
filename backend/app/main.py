from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_db
from app.routes.auth import router as auth_router
from app.routes.profile import router as profile_router
from app.routes.interview import router as interview_router
from app.routes.history import router as history_router

app = FastAPI(
    title="AI Interview Preparation Assistant API",
    description="Backend API for conducting, scoring, and analyzing mock interviews using Gemini and MongoDB.",
    version="1.0.0"
)

# CORS middleware configuration
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers under the "/api" prefix
app.include_router(auth_router, prefix="/api")
app.include_router(profile_router, prefix="/api")
app.include_router(interview_router, prefix="/api")
app.include_router(history_router, prefix="/api")

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "AI Interview Preparation Assistant API is running."
    }
