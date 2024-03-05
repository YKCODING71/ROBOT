import time
import serial
import serial.tools.list_ports
import threading

def send_temperature():
    sendData = f"TEMPERATURE=?\n"
    my_serial.write( sendData.encode() )

def send_humidity():
    sendData = f"HUMIDITY=?\n"
    my_serial.write( sendData.encode() )

serial_receive_data = ""
def serial_read_thread():
    global serial_receive_data
    while True:
        read_data = my_serial.readline()
        serial_receive_data = read_data.decode()

def send_temp_humi():
    t2 = threading.Timer(1, send_temp_humi)
    t2.daemon = True
    t2.start()
    send_temperature()
    time.sleep(0.2)
    send_humidity()
    time.sleep(0.2)

def main():
    try:
        send_temp_humi()
        global serial_receive_data
        while True:
            if "TEMPERATURE=" in serial_receive_data:
                print("온도:",serial_receive_data[12:])
                serial_receive_data = ""
            elif "HUMIDITY=" in serial_receive_data:
                print("습도:",serial_receive_data[9:])
                serial_receive_data = ""

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