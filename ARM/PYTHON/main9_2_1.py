import cv2

def main():
    camera = cv2.VideoCapture(0)
    camera.set(3,640)
    camera.set(4,480)
        
    while( camera.isOpened() ):
        _, image = camera.read()
        cv2.imshow('camera test',image)
        
        if cv2.waitKey(10) == ord('q'): #10초간 기다림
            break
    
    cv2.destroyAllWindows()             #열린창 모두 닫기

if __name__ == '__main__':
    main()