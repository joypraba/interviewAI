from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.application import Application
from app.models.job import Job
from app.models.candidate import Candidate
from app.schemas.application import ApplicationCreate, ApplicationUpdate
from sqlalchemy import update
from openai import OpenAI
client = OpenAI(api_key="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")
async def createService(db: AsyncSession, application_data: ApplicationCreate):
    application = Application(
        jobId= application_data.jobId,
        candidateId= application_data.candidateId,
    )
    db.add(application)
    await db.commit()
    await db.refresh(application)
    return application

async def getOneService(db: AsyncSession, application_id: int):
    """ Get application by ID """
    result = await db.execute(select(Application).where(Application.id == application_id))
    return result.scalars().first()

async def updateService(db: AsyncSession, application_id: int, application_data: ApplicationUpdate):

    # Update the application status
    await db.execute(
        update(Application)
        .where(Application.id == application_id)
        .values(**application_data.dict())  # Convert Pydantic model to dictionary
    )
    await db.commit()

    # Fetch and return the updated record
    result = await db.execute(select(Application).where(Application.id == application_id))
    return result.scalars().first()

async def getAllService(db: AsyncSession):
    """ Get all applications """
    result = await db.execute(select(Application))
    return result.scalars().all()


async def mockInterviewService(db: AsyncSession, application_id: int):
    """ Get all applications """
    application_result = await db.execute(select(Application).where(Application.id == application_id))
    application = application_result.scalars().first()

    if application:  # Ensure application exists before querying related data
        job_result = await db.execute(select(Job).where(Job.id == application.jobId))
        job = job_result.scalars().first()

        candidate_result = await db.execute(select(Candidate).where(Candidate.id == application.candidateId))
        candidate = candidate_result.scalars().first()

        return await generate_questions(job.description, candidate.resumeExtractTxt)
   
    return []


def generate_questions(job_description, resume_content):
    """Generates five interview questions based on job description and resume."""
    prompt = f"""
    Given the following job description and candidate resume, generate 5 interview questions that test the candidate's relevant skills.

    Job Description:
    {job_description}

    Resume Content:
    {resume_content}

    Questions:
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an AI interviewer."}, 
                  {"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

