import cv2

image = cv2.imread("rgb.png")

# ROI 좌표 = (x, y), width, and height
x, y, width, height = 350, 400, 500, 800

# ROI 추출
roi = image[y:y+height, x:x+width]

# 추출된 ROI 이미지 프로세싱 (회색으로 바꾸기)
gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", image)
cv2.imshow("Processed ROI", gray_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
