import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def process_frame(frame):
    height, width, _ = frame.shape
    roi_height = int(height / 3)
    roi_top = height - roi_height
    roi = frame[roi_top:, :]

    # 그레이스케일 이미지에서 중앙 선 그리기
    cv2.line(roi, (width // 2, 0), (width // 2, roi_height), (0, 255, 0), 2)

    # 색상 변화 및 이진화 
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    lower_white = np.array([0, 0, 200], dtype=np.uint8)
    upper_white = np.array([255, 30, 255], dtype=np.uint8)
    white_mask = cv2.inRange(hsv, lower_white, upper_white)

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 윤곽선 검출 및 처리 
    if len(contours) >= 1:
        max_contour = max(contours, key=cv2.contourArea)
        cv2.drawContours(roi, [max_contour], -1, (0, 255, 0), 2)

        # 물체의 중심 계산 및 결과 출력 
        M = cv2.moments(max_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            
            center_line = width // 2
            if cx < center_line - 50:
                return "LEFT"
            elif cx > center_line + 50:
                return "RIGHT"

    return None

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera error")
        break

    result = process_frame(frame)
    
    if result:
        print(result)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(2000) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()