import cv2
import serial
import time

def main():
    camera = cv2.VideoCapture(0)
    camera.set(3,320)
    camera.set(4,240)
    
    portNum = "COM8"
    ser = serial.Serial(portNum, 9600, timeout=1)           
     
    while True:
        _, frame = camera.read()  

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower_my = (0,100,100)
        upper_my = (20,255,255)
        
        lower_red = (160, 50, 50)
        upper_red = (180, 255, 255)
    
        myMask = cv2.inRange(hsv,lower_my,upper_my)        
        redMask = cv2.inRange(hsv, lower_red, upper_red)
        img_mask = myMask + redMask 
        cv2.imshow('myMask',myMask)
        cv2.imshow('redMask',redMask)
        cv2.imshow('img_mask',img_mask)
      
        cont_list,hierachy = cv2.findContours(img_mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        try:
            c = max(cont_list,key=cv2.contourArea) 
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.drawContours(frame,c,-1,(0,0,255),1)
        except :
            pass 
        
        cv2.circle(frame, (cx,cy),10,(0,255,0),-1) 
        cv2.imshow('mask',frame)
       
        a=int(cx/2)
        sendData = f"a90sb90sc90sd{a}s\n"
        ser.write(sendData.encode())         
        read_data = ser.readline()
        print(read_data.decode())
        time.sleep(0.1)

        if cv2.waitKey(1) == ord('q'):
            break
    
    cv2.destroyAllWindows()
  
if __name__ == '__main__':
    main()
     