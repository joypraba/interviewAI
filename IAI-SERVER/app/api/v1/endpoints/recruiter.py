from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.recruiter import Recruiter
from app.schemas.recruiter import RecruiterCreate, RecruiterResponse
from app.db.session import get_db
from app.services.recruiterService import createService, getOneService, getAllService, duplicateCheck

router = APIRouter()

# ✅ Create Recruiter
@router.post("/", response_model=RecruiterResponse)
async def create(recruiter: RecruiterCreate, db: AsyncSession = Depends(get_db)):
    try:
        if await duplicateCheck(db, recruiter.email):
            raise HTTPException(status_code=400, detail="Email already registered")

        print('after duplicate check')
        return await createService(db, recruiter)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# # ✅ Get All Recruiters
@router.get("/", response_model=list[RecruiterResponse])
async def getAll(db: AsyncSession = Depends(get_db)):
    try:
        return await getAllService(db)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# # ✅ Get Recruiter by ID
@router.get("/{recruiterId}", response_model=RecruiterResponse)
async def getOne(recruiterId: int, db: AsyncSession = Depends(get_db)):
    try:
        return await getOneService(db, recruiterId)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

