import cv2
import mediapipe as mp
import numpy as np

def get_distance(ax, ay, bx, by):
    a = np.array([ax, ay])
    b = np.array([bx, by])

    distance = np.sqrt(np.sum(np.square(a - b)))      
    # 최소 거리 갱신   
    distance = 0 if distance < 10 else distance
    return distance

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# 이미지 한편에 넣을 슬라이드 바 세팅값
bar_x, bar_y, bar_width, bar_height = 500, 50, 20, 255
bar_max_color = (0, 255, 0)
max_distance = 200
led_bright_max = 255

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

        distance = get_distance(thumb_x, thumb_y, index_x, index_y)
        #print(distance)
    
        # 거리를 LED 밝기로 변환하기
        led_brightness = int((distance / max_distance) * led_bright_max)
        bar_color = tuple(np.multiply(bar_max_color, led_brightness / led_bright_max).astype(int))

        # 밝기 수치를 슬라이드 바로 시각화 하기  
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_width, bar_y + bar_height), (255, 255, 255), -1)  # Clear the rectangle
        cv2.rectangle(frame, (bar_x, bar_y + bar_height - led_brightness), (bar_x + bar_width, bar_y + bar_height), tuple(map(int, bar_color)), -1)  # Fill the rectangle

        # 엄지와 검지에 그린 동그라미 표시하기
        cv2.circle(frame, (thumb_x, thumb_y), 5, (0, 255, 0), -1)  #  
        cv2.circle(frame, (index_x, index_y), 5, (0, 255, 0), -1)  #  

    cv2.imshow('Hand Landmarks', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()