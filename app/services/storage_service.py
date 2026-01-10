from fastapi import UploadFile
from pathlib import Path
import uuid
import shutil
import random

TEMP_VIDEO_DIR = Path("D:\\Projects\\Online-banking-system\\kyc-ml-service\\temp\\videos")
TEMP_FRAMES_DIR = Path("D:\\Projects\\Online-banking-system\\kyc-ml-service\\temp\\frames")
TEMP_VIDEO_DIR.mkdir(parents=True, exist_ok=True)
TEMP_FRAMES_DIR.mkdir(parents=True, exist_ok=True)

def save_upload_video(file: UploadFile) -> str:
    session_id = f"session_{uuid.uuid4().hex}"
    file_path = TEMP_VIDEO_DIR / f"{session_id}.mp4"
        
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path
