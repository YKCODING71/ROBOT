import cv2
import numpy as np

cap = cv2.VideoCapture('testVideo.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # 이미지를 hsv로 변환 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 흰색 영역 검출
    lower_white = np.array([200, 200, 200], dtype=np.uint8)
    upper_white = np.array([255, 255, 255], dtype=np.uint8)
    white_mask = cv2.inRange(frame, lower_white, upper_white)

    # 흰색 영역 이외는 검은색으로 출력 
    white_result = cv2.bitwise_and(frame, frame, mask=white_mask)
    
    ############### ROI ######################
    height, width = frame.shape[:2]
    roi_top = height * 2 // 3 # 상단 경계 
    roi_bottom = height # 하단 경계 
    roi_left = 0 # 왼쪽 경계 
    roi_right = width # 오른쪽 경계 
    roi = white_result[roi_top:roi_bottom, roi_left:roi_right]
    
    # 결과 이미지 표시
    cv2.imshow("Original", frame)
    cv2.imshow("White", white_result)
    cv2.imshow("ROI", roi)

    # 'q' 키 누르면 종료 
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.release()
cv2.destroyAllWindows()
