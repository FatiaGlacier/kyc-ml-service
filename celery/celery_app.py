import os
from celery import Celery
from pathlib import Path
from dotenv import load_dotenv

print(f"[CONFIG] Loading environment from: {os.getenv("ENV_FILE")}")
print(f"[CONFIG] TEMP_DIR from env: {os.getenv('TEMP_DIR')}")
print(f"[CONFIG] VIDEOS_DIR from env: {os.getenv("VIDEOS_DIR")}")
print(f"[CONFIG] FRAMES_DIR from env: {os.getenv("FRAMES_DIR")}")

VIDEOS_DIR = str(os.getenv("VIDEOS_DIR"))

app = Celery(
    "app.celery_app",
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_RESULT_BACKEND"),
)

app.autodiscover_tasks(['app.tasks'])