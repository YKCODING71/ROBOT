import cv2
import time
import serial
import serial.tools.list_ports

def send_buzzer(freq):
    sendData = f"BUZZER={freq}\n"
    my_serial.write( sendData.encode() )

def main():
    camera = cv2.VideoCapture(0)
    camera.set(3,640)
    camera.set(4,480)
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_casecade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    
    sleep_count = 0
    while( camera.isOpened() ):
        _, image = camera.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(50,50),flags=cv2.CASCADE_SCALE_IMAGE)
        #print("faces detected Number: " + str(len(faces)))

        if len(faces):
            for (x,y,w,h) in faces:
                cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
                
                face_gray = gray[y:y+h, x:x+w]
                face_color = image[y:y+h, x:x+w]
                
                eyes = eye_casecade.detectMultiScale(face_gray,scaleFactor=1.2,minNeighbors=10)
                
                if len(eyes) == 0:
                    if sleep_count < 50:
                        sleep_count = sleep_count +1
                    
                    if sleep_count >= 50:
                        print("졸지마")
                        send_buzzer(1000)
                else:
                    if sleep_count >= 2:
                        sleep_count = sleep_count - 2
                    send_buzzer(0)
                
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(face_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)
        print(sleep_count)
        cv2.imshow('result', image)
        
        if cv2.waitKey(10) == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == '__main__':
    
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'CH340' in p.description:
            print(f"{p} 포트에 연결하였습니다.")
            my_serial = serial.Serial(p.device, baudrate=9600, timeout=1.0)
            time.sleep(2.0)
    
    main()
    
    my_serial.close()