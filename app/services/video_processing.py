import cv2

FRAME_SKIP = 50; #TODO config.env

def extract_frames(video_path) -> list:
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Can't open video: {video_path}")
        return
    
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

    return frames;


