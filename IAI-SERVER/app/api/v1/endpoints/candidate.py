from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate, CandidateResponse
from app.db.session import get_db
from typing import Optional
import json
from app.services.candidateService import createService, getOneService, getAllService, duplicateCheck
from app.services.resumeParserService import parseResume

UPLOAD_DIR = "uploads/resumes"
router = APIRouter()

# ✅ Create Candidate
@router.post("/", response_model=CandidateResponse)
async def create(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    skills: Optional[str] = Form(None),  # Optional JSON string
    resume: Optional[UploadFile] = File(None),  # Optional file
    db: AsyncSession = Depends(get_db),
):
    try:
        if await duplicateCheck(db, email):
            raise HTTPException(status_code=400, detail="Email already registered")
        
        skills_list = None
        if skills:
            try:
                skills_list = json.loads(skills)
                if not isinstance(skills_list, list):
                    raise ValueError("Skills must be a list")
            except json.JSONDecodeError:
                raise HTTPException(status_code=400, detail="Invalid skills format")
            
        resumeExtractTxt, parsed_data, resumePath = None, {}, None
        if resume:
            resumeExtractTxt, parsed_data, resumePath = await parseResume(resume, UPLOAD_DIR)

         # ✅ Set name from form or parsed resume
        candidate_name = name or parsed_data.get("Name")

        # ✅ Create candidate object
        candidate_data = {
            "name": candidate_name,
            "email": email,
            "password": password,
            "skills": skills_list or parsed_data.get("Skills", []),
            "resumeExtractTxt": resumeExtractTxt,
            "resumePath": resumePath,
            "phone": parsed_data.get("Phones")[0] if parsed_data.get("Phones") and len(parsed_data.get("Phones")) > 0 else "",
            "experience": parsed_data.get("Experience") if parsed_data else "",
            "education": parsed_data.get("Education") if parsed_data else "",
        }
        return await createService(db, candidate_data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# # ✅ Get All Candidates
@router.get("/", response_model=list[CandidateResponse])
async def getAll(db: AsyncSession = Depends(get_db)):
    try:
        return await getAllService(db)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# # ✅ Get Candidate by ID
@router.get("/{candidateId}", response_model=CandidateResponse)
async def getOne(candidateId: int, db: AsyncSession = Depends(get_db)):
    try:
        return await getOneService(db, candidateId)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

