from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.services.authService import signInService

router = APIRouter()

# ✅ Create Job
@router.post("/signin")
async def signIn(request: Request, db: AsyncSession = Depends(get_db)):
    try:
        data = await request.json()
        return await signInService(db, data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))