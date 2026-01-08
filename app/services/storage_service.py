from fastapi import UploadFile
from pathlib import Path

TEMP_VIDEO_DIR = Path("D:\\Projects\\Online-banking-system\\kyc-ml-service\\temp\\videos")
TEMP_VIDEO_DIR.mkdir(parents=True, exist_ok=True)

def save_upload_video(file: UploadFile) -> str:
    file_path = TEMP_VIDEO_DIR / file.filename
        
    with file_path.open("wb") as buffer:
        buffer.write(file.file.read())

        return str(file_path)
