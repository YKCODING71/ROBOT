import socket
import struct
import cv2
import pickle
# import RPi.GPIO as GPIO
import threading
# from motor_control import *
# from Rosmaster_Lib import Rosmaster
#from pymycobot.myagv import MyAgv
########from myagv import MyAgv


# GPIO.setmode(GPIO.BCM)
###########################################################################
def initMotor() :
   print("init")

def goForward() :
   #print("goForward")
   print("F")
   # speed_x=  0.2
   # speed_y = 0.0
   # speed_z = 0.0
   # bot.set_car_motion(speed_x, speed_y, speed_z)
   #########MA.go_ahead(20, timeout=1)

def stopMotor() :
   #print("stopMotor")
   print("S")
   # speed_x= 0.0
   # speed_y = 0.0
   # speed_z = 0.0
   # bot.set_car_motion(speed_x, speed_y, speed_z)
   ##########MA.stop()

def goBackward() :
   #print("goBackward")
   print("B")
   # speed_x= -0.2
   # speed_y = 0.0
   # speed_z = 0.0
   # bot.set_car_motion(speed_x, speed_y, speed_z)
   #############MA.retreat(20, timeout=1)

def turnLeft() :
   #print("turnLeft")
   print("L")
   # speed_x= 0.0
   # speed_y = 0.2
   # speed_z = 0.0
   # bot.set_car_motion(speed_x, speed_y, speed_z)
   #############MA.pan_left(20, timeout=1)

def turnRight() :
   #print("turnRight")
   print("R")
   # speed_x= 0.0
   # speed_y = - 0.2
   # speed_z = 0.0
   # bot.set_car_motion(speed_x, speed_y, speed_z)
   #############MA.pan_right(20, timeout=1)

def exitMotor() :
   print("exitMotor")

#####################################################################


initMotor()

# bot = Rosmaster()   # add
###########MA = MyAgv('/dev/ttyAMA2', 115200)

# VIDSRC = 'v4l2src device=/dev/video0 ! video/x-raw,width=160,height=120,framerate=20/1 ! videoscale ! videoconvert ! jpegenc ! appsink'

# cap=cv2.VideoCapture(VIDSRC, cv2.CAP_GSTREAMER)
cap = cv2.VideoCapture(0)

HOST = ''
PORT = 8089

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

server.bind((HOST, PORT))
print('Socket bind complete')

server.listen(10)
print('Socket now listening')

server_cam, addr = server.accept()
server_mot, addr = server.accept()
print('New Client.')

flag_exit = False
def mot_main() :

   while True:

      rl_byte = server_mot.recv(1)
      rl = struct.unpack('!B', rl_byte)

      right, left = (rl[0] & 2)>>1, rl[0] & 1
      print(rl[0])

      if not right and not left:
         goForward()
      elif not right and left:
         turnRight()
      elif right and not left:
         turnLeft()
      else:
         stopMotor()

      if flag_exit: break

motThread = threading.Thread(target=mot_main)
motThread.start()

try:

   while True:

      cmd_byte = server_cam.recv(1)
      cmd = struct.unpack('!B', cmd_byte)
      # print(cmd[0])
      if cmd[0]==12 :

         # capture camera data
         ret,frame=cap.read()

         # Serialize frame
         data = pickle.dumps(frame)

         # send sensor + camera data
         data_size = struct.pack("!L", len(data))
         server_cam.sendall(data_size + data)

except KeyboardInterrupt:
   pass
except ConnectionResetError:
   pass
except BrokenPipeError:
   pass
except:
   pass

flag_exit = True
motThread.join()

server_cam.close()
server_mot.close()
server.close()

exitMotor()
# GPIO.cleanup()