import cv2
import numpy as np

def find_contours_in_color_range(image, lower_range, upper_range):
    # 이미지를 HSV로 변환
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 지정한 색 범위에 해당하는 마스크 생성
    color_mask = cv2.inRange(hsv_image, lower_range, upper_range)

    # 마스크와 원본 이미지 비트와 연산
    masked_image = cv2.bitwise_and(image, image, mask=color_mask)

    # 마스크 이미지를 그레이스케일로 변환
    gray_mask = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)

    # 이진화 처리
    _, binary_mask = cv2.threshold(gray_mask, 1, 255, cv2.THRESH_BINARY)

    # 윤곽선 찾기
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 윤곽선 그리기
    cv2.drawContours(image, contours, -1, (0, 0, 0), 5)

    return image

# 이미지 불러오기
image = cv2.imread('rgb.png')

# 찾고자 하는 색상 범위 (예: 빨간색)
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# 특정 색상 영역의 윤곽선을 찾아 이미지에 표시
result_image = find_contours_in_color_range(image, lower_red, upper_red)

# 결과 보기
cv2.imshow('Contours in Red', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
