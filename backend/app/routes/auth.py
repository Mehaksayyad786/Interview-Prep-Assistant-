from fastapi import APIRouter, HTTPException, Depends, status
from bson import ObjectId
from app.database import users_collection
from app.models import UserRegister, UserLogin, Token, UserResponse
from app.auth import get_password_hash, verify_password, create_access_token, get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserRegister):
    # Check if user already exists
    existing_user = users_collection.find_one({"email": user_data.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    hashed_password = get_password_hash(user_data.password)
    
    new_user = {
        "name": user_data.name,
        "email": user_data.email,
        "password": hashed_password,
        "education": "",
        "skills": [],
        "experience_level": "",
        "preferred_job_role": ""
    }
    
    result = users_collection.insert_one(new_user)
    
    # Return user data with string ID
    return UserResponse(
        id=str(result.inserted_id),
        name=new_user["name"],
        email=new_user["email"],
        education=new_user["education"],
        skills=new_user["skills"],
        experience_level=new_user["experience_level"],
        preferred_job_role=new_user["preferred_job_role"]
    )

@router.post("/login", response_model=Token)
def login(credentials: UserLogin):
    user = users_collection.find_one({"email": credentials.email})
    if not user or not verify_password(credentials.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": str(user["_id"])})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
def get_me(current_user: dict = Depends(get_current_user)):
    return UserResponse(
        id=str(current_user["_id"]),
        name=current_user["name"],
        email=current_user["email"],
        education=current_user.get("education", ""),
        skills=current_user.get("skills", []),
        experience_level=current_user.get("experience_level", ""),
        preferred_job_role=current_user.get("preferred_job_role", "")
    )
