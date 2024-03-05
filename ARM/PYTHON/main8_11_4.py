from tkinter import *
from random import random
from datetime import datetime

# 0. 기본 설정
win = Tk()
win.title("Shoot_em_all!")
win.geometry("700x500")
win.option_add("*Font", "맑은고딕 20")
win.config(bg="#6ba4ff")

# 2. 게임 진행
k = 1
timer1 = datetime.now()

# 2.3 타겟 재생 및 미션 종료
def target_Respawn():
    global k
    if k < goal:
        k += 1
        btnPop.destroy()
        target_Pop()
    else:
        fin = datetime.now()
        diff_sec = (fin - start).total_seconds()
        btnPop.destroy()
        lab = Label(win)
        lab.config(text="Mission Clear\n"+str(f"{diff_sec:0.2f}") + "초", pady=250)
        lab.pack()

# 2.2 타겟 생성
def target_Pop():
    global btnPop
    global start
    btnPop = Button(win)
    btnPop.config(bg="red", padx=10, pady=10)
    btnPop.config(text=k)
    canvas_width = win.winfo_reqwidth() - 5
    canvas_height = win.winfo_reqheight() - 5
    btnPop.place(relx= random() * canvas_width / win.winfo_reqwidth(), rely=random() * canvas_height / win.winfo_reqheight())
    btnPop.config(command=target_Respawn)

# 2.1 타켓 클릭 액션
def btn_action():
    global goal
    global start
    goal = int(ent.get())
    #라벨, 엔트리, 버튼 등 모든 위젯 없애기
    for wg in win.grid_slaves(): 
        wg.destroy()
    win.geometry("500x500")
    target_Pop()
    start = datetime.now()

# 1. 화면 구성
# Label
lab = Label(win)
lab.config(text = "Kills")
lab.grid(column=0, row=0, padx=20, pady=20)

# Entry
ent = Entry(win)
ent.grid(column=1, row=0, padx=20, pady=20)

# Button
btn = Button(win)
btn.config(text = "게임 시작")
btn.grid(column=3, row=0, columnspan=2)
btn.config(command=btn_action)

win.mainloop()