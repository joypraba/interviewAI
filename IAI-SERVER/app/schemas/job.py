from pydantic import BaseModel
from typing import List

class JobCreate(BaseModel):
    title: str
    description: str
    startDate: str
    endDate: str
    skills: List[str]


class JobResponse(BaseModel):
    id: int
    title: str
    startDate: str
    endDate: str
    skills: List[str] = []
    
    class Config:
        from_attributes = True