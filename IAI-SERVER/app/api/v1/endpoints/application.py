from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.application import Application
from app.schemas.application import ApplicationCreate, ApplicationResponse, ApplicationUpdate, ApplicationMockInterview, ApplicationMockInterviewSubmit
from app.db.session import get_db
from app.services.applicationService import createService, getOneService, getAllService, updateService, mockInterviewService, mockInterviewSubmitService

router = APIRouter()

# ✅ Create Application
@router.post("/", response_model=ApplicationResponse)
async def create(application: ApplicationCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await createService(db, application)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# # ✅ Get All Applications
@router.get("/")
async def getAll(db: AsyncSession = Depends(get_db)):
    try:
        data = await getAllService(db)
        print(data)
        return await getAllService(db)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# # ✅ Get Application by ID
@router.get("/{applicationId}", response_model=ApplicationResponse)
async def getOne(applicationId: int, db: AsyncSession = Depends(get_db)):
    try:
        return await getOneService(db, applicationId)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# # ✅ update Application by ID
@router.put("/{applicationId}", response_model=ApplicationResponse)
async def update(applicationId: int, application: ApplicationUpdate, db: AsyncSession = Depends(get_db)):
    try:
        return await updateService(db, applicationId, application)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# # ✅ Get Application by ID
@router.get("/mockInterview/{applicationId}", response_model=ApplicationMockInterview)
async def mockInterview(applicationId: int, db: AsyncSession = Depends(get_db)):
    try:
        return await mockInterviewService(db, applicationId)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# # ✅ Get Application by ID
@router.put("/mockInterviewSubmit/{applicationId}", response_model=ApplicationMockInterview)
async def mockInterview(applicationId: int, data: ApplicationMockInterviewSubmit, db: AsyncSession = Depends(get_db)):
    try:
        return await mockInterviewSubmitService(db, applicationId, data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

