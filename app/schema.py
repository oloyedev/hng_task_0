from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


class UserProfile(BaseModel):
    email:EmailStr
    name:str
    stack:str

class ProfileResponse(BaseModel):
    status:str
    user:UserProfile
    timestamp:str
    fact:str


class SuccessResponse(BaseModel):
    status: str = "success"
    user: UserProfile
    timestamp: datetime
    fact: str

class ErrorResponse(BaseModel):
    status: str = "failed"
    user: UserProfile
    timestamp: datetime
    error: str


   