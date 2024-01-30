import cv2
import mediapipe as mp
import numpy as np

def get_distance(ax, ay, bx, by):
    a = np.array([ax, ay])
    b = np.array([bx, by])

    # 두 점 사이의 거리 계산
    distance = np.sqrt(np.sum(np.square(a - b)))      
    # 최소 거리 갱신   
    distance = 0 if distance < 10 else distance
    return distance

# Mediapipe Hands 모듈 초기화
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# 이미지 한편에 넣을 슬라이드 바의 위치 및 크기 설정
bar_x, bar_y, bar_width, bar_height = 500, 50, 20, 255
bar_max_color = (0, 255, 0)
max_distance = 200
led_bright_max = 255

# 웹캠 열기
cap = cv2.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 손 인식 수행
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

        img_height, img_width, _ = frame.shape
        thumb_x, thumb_y = int(thumb_tip.x * img_width), int(thumb_tip.y * img_height)
        index_x, index_y = int(index_tip.x * img_width), int(index_tip.y * img_height)

        # 엄지와 검지 사이의 거리 계산
        distance = get_distance(thumb_x, thumb_y, index_x, index_y)
    
        # 거리를 LED 밝기로 변환하기
        led_brightness = int((distance / max_distance) * led_bright_max)
        bar_color = tuple(np.multiply(bar_max_color, led_brightness / led_bright_max).astype(int))

        # 밝기 수치를 슬라이드 바로 시각화하기  
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_width, bar_y + bar_height), (255, 255, 255), -1)  # 직사각형 지우기
        cv2.rectangle(frame, (bar_x, bar_y + bar_height - led_brightness), (bar_x + bar_width, bar_y + bar_height), tuple(map(int, bar_color)), -1)  # 직사각형 채우기

        # 엄지와 검지에 동그라미 그리기
        cv2.circle(frame, (thumb_x, thumb_y), 5, (0, 255, 0), -1)  # 엄지 동그라미 그리기
        cv2.circle(frame, (index_x, index_y), 5, (0, 255, 0), -1)  # 검지 동그라미 그리기

    # 화면에 손 랜드마크 표시
    cv2.imshow('Hand Landmarks', frame)

    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠 해제 및 모든 OpenCV 창 닫기
cap.release()
cv2.destroyAllWindows()
