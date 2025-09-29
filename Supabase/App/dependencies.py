from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from typing import Annotated
from app.database import supabase
from app.schemas.user import UserInDB, TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> UserInDB:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Verify token with Supabase
        user_data = supabase.auth.get_user(token)
        if not user_data:
            raise credentials_exception
            
        # Get additional user details from our database
        db_user = supabase.table("users")\
                       .select("*")\
                       .eq("id", user_data.user.id)\
                       .single()\
                       .execute()
                       
        if not db_user.data:
            raise credentials_exception
            
        return UserInDB(**db_user.data)
        
    except Exception as e:
        print(f"Authentication error: {str(e)}")
        raise credentials_exception
        
def get_current_active_user(
    current_user: Annotated[UserInDB, Depends(get_current_user)]
) -> UserInDB:
    if not current_user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User not verified"
        )
    return current_user
