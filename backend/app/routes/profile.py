from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId
from app.database import users_collection
from app.models import ProfileUpdate, UserResponse
from app.auth import get_current_user

router = APIRouter(prefix="/profile", tags=["Profile"])

@router.get("", response_model=UserResponse)
def get_profile(current_user: dict = Depends(get_current_user)):
    return UserResponse(
        id=str(current_user["_id"]),
        name=current_user["name"],
        email=current_user["email"],
        education=current_user.get("education", ""),
        skills=current_user.get("skills", []),
        experience_level=current_user.get("experience_level", ""),
        preferred_job_role=current_user.get("preferred_job_role", "")
    )

@router.put("", response_model=UserResponse)
def update_profile(profile_data: ProfileUpdate, current_user: dict = Depends(get_current_user)):
    update_fields = {}
    
    if profile_data.name is not None:
        update_fields["name"] = profile_data.name
    if profile_data.education is not None:
        update_fields["education"] = profile_data.education
    if profile_data.skills is not None:
        update_fields["skills"] = profile_data.skills
    if profile_data.experience_level is not None:
        update_fields["experience_level"] = profile_data.experience_level
    if profile_data.preferred_job_role is not None:
        update_fields["preferred_job_role"] = profile_data.preferred_job_role
        
    if not update_fields:
        return UserResponse(
            id=str(current_user["_id"]),
            name=current_user["name"],
            email=current_user["email"],
            education=current_user.get("education", ""),
            skills=current_user.get("skills", []),
            experience_level=current_user.get("experience_level", ""),
            preferred_job_role=current_user.get("preferred_job_role", "")
        )
        
    users_collection.update_one(
        {"_id": current_user["_id"]},
        {"$set": update_fields}
    )
    
    updated_user = users_collection.find_one({"_id": current_user["_id"]})
    return UserResponse(
        id=str(updated_user["_id"]),
        name=updated_user["name"],
        email=updated_user["email"],
        education=updated_user.get("education", ""),
        skills=updated_user.get("skills", []),
        experience_level=updated_user.get("experience_level", ""),
        preferred_job_role=updated_user.get("preferred_job_role", "")
    )
