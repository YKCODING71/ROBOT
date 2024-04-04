import cv2
import numpy as np

def find_contours_in_white(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    return image

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture('testVideo.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 2. 양쪽 사이드를 제외한 중앙의 1/3 부분 추출
    height, width, _ = frame.shape
    roi_height = int(height / 3)
    roi_width = int(width / 3)
    roi = frame[2 * roi_height:height, roi_width:(width - roi_width)]

    # 흰색 영역의 윤곽선을 찾아 이미지에 표시
    result_frame = find_contours_in_white(roi)

    # 전체 이미지에 결과 적용
    frame[2 * roi_height:height, roi_width:(width - roi_width)] = result_frame[:, :]

    cv2.imshow('Contours in White', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
