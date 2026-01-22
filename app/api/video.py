from fastapi import APIRouter, File, UploadFile
from app.services.storage_service import  save_video_tmp, save_frames,  delete_video, save_frames_name
from ...celery.tasks import save_frames_task

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

@router.post("/process-video-name")
async def process_video(video: UploadFile = File(...)):
    
    video_path, video_name = save_video_tmp(video)

    #1 Liveness check

    # Response

    #2 Saving farmes CELERY

    frame_pathes = save_frames_name(video_name)

    msg = delete_video(video_name)

    return {"message": "Servus!", "video_name" : video_name, "frames" : frame_pathes}#, "delete_msg" : msg}

@router.post("/process-video-celery")
def process_video_celery(video: UploadFile = File(...)):
    
    video_path, video_name = save_video_tmp(video)

    #1 Liveness check

    # Response

    #2 Saving farmes CELERY

    task = save_frames_task.delay(video_name)
    task.get()
    msg = delete_video(video_name)

    return {"message": "Servus!", "video_name" : video_name, "id" : task.id}