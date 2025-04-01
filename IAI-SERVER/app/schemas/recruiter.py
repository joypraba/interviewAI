from pydantic import BaseModel, EmailStr

class RecruiterCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class RecruiterResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True