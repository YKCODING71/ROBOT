import time
import serial
import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
print(ports)
for p in ports:
    if 'Arduino Uno' in p.description:
        
        print(f"{p} 포트에 연결하였습니다.")

        my_serial = serial.Serial(p.device, baudrate=9600, timeout=1.0)
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