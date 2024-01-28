from tkinter import *
import tkinter

priceAM  = 200                                       #아메리카노 200, 믹스 100
priceMIX = 100   
priceMILK = 500
money = 0                                           #투입금액
window = Tk()                                       #시작    
window.title("자판기")                              #제목표시
window.geometry('500x300+200+200')                  #폭 500, 높이 300, 왼쪽에서 200픽셀만큼이동뒤, 위에서 200픽셀만큼 내려온뒤 표시


def process(price):                                 #커피선택버튼 클릭
    global money
        
    en1.delete(0,"end")                             #표시된 글자 삭제
    en2.delete(0,"end")
    if money< price  :                              #잔액이 100원 미만일 때
        en2.insert(0,str(money))                    #"잔액부족"     
    elif money<200 and price==200:                  #잔액이 200원미만이고, 아메리카노를 선택
        en2.insert(0,str("믹스커피만 가능합니다."))   #"믹스커피 선택" 

    else : 
        money -= price                              #투입금액이 200원이상일때 선택금액만큼만 빼고,표시
        en2.insert(0,str(money))


def p_get():                                        #확인  선택
    global money
    remoney = int(en1.get())                        #투입금액 가져오기

    if money>0 :                                    #잔액이 남아있으면, 투입금과  합한뒤 표시
        money += remoney
        en1.delete(0,"end")
        en2.delete(0,"end")
        en2.insert(0,str(money))

    else :                                          #잔액이 없으면, 커피선택을 안내함
        money = remoney   
        en2.delete(0,"end")
        en2.insert(0,str("커피를 선택하세요."))


la1 = Label(window,text="투입금액")                 #투입금액 글자 표시
la1.grid(row=0, column=0)                           #첫줄, 첫번째칸
en1 = Entry(window)                                 #입력가능창 
en1.grid(row=0, column=1)                           #첫줄, 두번째칸

la2 = Label(window,text="거스름돈")
la2.grid(row=1, column=0)
en2 = Entry(window)
en2.grid(row=1, column=1)

bt1 = Button(window,height='2', width='20',text="아메리카노 200원",command=lambda: process(priceAM))
bt1.place(x=50, y=50)
bt2 = Button(window,height='2', width='20',text=" 믹스커피 100원 ",command=lambda: process(priceMIX))
bt2.place(x=50, y=100)
bt3 = Button(window, text="확인",command=p_get)
bt3.grid(row=0,column=3)
bt4 = Button(window,height='2', width='20',text=" 밀크커피 500원 ",bg='red', fg='yellow',command=lambda: process(priceMILK))
bt4.place(x=50, y=150)


window.mainloop()
