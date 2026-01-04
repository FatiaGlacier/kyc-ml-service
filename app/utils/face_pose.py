import numpy as np

# Пороги для pose (положення обличчя)
MAX_PITCH = 20#15  # ±15° вгору/вниз (менше = строгіше)
MAX_YAW = 20#20  # ±20° вліво/вправо
MAX_ROLL = 20#15  # ±15° нахил голови

def calculate_face_size_score(face_box, frame_width, frame_height):
    x, y, w, h = face_box
    face_area = w * h
    frame_area = frame_width * frame_height

    # Відносний розмір обличчя (0-1)
    relative_size = face_area / frame_area

    # Оптимально коли обличчя займає 10-40% кадру
    if relative_size < 0.05:
        return relative_size / 0.05 * 0.5  # Дуже маленьке
    elif relative_size <= 0.4:
        return 0.5 + (relative_size - 0.05) / 0.35 * 0.5  # Оптимальний розмір
    else:
        return 1.0 - (relative_size - 0.4) / 0.6 * 0.3  # Занадто велике


def calculate_face_position_score(face_box, frame_width, frame_height):
    x, y, w, h = face_box

    face_center_x = x + w / 2
    face_center_y = y + h / 2

    frame_center_x = frame_width / 2
    frame_center_y = frame_height / 2

    # Відстань від центру (нормалізована)
    distance_x = abs(face_center_x - frame_center_x) / (frame_width / 2)
    distance_y = abs(face_center_y - frame_center_y) / (frame_height / 2)

    # Комбінована відстань (0 = центр, 1 = край)
    distance = (distance_x + distance_y) / 2

    # Інвертуємо: центр = 1.0, край = 0.0
    return 1.0 - distance


def calculate_head_pose(keypoints):
    left_eye = np.array(keypoints['left_eye'])
    right_eye = np.array(keypoints['right_eye'])
    nose = np.array(keypoints['nose'])
    mouth_left = np.array(keypoints['mouth_left'])
    mouth_right = np.array(keypoints['mouth_right'])

    # 1. ROLL (нахил голови) - з кута між очима
    dY = right_eye[1] - left_eye[1]
    dX = right_eye[0] - left_eye[0]
    roll = np.degrees(np.arctan2(dY, dX))

    # 2. YAW (поворот вліво/вправо) - з позиції носа відносно очей
    eye_center = (left_eye + right_eye) / 2
    eye_width = np.linalg.norm(right_eye - left_eye)

    # Відстань носа від лінії між очима
    nose_to_eye_center = nose - eye_center

    # Проекція на горизонтальну вісь
    eye_direction = (right_eye - left_eye) / eye_width
    nose_offset = np.dot(nose_to_eye_center, eye_direction)

    # Конвертуємо в градуси (0 = по центру, + = вправо, - = вліво)
    yaw = nose_offset * 2  # Емпіричний коефіцієнт

    # 3. PITCH (нахил вгору/вниз) - з позиції носа по вертикалі
    mouth_center = (mouth_left + mouth_right) / 2

    # Відстань від очей до рота (висота обличчя)
    face_height = np.linalg.norm(mouth_center - eye_center)

    # Вертикальна позиція носа відносно очей
    nose_y_offset = nose[1] - eye_center[1]

    # Нормалізуємо по висоті обличчя
    nose_y_ratio = nose_y_offset / face_height if face_height > 0 else 0

    # Конвертуємо в градуси (- = вгору, + = вниз)
    # Нормальна позиція носа ~0.3 від очей до рота
    pitch = (nose_y_ratio - 0.3) * 60  # Емпіричний коефіцієнт

    return pitch, yaw, roll


def is_frontal_face(keypoints, pitch_threshold=MAX_PITCH,
                    yaw_threshold=MAX_YAW, roll_threshold=MAX_ROLL):
    pitch, yaw, roll = calculate_head_pose(keypoints)

    is_frontal = (
            abs(pitch) <= pitch_threshold and
            abs(yaw) <= yaw_threshold and
            abs(roll) <= roll_threshold
    )

    return is_frontal, pitch, yaw, roll


def calculate_pose_score(pitch, yaw, roll):
    # Кожна вісь окремо
    pitch_score = max(0, 1.0 - abs(pitch) / 30)  # 0° = 1.0, 30° = 0.0
    yaw_score = max(0, 1.0 - abs(yaw) / 40)
    roll_score = max(0, 1.0 - abs(roll) / 30)

    # Середнє
    pose_score = (pitch_score + yaw_score + roll_score) / 3

    return pose_score