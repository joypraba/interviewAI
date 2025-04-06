from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey, CheckConstraint

from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime
from sqlalchemy.dialects.postgresql import ARRAY, JSONB  

class Application(Base):
    __tablename__ = "applications"
    
    id = Column(Integer, primary_key=True, index=True)
    jobId = Column(Integer, ForeignKey("jobs.id"))
    candidateId = Column(Integer, ForeignKey("candidates.id"))
    qa = Column(JSONB, default=[])
    rating = Column(Float, default=0)
    status = Column(String, 
                    CheckConstraint("status IN ('Pending', 'Rejected', 'Interview Inprogress', 'Interview Done')"),
                    default="Pending")

    candidate = relationship("Candidate", back_populates="applications")
    job = relationship("Job", back_populates="applications")
