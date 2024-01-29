from tkinter import *
count = 0
count10 = 0

window = Tk()
window.title("연습장")
window.geometry('500x300+200+200')   

def countD1():
    global count
    count = int(en1.get()) 
    count += 1
    en1.delete(0,END)
    en1.insert(0,str(count))

def countD2():
    global count
    count = int(en1.get()) 
    count -= 1
    en1.delete(0,END)
    en1.insert(0,str(count))

la1 = Label(window,text="투입금액")
la1.grid(row=0, column=0) 
en1 = Entry(window)                                 
en1.grid(row=0, column=1)             
en1.insert(0,str(0))

bt1 = Button(window,height='2', width='20',text="1씩증가", command=countD1)
bt1.place(x=50, y=50)
bt2 = Button(window,height='2', width='20',text="1씩감소", command=countD2)
bt2.place(x=50, y=100)

window.mainloop()