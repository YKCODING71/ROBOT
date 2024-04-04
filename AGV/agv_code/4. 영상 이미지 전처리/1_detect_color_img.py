import cv2
import numpy as np

# 이미지 읽기
img_path = "rgb.png"
image = cv2.imread(img_path)

# BGR을 HSV 컬러 스페이스로 변환
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 흰색 영역 검출
lower_white = np.array([0, 0, 200], dtype=np.uint8)
upper_white = np.array([255, 30, 255], dtype=np.uint8)
white_mask = cv2.inRange(hsv, lower_white, upper_white)
white_result = cv2.bitwise_and(image, image, mask=white_mask)

# 결과 이미지 표시
cv2.imshow("Original", image)
cv2.imshow("White", white_result)

# 창 종료 
cv2.waitKey(0)
cv2.destroyAllWindows()
