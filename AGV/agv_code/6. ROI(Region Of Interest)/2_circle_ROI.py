import cv2
import numpy as np

image = cv2.imread("rgb.png")
image = cv2.resize(image, dsize=(300, 450))

# ROI 중심 좌표 (x, y) 및 반지름 정의
center_coordinates = (150, 150)
radius = 100

# 원 모양 ROI를 위한 마스크 생성
mask = np.zeros_like(image)
cv2.circle(mask, center_coordinates, radius, (255, 255, 255), thickness=cv2.FILLED)

# 비트와이즈 AND 연산을 사용하여 원 모양 ROI 추출
circular_roi = cv2.bitwise_and(image, mask)

# 추출한 원 모양 ROI에 처리 적용 (예: 엣지 검출)
edges = cv2.Canny(circular_roi, 400, 150)

# 원본 이미지, 원 모양 ROI 및 처리된 원 모양 ROI 표시
cv2.imshow("Original", image)
cv2.imshow("Circle ROI", circular_roi)
cv2.imshow("Processed Circle ROI", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
