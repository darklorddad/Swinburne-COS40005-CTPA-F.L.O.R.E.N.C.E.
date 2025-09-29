from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from app.database import supabase
from app.schemas.user import UserInDB, UserCreate, LoginRequest, Token
from app.dependencies import get_current_user, get_current_active_user

router = APIRouter(prefix="/users", tags=["Users"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.post("/register", response_model=UserInDB, status_code=status.HTTP_201_CREATED)
async def register_user(user_create: UserCreate):
    """Register a new user (patient or clinician)"""
    try:
        # Create auth user
        auth_response = supabase.auth.sign_up({
            "email": user_create.email,
            "password": user_create.password,
            "options": {
                "data": {
                    "name": user_create.name,
                    "role": user_create.role.value,
                    "is_verified": False
                }
            }
        })
        
        # Create database user record
        db_user = supabase.table("users").insert({
            "email": user_create.email,
            "role": user_create.role.value,
            "is_verified": False,
            "name": user_create.name
        }).execute()
        
        return UserInDB(**db_user.data[0])
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/login", response_model=Token)
async def login_for_access_token(login_data: LoginRequest):
    """Authenticate and return JWT token"""
    try:
        response = supabase.auth.sign_in_with_password({
            "email": login_data.email,
            "password": login_data.password
        })
        return Token(
            access_token=response.session.access_token,
            token_type="bearer"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.get("/me", response_model=UserInDB)
async def read_current_user(
    current_user: Annotated[UserInDB, Depends(get_current_active_user)]
):
    """Get current authenticated user's profile"""
    return current_user
