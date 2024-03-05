from tkinter import *
import serial
import time

# 1. 기본 설정
win = Tk()
win.geometry("700x700")
win.title("MyRobo Pendant")
win.config(bg="#6ba4ff")
win.option_add("*Font", "맑은고딕 20")

portNum = "COM8"
ser = serial.Serial(portNum, 9600, timeout=1)

ang_list = [0,0,0,0]

# 3. 기능 구현
# 3.1 슬라이드바
def sliding1(v):
    lab_ang1.config(text=v)
    ang_list[0] = v
def sliding2(v):
    lab_ang2.config(text=v)
    ang_list[1] = v
def sliding3(v):
    lab_ang3.config(text=v)
    ang_list[2] = v
def sliding4(v):
    lab_ang4.config(text=v)
    ang_list[3] = v

# 3.2 등록 버튼
def btn_ent_fix():
    selectN = rv.get()
    if selectN == 0:
        ent1.delete(0, END)
        ent1.insert(0, ', '.join(map(str, ang_list)))
    elif selectN == 1:
        ent2.delete(0, END)
        ent2.insert(0, ', '.join(map(str, ang_list)))
    else:
        ent3.delete(0, END)
        ent3.insert(0, ', '.join(map(str, ang_list)))

# 3.3 아두이노로 각도 보내기 (수업시간에 블라이드 처리!!!)
def angles2Ardu(angles):
    a, b, c, d = angles.split(', ')
    Tk2Ardu = 'a'+a+'b'+b+'c'+c+'d'+d
    ser.write(Tk2Ardu.encode('utf-8'))
    # Tk2Ardu = ['a'+a, 'b'+b, 'c'+c, 'd'+d]
    # for i in Tk2Ardu:
    #     ser.write(i.encode('utf-8'))
    #     ser.reset_output_buffer() #시리얼 tx버퍼 비우기. 딜레이 No!
    #     time.sleep(0.1)

    # from 아두이노: 데이터 송수신 검사용
    while True:
        data_in = ser.readline().decode('utf-8').strip('\n')
        print(f"Data In: {data_in}")

# 3.4 구동 버튼
def btn_op1_start():
    angles = ent1.get()
    print(angles)
    angles2Ardu(angles)
def btn_op2_start():
    angles = ent2.get()
    print(angles)
    angles2Ardu(angles)
def btn_op3_start():
    angles = ent3.get()
    print(angles)
    angles2Ardu(angles)

# 3.5 시리얼 포트 닫고 창닫기
def close_serial():
    ser.close()
    win.destroy()

# 2. 화면 구성
# 2.1.1 모터번호 라벨 생성
lab0 = Label(win, text="모터")
lab0.grid(column=0, row=0, padx=5, pady=5, sticky="w")

lab1 = Label(win, text="#1")
lab1.grid(column=0, row=1, padx=5, pady=5, sticky="w")
lab2 = Label(win, text="#2")
lab2.grid(column=0, row=2, padx=5, pady=5, sticky="w")
lab3 = Label(win, text="#3")
lab3.grid(column=0, row=3, padx=5, pady=5, sticky="w")
lab4 = Label(win, text="#4")
lab4.grid(column=0, row=4, padx=5, pady=5, sticky="w")

# 2.1.2 각도표시 라벨 생성 (입력창 대체)
lab_ang1 = Label(win, text="000")
lab_ang1.grid(column=1, row=1, padx=5, pady=5, sticky="w")
lab_ang2 = Label(win, text="000")
lab_ang2.grid(column=1, row=2, padx=5, pady=5, sticky="w")
lab_ang3 = Label(win, text="000")
lab_ang3.grid(column=1, row=3, padx=5, pady=5, sticky="w")
lab_ang4 = Label(win, text="000")
lab_ang4.grid(column=1, row=4, padx=5, pady=5, sticky="w")

# 2.2 버튼 생성
# 등록 버튼
btn_ent = Button(win, text="   각도 등록   ")
btn_ent.config(command=btn_ent_fix)
btn_ent.grid(column=1, row=0, padx=5, pady=5, sticky="w")

# 2.4 스케일(슬라이더)
sl1 = Scale(win, from_=0, to_=180, orient=HORIZONTAL, command=sliding1, showvalue=False)
sl1.grid(column=2, row=1, columnspan=3)
sl2 = Scale(win, from_=0, to_=180, orient=HORIZONTAL, command=sliding2, showvalue=False)
sl2.grid(column=2, row=2, columnspan=3)
sl3 = Scale(win, from_=0, to_=180, orient=HORIZONTAL, command=sliding3, showvalue=False)
sl3.grid(column=2, row=3, columnspan=3)
sl4 = Scale(win, from_=0, to_=180, orient=HORIZONTAL, command=sliding4, showvalue=False)
sl4.grid(column=2, row=4, columnspan=3)

# 2.5 등록각도 라벨
# 2.5.1 각도 번호
lab_a1 = Label(win, text="번호")
lab_a1.grid(column=0, row=5, padx=5, pady=5, sticky="w")

# 2.5.1 등록각도
angles1 = Label(win, text="   등록 각도   ")
angles1.grid(column=1, row=5, padx=5, pady=5, sticky="w")

# 2.6 등록각도 라디오버튼
rv = IntVar()
rb1 = Radiobutton(win, value=0, variable=rv)
rb2 = Radiobutton(win, value=1, variable=rv)
rb3 = Radiobutton(win, value=2, variable=rv)
rb1.grid(column=0, row=6, padx=5, pady=5, sticky="w")
rb2.grid(column=0, row=7, padx=5, pady=5, sticky="w")
rb3.grid(column=0, row=8, padx=5, pady=5, sticky="w")

# 2.6 등록각도 입력필드
ent1 = Entry(win)
ent1.grid(column=1, row=6, padx=5, pady=5, sticky="w")
ent2 = Entry(win)
ent2.grid(column=1, row=7, padx=5, pady=5, sticky="w")
ent3 = Entry(win)
ent3.grid(column=1, row=8, padx=5, pady=5, sticky="w")

# 2.7 구동 버튼
btn_op1 = Button(win, text="구동")
btn_op2 = Button(win, text="구동")
btn_op3 = Button(win, text="구동")
btn_op1.config(command=btn_op1_start)
btn_op2.config(command=btn_op2_start)
btn_op3.config(command=btn_op3_start)
btn_op1.grid(column=2, row=6, padx=5, pady=5, sticky="w")
btn_op2.grid(column=2, row=7, padx=5, pady=5, sticky="w")
btn_op3.grid(column=2, row=8, padx=5, pady=5, sticky="w")

# 프로그램 종료 시 시리얼 포트 닫기
win.protocol("WM_DELETE_WINDOW", close_serial)

# q 키를 눌렀을 때 시리얼 포트 닫기
win.bind("<KeyPress-q>", lambda e: close_serial())

win.mainloop()