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
supabase: Client = create_client("https://oproybafrxjwwvsfeoyc.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9wcm95YmFmcnhqd3d2c2Zlb3ljIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1ODU3Mzg2MCwiZXhwIjoyMDc0MTQ5ODYwfQ.zDOjQ04fAewagzJTCoumpJBWMCtNCr9F5vvozPV6hGo")

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

