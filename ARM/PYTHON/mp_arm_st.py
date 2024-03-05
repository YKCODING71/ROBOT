import cv2
import mediapipe as mp
import numpy as np
import serial
import time
def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle
def calculate_shoulder_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle
def main():
    portNum = "COM8"
    ser = serial.Serial(portNum, 9600, timeout=1)
    # 비디오 캡처 객체 생성
    cap = cv2.VideoCapture(0)
    # MediaPipe 포즈 객체 생성
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    # 동영상 해상도 설정
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # 포즈 추정을 위해 BGR을 RGB로 변환
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 포즈 추정
        results = pose.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        landmarks = results.pose_landmarks.landmark
        shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
        wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
        frame_height, frame_width = image.shape[:2]
        shoulder = int(shoulder[0] * frame_width), int(shoulder[1] * frame_height)
        elbow = int(elbow[0] * frame_width), int(elbow[1] * frame_height)
        wrist = int(wrist[0] * frame_width), int(wrist[1] * frame_height)
        # 선 그리기
        cv2.line(image, shoulder, elbow, (255,255,0), thickness=3)
        cv2.line(image, elbow, wrist, (255,255,0), thickness=3)
        # 각도 계산
        angle = 180 - calculate_angle(shoulder, elbow, wrist)
        angle_shoulder = calculate_shoulder_angle(elbow, shoulder, [elbow[0],shoulder[1]])
        print(angle_shoulder)
        angle_str = 'a0sb' + str(int(angle_shoulder)) + 'sc' + str(int(angle)) + 's' + 'd0s\n'
        ser.write(angle_str.encode('utf-8'))
        cv2.putText(image, f'Angle: {round(angle, 2)}', elbow, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Mediapipe Feed', image)
        if cv2.waitKey(30) & 0xFF ==  ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()