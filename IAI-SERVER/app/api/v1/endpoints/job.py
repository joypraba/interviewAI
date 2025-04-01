from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.job import Job
from app.schemas.job import JobCreate, JobResponse
from app.db.session import get_db
from app.services.jobService import createService, getOneService, getAllService

router = APIRouter()

# ✅ Create Job
@router.post("/", response_model=JobResponse)
async def create(job: JobCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await createService(db, job)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# # ✅ Get All Jobs
@router.get("/", response_model=list[JobResponse])
async def getAll(db: AsyncSession = Depends(get_db)):
    try:
        return await getAllService(db)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# # ✅ Get Job by ID
@router.get("/{jobId}", response_model=JobResponse)
async def getOne(jobId: int, db: AsyncSession = Depends(get_db)):
    try:
        return await getOneService(db, jobId)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

