import cv2

FRAME_SKIP = 50; #TODO config.env

def extract_frames(video_path: str) -> list:
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return []
    
    frames = []
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break

        if frame_count % FRAME_SKIP != 0:
            frame_count += 1
            continue
        
        frames.append(frame)
        frame_count += 1

    cap.release()
    return frames;


