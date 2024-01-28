import time
import serial
import serial.tools.list_ports
import threading

ports = list(serial.tools.list_ports.comports())
for p in ports:
    if 'Arduino Uno' in p.description:
        print(f"{p} 포트에 연결하였습니다.")
        my_serial = serial.Serial(p.device, baudrate=9600, timeout=1.0)
        time.sleep(2.0)

def serial_read_thread():
    while True:
        read_data = my_serial.readline()
        print(read_data.decode())

t1 = threading.Thread(target=serial_read_thread)
t1.daemon = True
t1.start()

def send_rgb_led(red,green,blue):
    sendData = f"RGB={red},{green},{blue}\n"
    my_serial.write( sendData.encode() )

try:
    while True:
        send_rgb_led(255,0,0)
        time.sleep(1.0)
        
        send_rgb_led(0,255,0)
        time.sleep(1.0)
        
        send_rgb_led(0,0,255)
        time.sleep(1.0)

except KeyboardInterrupt:
    pass

my_serial.close()