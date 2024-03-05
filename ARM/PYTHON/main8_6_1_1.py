import numpy as np
import cv2

def main():
    blue = np.uint8([[[255,0,0]]])
    green = np.uint8([[[0,128,0]]])        
    red = np.uint8([[[0,0,255]]]) 
    hsv_blue=cv2.cvtColor(blue,cv2.COLOR_BGR2HSV) 
    hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV) 
    hsv_red=cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
     
    print("blue",hsv_blue)      
    print("green",hsv_green)      
    print("red",hsv_red)      

if __name__ == '__main__':
    main()