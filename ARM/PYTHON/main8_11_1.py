import tkinter
import tkinter.font
import time

def send_servo(v):
    print(v)
    time.sleep(0.1)

if __name__ == '__main__':
        
    window = tkinter.Tk()
    window.title("SERVO CONTROL")
    window.geometry("500x200")
    window.resizable(False,False)

    font = tkinter.font.Font(size = 20)
    label = tkinter.Label(window, text="SERVO DIGREE", font=font)

    var = tkinter.IntVar()
    scale = tkinter.Scale(window, variable=var, command=send_servo, orient="horizontal",
                        showvalue=True,tickinterval=20,to=180, length=500)
    
    scale.set(90)       #슬라이드 초기값을 90으로 정함
    label.grid(row = 0, column = 0)
    scale.grid(row = 1, column = 0)

    window.mainloop()
    
    