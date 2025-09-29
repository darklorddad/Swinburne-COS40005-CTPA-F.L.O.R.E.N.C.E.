# main.py

import os
from fastapi import FastAPI, Depends, HTTPException, Header
from supabase import create_client, Client
from gotrue.errors import AuthApiError
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Initialize Supabase client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# --- Pydantic Models for Data Validation ---
# These models ensure the data sent to your API has the correct shape and types.

class DailyLogCreate(BaseModel):
    log_date: str # e.g., "2023-10-27"
    meal_time: str # e.g., "BREAKFAST_AFTER"
    diet_log: Optional[str] = None
    glucose_value: Optional[float] = None

class PatientProfileResponse(BaseModel):
    id: int
    user_id: str
    name: Optional[str]
    # Add other fields you want to return to the user

