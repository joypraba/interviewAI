from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey

from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime
from sqlalchemy.dialects.postgresql import ARRAY

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    skills = Column(ARRAY(String))
    description = Column(String)
    startDate = Column(String)
    endDate = Column(String)
    status = Column(Boolean, default=True)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow)
    createdBy = Column(Integer, ForeignKey("recruiters.id"))
    updatedBy = Column(Integer, ForeignKey("recruiters.id"))


    applications = relationship("Application", back_populates="job")
