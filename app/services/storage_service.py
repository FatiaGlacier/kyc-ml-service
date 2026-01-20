from fastapi import UploadFile
from pathlib import Path
from typing import Tuple
import uuid
import shutil
import cv2
from app.services.video_processing import extract_frames
from app.app_config import VIDEOS_DIR_STR, FRAMES_DIR_STR

def save_video_tmp(file: UploadFile) -> Tuple[str, str]:
    session_id = f"session_{uuid.uuid4().hex}"
    video_name = f"{session_id}.mp4"
    file_path = VIDEOS_DIR_STR + "\\" + video_name
    
    print(file_path)

    with Path(file_path).open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(file_path), str(video_name)

def save_extracted_frames(video_name: str, frames: list) -> list[str]:
    core_name = Path(video_name).stem
    frames_dir = FRAMES_DIR_STR + "\\" + core_name
    Path(frames_dir).mkdir(parents=True, exist_ok=True)

    frames_names = []
    count = 0;

    for idx, frame in enumerate(frames):
        frame_name = f"{core_name}_{idx:03d}.jpg"
        frame_path = frames_dir + "\\" + frame_name
        cv2.imwrite(str(frame_path), frame)
        frames_names.append(frame_name)
        count+=1

    print("FRAMES COUNT: " + str(count))
    return frames_names

def save_frames(video_path: str) -> list[str]:
    frames = extract_frames(video_path)
    video_path = Path(video_path)
    core_name = Path(video_path).stem

    pathes = save_extracted_frames(core_name, frames)

    return pathes

def save_frames_name(video_name: str) -> list[str]:
    video_path = VIDEOS_DIR_STR + "\\" + video_name
    frames = extract_frames(video_path)
    core_name = Path(video_path).stem

    pathes = save_extracted_frames(core_name, frames)

    return pathes

def delete_video(video_name: str) -> str:
    video_path = VIDEOS_DIR_STR + "\\" + video_name
    path_obj = Path(video_path)

    if path_obj.exists() and path_obj.is_file():
        path_obj.unlink()
        return f"Deleted: {video_path}"
    else:
        return f"File not foun: {video_path}"
