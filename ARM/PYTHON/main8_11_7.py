from tkinter import *


win = Tk()
win.geometry("700x700")
win.title("MyRobo Pendant")
win.config(bg="#6ba4ff")
win.option_add("*Font", "맑은고딕 20")
'''
lab0 = Label(win, text="모터")
lab0.grid(column=0, row=1, padx=5, pady=5, sticky="w")
lab1 = Label(win, text="모터")
lab1.grid(column=0, row=2, padx=5, pady=5, sticky="w")
lab2 = Label(win, text="모터")
lab2.grid(column=0, row=3, padx=5, pady=5, sticky="w")

lab_ang1 = Label(win, text="000")
lab_ang1.grid(column=1, row=1, padx=5, pady=5, sticky="w")
lab_ang2 = Label(win, text="000")
lab_ang2.grid(column=1, row=2, padx=5, pady=5, sticky="w")
lab_ang3 = Label(win, text="000")
lab_ang3.grid(column=1, row=3, padx=5, pady=5, sticky="w")
lab_ang4 = Label(win, text="000")
lab_ang4.grid(column=1, row=4, padx=5, pady=5, sticky="w")

sl1 = Scale(win, from_=0, to_=180, orient=HORIZONTAL,  showvalue=False)
sl1.grid(column=2, row=1, columnspan=3)
sl2 = Scale(win, from_=0, to_=180, orient=HORIZONTAL,  showvalue=False)
sl2.grid(column=2, row=2, columnspan=3)
sl3 = Scale(win, from_=0, to_=180, orient=HORIZONTAL,  showvalue=False)
sl3.grid(column=2, row=3, columnspan=3)
sl4 = Scale(win, from_=0, to_=180, orient=HORIZONTAL,  showvalue=False)
sl4.grid(column=2, row=4, columnspan=3)
'''

lab0 = Label(win, text="모터1")
lab0.grid(column=0, row=1, padx=5, pady=5, sticky="w") 
lab1 = Label(win, text="모터2")
lab1.grid(column=0, row=2, padx=5, pady=5, sticky="w")
lab2 = Label(win, text="모터3")
lab2.grid(column=0, row=3, padx=5, pady=5, sticky="w")

lab_ang1 = Label(win, text="000")
lab_ang1.grid(column=1, row=1, padx=5, pady=5, sticky="w")
lab_ang2 = Label(win, text="000")
lab_ang2.grid(column=1, row=2, padx=5, pady=5, sticky="w")
lab_ang3 = Label(win, text="000")
lab_ang3.grid(column=1, row=3, padx=5, pady=5, sticky="w")
lab_ang4 = Label(win, text="000")
lab_ang4.grid(column=1, row=4, padx=5, pady=5, sticky="w")

sl1 = Scale(win, from_=0, to_=180, orient=HORIZONTAL,  showvalue=False)
sl1.grid(column=2, row=1, columnspan=3)
sl2 = Scale(win, from_=0, to_=180, orient=HORIZONTAL,  showvalue=False)
sl2.grid(column=2, row=2, columnspan=3)
sl3 = Scale(win, from_=0, to_=180, orient=HORIZONTAL,  showvalue=False)
sl3.grid(column=2, row=3, columnspan=3)
sl4 = Scale(win, from_=0, to_=180, orient=HORIZONTAL,  showvalue=False)
sl4.grid(column=2, row=4, columnspan=3)



win.mainloop()