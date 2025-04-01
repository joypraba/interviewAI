from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.job import Job
from app.schemas.job import JobCreate

async def createService(db: AsyncSession, job_data: JobCreate):
    job = Job(
        title= job_data.title,
        skills= job_data.skills,
        description= job_data.description,
        startDate= job_data.startDate,
        endDate= job_data.endDate
    )
    db.add(job)
    await db.commit()
    await db.refresh(job)
    return job

async def getOneService(db: AsyncSession, job_id: int):
    """ Get job by ID """
    result = await db.execute(select(Job).where(Job.id == job_id))
    return result.scalars().first()

async def getAllService(db: AsyncSession):
    """ Get all jobs """
    result = await db.execute(select(Job))
    return result.scalars().all()
