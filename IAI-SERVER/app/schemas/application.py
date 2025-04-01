from pydantic import BaseModel

class ApplicationCreate(BaseModel):
    jobId: int
    candidateId: int

class ApplicationUpdate(BaseModel):
    status: str

class ApplicationResponse(BaseModel):
    id: int
    jobId: int
    candidateId: int
    status: str

    class Config:
        from_attributes = True