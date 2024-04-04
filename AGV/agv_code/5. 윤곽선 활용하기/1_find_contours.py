import cv2
import numpy as np

image = cv2.imread('rgb.png')

# 그레이스케일 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 가우시안 블러 적용
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny 에지 검출
edges = cv2.Canny(blurred, 50, 150)

# 윤곽선 찾기
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 바깥쪽 윤곽선 잡기

# 이미지에 윤곽선 그리기
cv2.drawContours(image, contours, -1, (0, 0, 0), 2)

# 결과 보기
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
