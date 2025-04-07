from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.recruiter import Recruiter
from app.models.candidate import Candidate
from passlib.context import CryptContext
from datetime import timedelta, datetime
from jose import jwt

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT config
SECRET_KEY = "Test123!"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Sign In Service
async def signInService(db: AsyncSession, data: dict):
    email = data.get("email")
    password = data.get("password")
    user_type = data.get("type")

    if not email or not password:
        raise Exception("Email and password are required")

    if user_type == '1':  # Recruiter
        result = await db.execute(select(Recruiter).where(Recruiter.email == email))
    elif user_type == '2':  # Candidate
        result = await db.execute(select(Candidate).where(Candidate.email == email))
    else:
        raise Exception("Invalid user type")

    user = result.scalars().first()
    if not user or not verify_password(password, user.password):
        raise Exception("Invalid email or password")

    # Generate JWT token
    access_token = create_access_token(
        data={"userId": user.id, "email": email, "name": user.name, "type": user_type},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "user_type": user_type
    }


# Helper: Verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# Helper: Hash password (for signup or reset)
def get_password_hash(password):
    return pwd_context.hash(password)


# Helper: Create JWT Token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
