from fastapi import FastAPI
from app.db.session import init_db
from contextlib import asynccontextmanager
from app.api.v1.endpoints import recruiter
from app.api.v1.endpoints import candidate
from app.api.v1.endpoints import application
from app.api.v1.endpoints import job
import socket
import os
print(socket.getaddrinfo("127.0.0.1", 5432))
UPLOAD_DIR = "uploads/resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()  # Initialize database on startup
    yield  # Continue running the app

app = FastAPI(lifespan=lifespan)

app.include_router(recruiter.router, prefix="/recruiters", tags=["Recruiters"])
app.include_router(candidate.router, prefix="/candidates", tags=["Candidates"])
app.include_router(job.router, prefix="/jobs", tags=["Jobs"])
app.include_router(application.router, prefix="/applications", tags=["Applications"])
