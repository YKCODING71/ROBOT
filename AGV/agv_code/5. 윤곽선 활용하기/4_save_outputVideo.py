
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

# 비디오 프레임의 가로, 세로 크기 및 FPS 가져오기
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(5))

# VideoWriter 객체 생성
out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, (frame_width, frame_height))

while True:
    # 비디오 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    result_frame = find_contours_in_white(frame)
    cv2.imshow('Contours in White', result_frame)

    # 비디오 저장
    out.write(result_frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# VideoWriter 객체 해제
out.release()

# 비디오 캡처 객체 해제
cap.release()
cv2.destroyAllWindows()
