from pydantic import BaseModel
from typing import List

class ApplicationCreate(BaseModel):
    jobId: int
    candidateId: int

class ApplicationUpdate(BaseModel):
    status: str


class ApplicationMockInterview(BaseModel):
    questions: List[str] = []
    msg: str

class QAItem(BaseModel):
    question: str
    answers: str

class ApplicationMockInterviewSubmit(BaseModel):
    qa: List[QAItem]

class ApplicationResponse(BaseModel):
    id: int
    jobId: int
    candidateId: int
    status: str
    # candidate: List[str]
    # job: List[str]
    

    class Config:
        from_attributes = True