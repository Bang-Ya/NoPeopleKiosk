from tkinter import *
import tkinter as tk
import threading
from playsound import playsound




# frame3 insert " - "
def getlabel(labelname,nowframe,xplace,yplace):
    labelname = Label(nowframe, relief="flat",text="-",font=("Times",30),background='White')
    labelname.place(x=xplace, y=yplace)


#버튼  선언 이미지의 파일명과 매칭을 위해 이름순서를 바꿔 조합하였음.
class btnderation:

    juminbtn = Button
    landbtn = Button
    comprevbtn = Button
    certbtn = Button
    comhomebtn = Button
    bothomebtn = Button
    botprevbtn = Button
    botokbtn = Button
    # set dial button Name 다이얼 버튼
    dialzero = Button
    # test.py에 하드 코딩 해뒀음  dialone=Button
    #dialone = Button
    dialtwo = Button
    dialthree = Button
    dialfour = Button
    dialfive = Button
    dialsix = Button
    dialseven = Button
    dialeight = Button
    dialnine = Button
    dialdel = Button
    dialmod = Button
    # consub7~
    selpublicbtn = Button
    selallbtn = Button
    selcourtbtn = Button
    seledubtn = Button
    selhostbtn = Button
    sellandbtn = Button
    selnonebtn = Button
    sub14ok1btn = Button
    sub14ok2btn = Button
    sub17cardbtn = Button
    sub17cashbtn = Button
    sub18cardbtn = Button
    subokbtn = Button
    boxselectbtn=Button
