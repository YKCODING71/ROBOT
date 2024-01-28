from tkinter import *
main = Tk()
main.title("Tk")
main.geometry("300x200")

lbl = Label(main, text="안녕하세요", font="Arial 20")
lbl.pack()
ok_button = Button(main, text="확인", foreground="Red")
ok_button.pack()
cancel_btn = Button(main, text="취소", foreground="Green")
cancel_btn.pack()

main.mainloop()
