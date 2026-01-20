from fastapi import FastAPI
from app.api import video
from dotenv import load_dotenv
import app.app_config 

app = FastAPI()

app.include_router(video.router)

@app.get("/")
def root():
    return {"message": "Servus! KYC Verification API"}