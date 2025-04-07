from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app.models.application import Application
from app.models.job import Job
from app.models.candidate import Candidate
from app.schemas.application import ApplicationCreate, ApplicationUpdate
from sqlalchemy import update
import json
import openai
client = openai.AsyncOpenAI(api_key="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")
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
    result = await db.execute(select(Application).options(
            selectinload(Application.candidate),
            selectinload(Application.job)
        ))
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
        questions = json.loads(await generate_questions(job.description, candidate.resumeExtractTxt))

        return {"questions": questions}
   
    return {"questions": []}


async def generate_questions(job_description, resume_content):
    """Generates five interview questions based on job description and resume."""
    prompt = f"""
        Given the following job description and candidate resume, generate 5 interview questions that test the candidate's relevant skills.

        Return the result as a **valid JSON array of strings only**, without any extra formatting like markdown or code blocks.

        Job Description:
        {job_description}

        Resume Content:
        {resume_content}

        Questions:
        """


    response = await client.chat.completions.create(
        model="gpt-4o-mini",  # "gpt-4o-mini" does not exist; use "gpt-4o" or a valid model name
        messages=[
            {"role": "system", "content": "You are an AI interviewer."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content


async def mockInterviewSubmitService(db: AsyncSession, application_id: int, data):
    qa_text = "\n".join(
        [f"{i+1}. Q: {item.question}\n   A: {item.answers}" for i, item in enumerate(data.qa)]
    )

    prompt = f"""
        Evaluate the overall quality of the following interview responses on a scale of 0 to 10 based on clarity, relevance, and depth. 

        Only return the final average rating as a number.

        Data:
        {qa_text}
        """
    response = await client.chat.completions.create(
        model="gpt-4o-mini",  # "gpt-4o-mini" does not exist; use "gpt-4o" or a valid model name
        messages=[
            {"role": "system", "content": "You are an AI interview evaluator."},
            {"role": "user", "content": prompt}
        ]
    )
    rating = response.choices[0].message.content

    await db.execute(
        update(Application)
        .where(Application.id == application_id)
        .values(
            rating=float(rating),
            qa=[item.dict() for item in data.qa]
        )  # Convert Pydantic model to dictionary
    )
    await db.commit()

    return {"msg": "Successfully Submitted"}


