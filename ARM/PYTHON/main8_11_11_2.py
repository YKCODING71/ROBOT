import tkinter
import tkinter.font
import time

ANGLE = 0                  


def send_servo(self):
    value = scale.get()
    print(value)
    time.sleep(0.1)
    
def process():                                   
    en1.delete(0,"end")                        
    en1.insert(0,str(scale.get()))
 #   en1.insert(0,',')
 #   en1.insert(0,str(scale.get()))

#def multi():


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
    
    scale.set(90)       #/슬라이드 초기값을 90으로 정함
    label.grid(row = 0, column = 0, columnspan=3)
    scale.grid(row = 3, column = 0, columnspan=3)
    
    bt1 = tkinter.Button(window, width='20',text="각도 등록",command=lambda: process())
    bt1.place(x=50, y=100)
    en1 = tkinter.Entry(window)                                 #입력가능창 
    en1.place(x=300, y=100)
#    bt2 = tkinter.Button(window, width='20',text="전송",command=lambda: multi())
#    bt3.place(x=50, y=100)
    window.mainloop()
    
    