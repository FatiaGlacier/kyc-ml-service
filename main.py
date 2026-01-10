from fastapi import FastAPI
from app.api import video

app = FastAPI()

app.include_router(video.router)

@app.get("/")
def root():
    return {"message": "Servus! KYC Verification API"}