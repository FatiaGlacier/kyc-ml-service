from pathlib import Path
from app.services.storage_service import extract_frames, save_extracted_frames
import os
from celery_app import app, VIDEOS_DIR

PATH = str(VIDEOS_DIR)

@app.task(name="save_frames_task")
def save_frames_task(video_name: str):
    video_path = PATH + "\\" + video_name
    print(video_path)
    frames = extract_frames(str(video_path))
    video_path = Path(video_path)
    core_name = Path(video_path).stem
    pathes = save_extracted_frames(core_name, frames)

