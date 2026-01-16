from fastapi import APIRouter, File, UploadFile
from app.services.storage_service import  save_video_tmp, save_frames,  delete_video
from celery.result import AsyncResult

router = APIRouter(prefix="/video", tags=["Video"])

@router.post("/process-video")
async def process_video(video: UploadFile = File(...)):
    
    video_path, video_name = save_video_tmp(video)

    #1 Liveness check

    # Response

    #2 Saving farmes CELERY

    frame_pathes = save_frames(video_path)

    msg = delete_video(video_name)

    return {"message": "Servus!", "video_name" : video_name, "frames" : frame_pathes, "delete_msg" : msg}