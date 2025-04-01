from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, CheckConstraint

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
    rating = Column(Integer, default=0)
    status = Column(String, 
                    CheckConstraint("status IN ('Pending', 'Rejected', 'Interview Inprogress', 'Interview Done')"),
                    default="Pending")

    # job = relationship("job", foreign_keys=[jobId], back_populates="jobs")
    # candidate = relationship("candidate", foreign_keys=[candidateId], back_populates="candidates")
