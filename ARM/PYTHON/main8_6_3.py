import cv2
import time
import serial
import serial.tools.list_ports

def send_rgb_led(red,green,blue):
    sendData = f"RGB={red},{green},{blue}\n"
    my_serial.write( sendData.encode() )

def main():
    camera = cv2.VideoCapture(1)
    camera.set(3,640)
    camera.set(4,480)
        
    while True:
        _, frame = camera.read()  

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = (100,100,120)
        upper_blue = (150,255,255)
        
        lower_green = (50, 150, 50)
        upper_green = (80, 255, 255)
        
        lower_red = (150, 50, 50)
        upper_red = (180, 255, 255)
                
        redMask = cv2.inRange(hsv, lower_red, upper_red)   
        greenMask = cv2.inRange(hsv, lower_green, upper_green)  
        blueMask = cv2.inRange(hsv, lower_blue, upper_blue)  

        redPixels = cv2.countNonZero(redMask)
        greenPixels = cv2.countNonZero(greenMask)
        bluePixels = cv2.countNonZero(blueMask)
        
        #print(redPixels,greenPixels,bluePixels)
        
        colorList = [redPixels,greenPixels,bluePixels]
        maxValue = max(colorList)
        maxPos = colorList.index(maxValue)
        #print( maxValue, maxPos)
        
        if maxValue >= 500:
            if maxPos == 0: #red
                print("red")
                send_rgb_led(255,0,0)
            elif maxPos == 1: #green
                print("green")
                send_rgb_led(0,255,0)
            elif maxPos == 2: #blue
                print("blue")
                send_rgb_led(0,0,255)
        else:
            pass
            
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'Arduino Uno' in p.description:
            print(f"{p} 포트에 연결하였습니다.")
            my_serial = serial.Serial(p.device, baudrate=9600, timeout=1.0)
            time.sleep(2.0)
    
    main()
    
    my_serial.close()