from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, auth
from app.config import settings

app = FastAPI(
    title="FLORENCE API",
    description="Backend services for the FLORENCE digital health platform",
    version="1.0.0",
    contact={
        "name": "FLORENCE Team",
        "email": "support@florence.health",
    },
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to the FLORENCE API",
        "docs": f"{settings.SUPABASE_URL}/docs",
    }
