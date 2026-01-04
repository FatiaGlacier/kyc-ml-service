from fastapi import APIRouter, File, UploadFile

router = APIRouter(prefix="/video", tags=["Video"])

@router.post("/process-video")
async def process_video(video: UploadFile = File(...)):
    return {"message": "Servus!", "video_name" : video.filename}