import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

app = Celery(
    "app.celery_app",
    broker=os.getenv("CELERY_BROCKER_URL"),
    backend=os.getenv("CELERY_RESULT_BACKEND"),
)