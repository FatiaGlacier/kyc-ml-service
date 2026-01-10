from fastapi import APIRouter, File, UploadFile
from app.services.storage_service import save_upload_video, save_upload_video_and_frames

router = APIRouter(prefix="/video", tags=["Video"])

@router.post("/process-video")
async def process_video(video: UploadFile = File(...)):
    
    path = save_upload_video(video)

    #1 Liveness check

    # Response

    #2 Saving farmes CELERY

    return {"message": "Servus!", "video_name" : video.filename, "video_path" : path}

@router.post("/process-video-and-save-frames")
async def process_video_and_save_frames(video: UploadFile = File(...)):
    pathes, msg = save_upload_video_and_frames(video)

    return {"message": "Servus!", "video_pathes" : pathes, "video_deleted: " : msg}