
import cv2
import numpy as np

# 웹캠을 엽니다.
cap = cv2.VideoCapture(0)

while True:
    # 프레임을 읽어옵니다.
    ret, frame = cap.read()

    # BGR 색상 공간을 HSV로 변환합니다.
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 빨간색의 범위를 정의합니다.
    lower_red = np.array([0,50,50])
    upper_red = np.array([0,75,255])

    # 정의한 범위 내의 픽셀을 찾습니다.
    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)

    # 빨간색 픽셀에 해당하는 부분만 추출합니다.
    red_objects = cv2.bitwise_and(frame, frame, mask=red_mask)

    # 결과 프레임을 출력합니다.
    cv2.imshow('Red Objects Tracking', red_objects)
    cv2.imshow('mask', red_mask)
    cv2.imshow('hsv', hsv_frame)

    # 'q' 키를 누르면 루프를 종료합니다.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠을 해제하고 창을 닫습니다.
cap.release()
cv2.destroyAllWindows()