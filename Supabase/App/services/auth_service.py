from app.database import supabase
from app.schemas.user import UserCreate, UserInDB, UserRole
from datetime import datetime
from typing import Optional

async def register_new_user(user_data: UserCreate) -> UserInDB:
    """
    Registers a new user with proper role-based profile creation.
    Includes validation checks for clinician registration.
    """
    if user_data.role == UserRole.CLINICIAN and not user_data.organisation_id:
        raise ValueError("Clinicians must specify an organisation_id")

    # Create auth user
    auth_response = supabase.auth.sign_up({
        "email": user_data.email,
        "password": user_data.password,
        "options": {
            "data": {
                "name": user_data.name,
                "role": user_data.role.value,
                "is_verified": False
            }
        }
    })

    if not auth_response.user:
        raise RuntimeError("Failed to create auth user")

    # Create corresponding user record
    user_record = {
        "email": user_data.email,
        "role": user_data.role.value,
        "is_verified": False,
        "name": user_data.name,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }

    result = supabase.table("users").insert(user_record).execute()
    if not result.data:
        # Clean up auth user if DB insert fails
        supabase.auth.admin.delete_user(auth_response.user.id)
        raise RuntimeError("Failed to create user record")
    
    return UserInDB(**result.data[0])


async def authenticate_user(email: str, password: str) -> Optional[UserInDB]:
    """
    Authenticates a user and returns their full profile if successful.
    """
    try:
        # Verify credentials with Supabase auth
        auth_response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        # Get full user profile
        result = supabase.table("users") \
            .select("*") \
            .eq("email", email) \
            .single() \
            .execute()

        if result.data:
            return UserInDB(**result.data)
            
    except Exception:
        return None
