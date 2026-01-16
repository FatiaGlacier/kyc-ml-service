from fastapi import UploadFile
from pathlib import Path
from typing import Tuple
import uuid
import shutil
import cv2
from app.services.video_processing import extract_frames

TEMP_VIDEO_DIR = Path("D:\\Projects\\Online-banking-system\\kyc-ml-service\\temp\\videos")
TEMP_FRAMES_DIR = Path("D:\\Projects\\Online-banking-system\\kyc-ml-service\\temp\\frames")
TEMP_VIDEO_DIR.mkdir(parents=True, exist_ok=True)
TEMP_FRAMES_DIR.mkdir(parents=True, exist_ok=True)

def save_video_tmp(file: UploadFile) -> Tuple[str, str]:
    session_id = f"session_{uuid.uuid4().hex}"
    video_name = f"{session_id}.mp4"
    file_path = TEMP_VIDEO_DIR / video_name
        
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(file_path), video_name

def save_extracted_frames(video_name: str, frames: list) -> list[str]:
    core_name = Path(video_name).stem
    frames_dir = TEMP_FRAMES_DIR / f"{core_name}"
    frames_dir.mkdir(parents=True, exist_ok=True)

    frames_names = []

    for idx, frame in enumerate(frames):
        frame_name = f"{core_name}_{idx:03d}.jpg"
        frame_path = frames_dir / frame_name
        cv2.imwrite(str(frame_path), frame)
        frames_names.append(frame_name)

    return frames_names

def save_frames(video_path: str) -> list[str]:
    frames = extract_frames(video_path)
    video_path = Path(video_path)
    core_name = Path(video_path).stem

    pathes = save_extracted_frames(core_name, frames)

    return pathes

def delete_video(video_name: str) -> str:
    video_path = TEMP_VIDEO_DIR / video_name

    if video_path.exists() and video_path.is_file():
        video_path.unlink()
        return f"Deleted: {video_path}"
    else:
        return f"File not foun: {video_path}"
