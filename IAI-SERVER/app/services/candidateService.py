from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate
import bcrypt

def hash_password(password: str) -> str:
    """Hash the password using bcrypt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

async def createService(db: AsyncSession, candidate_data: CandidateCreate):
    """ Create a new candidate """
    hashed_password = hash_password(candidate_data["password"])
    candidate = Candidate(
        name=candidate_data["name"],
        email=candidate_data["email"],
        password=hashed_password,
        skills=candidate_data["skills"],
        resumePath=candidate_data["resumePath"],
        resumeExtractTxt=candidate_data["resumeExtractTxt"],
        phone=candidate_data["phone"],
        experience=candidate_data["experience"],
        education=candidate_data["education"],
    )
    db.add(candidate)
    await db.commit()
    await db.refresh(candidate)
    return candidate

async def getOneService(db: AsyncSession, candidate_id: int):
    """ Get candidate by ID """
    result = await db.execute(select(Candidate).where(Candidate.id == candidate_id))
    return result.scalars().first()

async def getAllService(db: AsyncSession):
    """ Get all candidates """
    result = await db.execute(select(Candidate))
    return result.scalars().all()

async def duplicateCheck(db: AsyncSession, email: str):
    """ Get candidate by Email """
    query = select(Candidate).where(Candidate.email == email)
    result = await db.execute(query)
    candidate = result.scalars().first()  # ✅ Extract the result
    return candidate
