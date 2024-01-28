import serial
import time

my_serial = serial.Serial("COM28", baudrate=9600, timeout=1.0)
time.sleep(2.0)

try:
    while True:
        sendData = "RGB=255,0,0\n"
        my_serial.write( sendData.encode() )
        time.sleep(1.0)
        
        sendData = "RGB=0,255,0\n"
        my_serial.write( sendData.encode() )
        time.sleep(1.0)
        
        sendData = "RGB=0,0,255\n"
        my_serial.write( sendData.encode() )
        time.sleep(1.0)

except KeyboardInterrupt:
    pass

my_serial.close()