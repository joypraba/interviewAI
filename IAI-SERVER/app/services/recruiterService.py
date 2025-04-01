from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.recruiter import Recruiter
from app.schemas.recruiter import RecruiterCreate
import bcrypt

def hash_password(password: str) -> str:
    """Hash the password using bcrypt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

async def createService(db: AsyncSession, recruiter_data: RecruiterCreate):
    """ Create a new recruiter """
    hashed_password = hash_password(recruiter_data.password)
    recruiter = Recruiter(
        name=recruiter_data.name,
        email=recruiter_data.email,
        password=hashed_password  # Store the hashed password
    )
    db.add(recruiter)
    await db.commit()
    await db.refresh(recruiter)
    return recruiter

async def getOneService(db: AsyncSession, recruiter_id: int):
    """ Get recruiter by ID """
    result = await db.execute(select(Recruiter).where(Recruiter.id == recruiter_id))
    return result.scalars().first()

async def getAllService(db: AsyncSession):
    """ Get all recruiters """
    result = await db.execute(select(Recruiter))
    return result.scalars().all()

async def duplicateCheck(db: AsyncSession, email: str):
    """ Get recruiter by Email """
    query = select(Recruiter).where(Recruiter.email == email)
    result = await db.execute(query)
    recruiter = result.scalars().first()  # ✅ Extract the result
    return recruiter
