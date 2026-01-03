from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Servus!"}

@app.post("/send-video/")
async def process_video(video: UploadFile = File(...)):
    return {"message": "Servus!", "video_name" : video.filename}
