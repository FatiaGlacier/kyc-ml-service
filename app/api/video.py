from fastapi import APIRouter, File, UploadFile
from app.services.storage_service import save_upload_video

router = APIRouter(prefix="/video", tags=["Video"])

@router.post("/process-video")
async def process_video(video: UploadFile = File(...)):
    
    path = save_upload_video(video)

    return {"message": "Servus!", "video_name" : video.filename, "video_path" : path}