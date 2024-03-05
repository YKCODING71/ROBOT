import time
import serial
import serial.tools.list_ports
import threading

def serial_read_thread():
    while True:
        read_data = my_serial.readline()
        print(read_data.decode())
        
def main():
    try:
        while True:
            pass

    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'CH340' in p.description:
            print(f"{p} 포트에 연결하였습니다.")
            my_serial = serial.Serial(p.device, baudrate=9600, timeout=1.0)
            time.sleep(2.0)

    t1 = threading.Thread(target=serial_read_thread)
    t1.daemon = True
    t1.start()
    
    main()
    
    my_serial.close()