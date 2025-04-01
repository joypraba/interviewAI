from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime
from sqlalchemy.dialects.postgresql import ARRAY

class Candidate(Base):
    __tablename__ = "candidates"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    skills = Column(ARRAY(String), default=[])
    resumePath = Column(String, default="")
    resumeExtractTxt = Column(String, default="")
    phone = Column(String, default="")
    experience = Column(String, default="")
    education = Column(String, default="")
    status = Column(Boolean, default=True)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow)
