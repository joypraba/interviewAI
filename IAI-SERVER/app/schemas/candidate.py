from pydantic import BaseModel, EmailStr
from typing import List

class CandidateCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class CandidateResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    skills: List[str] = []
    phone: str
    experience: str
    education: str

    class Config:
        from_attributes = True