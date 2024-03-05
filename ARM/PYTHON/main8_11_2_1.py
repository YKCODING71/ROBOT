import tkinter
import tkinter.font
import time
import serial
import serial.tools.list_ports

def send_servo(digree):
   # sendData = f"SERVO={digree}\n"
    sendData = f"a90sb90sc90sd100s\n"
    my_serial.write( sendData.encode() )
    read_data = my_serial.readline()
    print(read_data.decode())

if __name__ == '__main__':
    
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'CH340' in p.description:
            print(f"{p} 포트에 연결하였습니다.")
            my_serial = serial.Serial(p.device, baudrate=9600, timeout=1.0)
            time.sleep(2.0)
    
    window = tkinter.Tk()
    window.title("SERVO CONTROL")
    window.geometry("500x200")
    window.resizable(False,False)

    font = tkinter.font.Font(size = 20)
    label = tkinter.Label(window, text="SERVO DIGREE", font=font)

    var = tkinter.IntVar()
    scale = tkinter.Scale(window, variable=var, command=send_servo, orient="horizontal",
                        showvalue=True,tickinterval=20,to=180, length=500)
    scale.set(90)
    label.grid(row = 0, column = 0)
    scale.grid(row = 1, column = 0)

    window.mainloop()