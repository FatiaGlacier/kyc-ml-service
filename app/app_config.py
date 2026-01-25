import os
from pathlib import Path
from dotenv import load_dotenv

env_file = os.getenv("ENV_FILE")
load_dotenv(env_file, override=True)

print(f"[CONFIG] Loading environment from: {env_file}")
print(f"[CONFIG] TEMP_DIR from env: {os.getenv('TEMP_DIR')}")

TEMP_DIR = Path(os.getenv("TEMP_DIR", "temp"))
VIDEOS_DIR = Path(os.getenv("VIDEOS_DIR"))
FRAMES_DIR = Path(os.getenv("FRAMES_DIR"))

VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
FRAMES_DIR.mkdir(parents=True, exist_ok=True)

VIDEOS_DIR_STR = str(VIDEOS_DIR)
FRAMES_DIR_STR = str(FRAMES_DIR)

print(f"[CONFIG] TEMP_DIR: {TEMP_DIR.absolute()}")
print(f"[CONFIG] VIDEOS_DIR: {VIDEOS_DIR.absolute()}")
print(f"[CONFIG] FRAMES_DIR: {FRAMES_DIR.absolute()}")