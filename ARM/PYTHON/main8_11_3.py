import tkinter
import tkinter.font
import time
import serial
import serial.tools.list_ports
import threading


def send_servo(digree):
    sendData = f"SERVO=a{digree}\n"
    my_serial.write( sendData.encode() )
    read_data = my_serial.readline()
    print(read_data.decode())
    print("1")

def send_servo2(digree):
    sendData = f"SERVO=b{digree}\n"
    my_serial.write( sendData.encode() )
    read_data = my_serial.readline()
    print(read_data.decode())
    print("2")

def send_servo3(digree):
    sendData = f"SERVO=c{digree}\n"
    my_serial.write( sendData.encode() )
    read_data = my_serial.readline()
    print(read_data.decode())
    print("3")
    
def send_servo4(digree):
    sendData = f"SERVO=d{digree}\n"
    my_serial.write( sendData.encode() )
    read_data = my_serial.readline()
    print(read_data.decode())
    print("4")
    
if __name__ == '__main__':
    c = 0
            
    window = tkinter.Tk()
    window.title("SERVO CONTROL")
    window.geometry("500x600")
    window.resizable(False,False)

    font = tkinter.font.Font(size = 20)
    label = tkinter.Label(window, text="ROBOT ARM", font=font)
    label.pack()
    var = tkinter.IntVar()
    var2 = tkinter.IntVar()
    var3 = tkinter.IntVar()
    var4 = tkinter.IntVar()
    
    scale = tkinter.Scale(window, variable=var, command=send_servo, orient="horizontal",
                        showvalue=True,tickinterval=20,to=180, length=500)
    scale.pack()
    scale2 = tkinter.Scale(window, variable=var2, command=send_servo2, orient="horizontal",
                        showvalue=True,tickinterval=20,to=180, length=500)
    scale2.pack()
    scale3 = tkinter.Scale(window, variable=var3, command=send_servo3, orient="horizontal",
                        showvalue=True,tickinterval=20,to=180, length=500)
    scale3.pack()
    scale4 = tkinter.Scale(window, variable=var4, command=send_servo4, orient="horizontal",
                        showvalue=True,tickinterval=20,to=180, length=500)
    scale4.pack()
    
    scale.set(90)
    scale2.set(90)
    scale3.set(90)
    scale4.set(90)

    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'CH340' in p.description:
            print(f"{p} 포트에 연결하였습니다.")
            my_serial = serial.Serial(p.device, baudrate=9600, timeout=0.1)
            time.sleep(2.0)
            
    window.mainloop()