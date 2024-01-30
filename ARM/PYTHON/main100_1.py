import cv2
import mediapipe as mp

# Mediapipe 라이브러리의 그림 그리기 유틸리티 및 Hands 모듈을 import합니다.
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 웹캠으로부터 비디오를 캡처하기 위해 OpenCV의 VideoCapture 객체를 생성합니다.
cap = cv2.VideoCapture(0)

# Mediapipe Hands 모듈을 설정합니다.
with mp_hands.Hands(
    max_num_hands=1,  # 검출할 손의 최대 개수 (이 경우 1개)
    min_detection_confidence=0.5,  # 검출 신뢰도의 최소값
    min_tracking_confidence=0.5) as hands:  # 추적 신뢰도의 최소값

    # 비디오 프레임을 캡처하고 처리하는 메인 루프입니다.
    while cap.isOpened():
        # 카메라로부터 한 프레임을 읽습니다.
        success, image = cap.read()
        if not success:
            continue

        # 이미지를 좌우 반전하여 셀피 뷰로 표시합니다.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        # Mediapipe Hands 모듈을 사용하여 손의 랜드마크를 처리합니다.
        results = hands.process(image)

        # 이미지를 BGR로 변환합니다.
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # 손의 랜드마크가 감지되었는지 확인합니다.
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # 특정 손가락 랜드마크의 x-좌표를 추출합니다.
                finger1 = int(hand_landmarks.landmark[4].x * 100)
                finger2 = int(hand_landmarks.landmark[8].x * 100)

                # 두 손가락 사이의 거리를 계산합니다.
                dist = abs(finger1 - finger2)

                # 이미지에 거리 정보를 표시합니다.
                cv2.putText(
                    image, text='f1=%d f2=%d dist=%d ' % (finger1,finger2,dist), org=(10, 30),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                    color=(255, 255, 255), thickness=3)

                # 이미지에 손의 랜드마크 및 연결을 그립니다.
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # 처리된 이미지를 화면에 표시합니다.
        cv2.imshow('image', image)

        # 'q' 키가 눌리면 루프를 종료합니다.
        if cv2.waitKey(1) == ord('q'):
            break

# 카메라를 해제하고 모든 OpenCV 창을 닫습니다.
cap.release()
cv2.destroyAllWindows()
