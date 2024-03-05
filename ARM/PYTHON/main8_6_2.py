import cv2

def main():
    camera = cv2.VideoCapture(0)
    camera.set(3,320)
    camera.set(4,240)
        
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
        
        print(redPixels,greenPixels,bluePixels)
        
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()