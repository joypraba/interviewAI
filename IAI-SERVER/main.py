from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import init_db
from contextlib import asynccontextmanager
from app.api.v1.endpoints import recruiter
from app.api.v1.endpoints import candidate
from app.api.v1.endpoints import application
from app.api.v1.endpoints import job
from app.api.v1.endpoints import auth
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

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Or use ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],              # Allow all HTTP methods
    allow_headers=["*"],              # Allow all headers
)

app.include_router(recruiter.router, prefix="/recruiters", tags=["Recruiters"])
app.include_router(candidate.router, prefix="/candidates", tags=["Candidates"])
app.include_router(job.router, prefix="/jobs", tags=["Jobs"])
app.include_router(application.router, prefix="/applications", tags=["Applications"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
