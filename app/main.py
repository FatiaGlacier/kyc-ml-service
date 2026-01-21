import app_config 
from fastapi import FastAPI
from app.api import video
from dotenv import load_dotenv

app = FastAPI()

app.include_router(video.router)

@app.get("/")
def root():
    return {"message": "Servus! KYC Verification API"}