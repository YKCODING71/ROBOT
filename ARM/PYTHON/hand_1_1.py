import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

        img_height, img_width, _ = frame.shape
        thumb_x, thumb_y = int(thumb_tip.x * img_width), int(thumb_tip.y * img_height)
        index_x, index_y = int(index_tip.x * img_width), int(index_tip.y * img_height)

  
        cv2.circle(frame, (thumb_x, thumb_y), 5, (0, 255, 0), -1)  # 엄지 동그라미 그리기
        cv2.circle(frame, (index_x, index_y), 5, (0, 255, 0), -1)  # 검지 동그라미 그리기

    cv2.imshow('Hand Landmarks', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
