import cv2
import mediapipe as mp
import numpy as np
import serial
import time

counter =0
arm_down = True

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# 아두이노와의 시리얼 통신을 설정합니다.
arduino = serial.Serial('COM13', 115200, timeout=0.1)  

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End
    
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
        
    return angle

 
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # RGB 이미지로 변환하기
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False      
        
        results = pose.process(image)    
         
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)        
         
        try:
            landmarks = results.pose_landmarks.landmark
            
            # 각 관절의 위치점 찾기
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, 
												landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, 
										 landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, 
											landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            shoulder_pos = tuple(np.multiply(shoulder, [640, 480]).astype(int))
            elbow_pos = tuple(np.multiply(elbow, [640, 480]).astype(int))
            wrist_pos = tuple(np.multiply(wrist, [640, 480]).astype(int))                


            # 포인트 비주얼 처리
            
            cv2.circle(image, shoulder_pos, 10, (255,0,0), -1)
            cv2.circle(image, elbow_pos, 10, (0,255,0), -1)
            cv2.circle(image, wrist_pos, 10, (0,0,255), -1)             
            cv2.line(image, shoulder_pos, elbow_pos,   (255,255,0), 3)
            cv2.line(image, elbow_pos, wrist_pos, (0,255,255), 3)
            

            # 각도 계산하기
            angle = calculate_angle(shoulder, elbow, wrist)
            
            # 각도 표시하기
            cv2.putText(image, f'Angle: {round(angle, 2)}', 
												tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, 
												cv2.LINE_AA)
            
            if angle <= 45 and not arm_down:
                counter += 1
                arm_down = True
            
            if angle > 45 :
                arm_down = False 

            cv2.putText(image, f'Count: {counter}', 
                        (10, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            
            # 아두이노에 각도 송신하기
            arduino.write(f'{angle}\n'.encode())
                       
        except:
            pass
        
        """
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))               
        
        """
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()