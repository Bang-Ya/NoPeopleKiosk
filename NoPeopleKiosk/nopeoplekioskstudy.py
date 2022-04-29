from tkinter import *
import tkinter as tk
from playsound import playsound
import threading
from imtest import btnderation as im
from imtest import *

soundtf = False

# show frame
def show_frame(frame):
    frame.tkraise()

# tkinter 기본세팅1
window=tk.Tk()
#전체화면 세팅
window.state('zoomed')
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)


count=0
price=10

#프레임 기본틀생성

frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame8,frame9,frame10,frame11,frame11_1,frame11_2,frame12,frame13,frame14,frame15,frame16,frame17,frame18,frame19,frame20,frame21,frame22,frame23,frame24=tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window),tk.Frame(window)

#프레임 사용을 위해 선언한 프레임 grid작업 반복
for frame in (frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame8,frame9,frame10,frame11,frame11_1,frame11_2,frame12,frame13,frame14,frame15,frame16,frame17,frame18,
              frame19,frame20,frame21,frame22,frame23,frame24):
    frame.grid(row=0,column=0,sticky='nsew')

# 전체화면 활성화 기분값==전체화면 F11+F12 입력시 창모드로 전환..
window.attributes("-fullscreen", True)
window.bind("<F11>"+"<F12>", lambda event: window.attributes("-fullscreen",
                                    not window.attributes("-fullscreen")))
window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))



#최초 기본 프레임 호출
show_frame(frame1)

#wall

#img 선언 작업 대부분 파일명과 동일하게 작업했다.
top = PhotoImage(file='img/img_top.png')
bot = PhotoImage(file='img/img_bot.png')
wall = PhotoImage(file = "img/con_main.png")
consub1=PhotoImage(file="img/con_sub1.png")
consub2=PhotoImage(file="img/con_sub2.png")
consub3=PhotoImage(file="img/con_sub3.png")
consub4=PhotoImage(file="img/con_sub4.png")
consub5=PhotoImage(file="img/con_sub5.png")
consub6=PhotoImage(file="img/con_sub6.png")
consub7=PhotoImage(file="img/con_sub7.png")
consub8=PhotoImage(file="img/con_sub8.png")
consub9=PhotoImage(file="img/con_sub9.png")
consub10=PhotoImage(file="img/con_sub10.png")
consub10_1=PhotoImage(file="img/con_sub10-1.png")
consub10_2=PhotoImage(file="img/con_sub10-2.png")
consub11=PhotoImage(file="img/con_sub11.png")
consub12=PhotoImage(file="img/con_sub12.png")
consub13=PhotoImage(file="img/con_sub13.png")
consub14=PhotoImage(file="img/con_sub14.png")
consub15=PhotoImage(file="img/con_sub15.png")
consub16=PhotoImage(file="img/con_sub16.png")
consub17=PhotoImage(file="img/con_sub17.png")
consub18=PhotoImage(file="img/con_sub18.png")
consub19=PhotoImage(file="img/con_sub19.png")
consub20=PhotoImage(file="img/con_sub20.png")
consub21=PhotoImage(file="img/con_sub21.png")
consub22=PhotoImage(file="img/con_sub22.png")
consub23=PhotoImage(file="img/con_sub23.png")
consub24=PhotoImage(file="img/con_sub24.png")
consub25=PhotoImage(file="img/con_sub25.png")
consub26=PhotoImage(file="img/con_sub26.png")
consub27=PhotoImage(file="img/con_sub27.png")
consub28=PhotoImage(file="img/con_sub28.png")
consub29=PhotoImage(file="img/con_sub29.png")

#버튼 이미지 선언
btn_jumin=PhotoImage(file="img/btn_jumin.png")
btn_land=PhotoImage(file="img/btn_land.png")
btn_cert=PhotoImage(file="img/btn_cert.png")
btn_prev=PhotoImage(file="img/btn_prev.png")
btn_home=PhotoImage(file="img/btn_home.png")
sub_btn_ok=PhotoImage(file="img/sub_btn_ok.png")
#bot버튼
bot_btn_ok=PhotoImage(file="img/bot_btn_ok.png")
bot_btn_home=PhotoImage(file="img/bot_btn_home.png")
bot_btn_prev=PhotoImage(file="img/bot_btn_prev.png")
bot_btn_hand=PhotoImage(file="img/bot_btn_hand.png")
#다이얼버튼
dial_0=PhotoImage(file="img/dial_0.png")
dial_1=PhotoImage(file="img/dial_1.png")
dial_2=PhotoImage(file="img/dial_2.png")
dial_3=PhotoImage(file="img/dial_3.png")
dial_4=PhotoImage(file="img/dial_4.png")
dial_5=PhotoImage(file="img/dial_5.png")
dial_6=PhotoImage(file="img/dial_6.png")
dial_7=PhotoImage(file="img/dial_7.png")
dial_8=PhotoImage(file="img/dial_8.png")
dial_9=PhotoImage(file="img/dial_9.png")
dial_del=PhotoImage(file="img/dial_del.png")
dial_mod=PhotoImage(file="img/dial_mod.png")
#consub7~
sel_brn_public=PhotoImage(file="img/sel_brn_public.png")
sel_btn_all=PhotoImage(file="img/sel_btn_all.png")
sel_btn_court=PhotoImage(file="img/sel_btn_court.png")
sel_btn_edu=PhotoImage(file="img/sel_btn_edu.png")
sel_btn_host=PhotoImage(file="img/sel_btn_host.png")
sel_btn_land=PhotoImage(file="img/sel_btn_land.png")
sel_btn_none=PhotoImage(file="img/sel_btn_none.png")
sub14_btn_ok1=PhotoImage(file="img/sub14_btn_ok1.png")
sub14_btn_ok2=PhotoImage(file="img/sub14_btn_ok2.png")
sub17_btn_card=PhotoImage(file="img/sub17_btn_card.png")
sub17_btn_cash=PhotoImage(file="img/sub17_btn_cash.png")
sub18_btn_card=PhotoImage(file="img/sub18_btn_card.png")


#버튼  선언 이미지의 파일명과 매칭을 위해 이름순서를 바꿔 조합하였음.


#추부 가격과 매수 계산을 위해 선언 함수에 사용됨

#sound 사용여부
#soundtf=True
#juminnumtest

jumininput=Label
# 초기 프레임 생성시 주민등록번호 입력창에 넣어놨던 리스트 추후 사용가능성이 있어보여 남겨둠.
#juminlst=['_','_','_','_','_','_','_','_','_','_','_','_','_']
# print(juminlst[0]+juminlst[1]+juminlst[2]+juminlst[3]+juminlst[4]+juminlst[5]+'-'+juminlst[6]+juminlst[7]+juminlst[8]+juminlst[9]+juminlst[10]+juminlst[11]+juminlst[12])

#juminent=Entry
#juminent2=Entry
#코드 줄이려고 테스트중


def placset2(name):
    return name.place


def setbackgroun(framenum, imagenm):
    top_label = Label(framenum, image=top)
    top_label.place(x=-2, y=-2)
    wall_label = Label(framenum, image=imagenm)
    wall_label.place(x=-2, y=646)
    bot_label = Label(framenum, image=bot)
    bot_label.place(x=-2, y=1457)



#=====================================================================================

# 프레임5에서 3초후 자동 프레임 전환을 하기 위함.
# genesis_function을 바로 사용하면 4-->5에도 동일한 타임의 딜레이가 발생하므로 패스하고
# 바로 a_function으로 사용하였음. 추후 비슷한 기능을 구현하기 위해 남겨둠.

def genesis_function(time):
    threading.Timer(time, function_a, [time]).start()

def function_a(time):
    show_frame(frame5)
    threading.Timer(time, function_b).start()

def function_b():
    deungaudio3()
    show_frame(frame7)




#================================================================================================================

def goframbtn(btnname,nowframe,imgname,nextframe,xplace,yplace):
    btnname = Button(nowframe, image=imgname, relief="flat", command=lambda: show_frame(nextframe))
    btnname.place(x=xplace, y=yplace)


def placebtn(btnname,nowframe,imgname,xplace,yplace):
    btnname = Button(nowframe, image=imgname, relief="flat")
    btnname.place(x=xplace, y=yplace)


# 주민등록 번호 입력시 6자를 초과하면 juminent2로 데이터를 입력시킴
def onClicknum(txt):
    if txt=="del":
        juminent.delete(0,END)
        juminent2.delete(0, END)

    elif txt=="mod":
        # 여기버튼 아직 해결못함. if문 반복해야하나?
        if len(juminent2.get()) >= 7:
            juminent2.delete(6,END)
        elif len(juminent2.get()) == 6:
            juminent2.delete(5, END)
        elif len(juminent2.get()) == 5:
            juminent2.delete(4, END)
        elif len(juminent2.get()) == 4:
            juminent2.delete(3, END)
        elif len(juminent2.get()) == 3:
            juminent2.delete(2, END)
        elif len(juminent2.get()) == 2:
            juminent2.delete(1, END)
        elif len(juminent2.get()) == 1:
            juminent2.delete(0, END)
        else:
            if len(juminent.get()) >= 6:
                juminent.delete(5, END)
            elif len(juminent.get()) == 5:
                juminent.delete(4, END)
            elif len(juminent.get()) == 4:
                juminent.delete(3, END)
            elif len(juminent.get()) == 3:
                juminent.delete(2, END)
            elif len(juminent.get()) == 2:
                juminent.delete(1, END)
            elif len(juminent.get()) == 1:
                juminent.delete(0, END)
    else:
        if len(juminent.get()) > 5:
            juminent2.insert(END, txt)
           #juminent2의 길이가 7이 되어야 버튼이 활성화 된다
           #juminent2의 길이가 6이하면 버튼 사라지게 처리하자..
            if len(juminent2.get()) > 6:
                #goframbtn(botokbtn, frame3, bot_btn_ok, frame4, 880, 1285)
                botokbtn = Button(frame3, image=bot_btn_ok, relief="flat", command=lambda: [show_frame(frame4),creatcallaudio(frame4,deungaudio2)])
                botokbtn.place(x=880, y=1285)
               # juminent.delete(0, END), juminent2.delete(0, END)
                #creatcallaudio(frame4,deungaudio2)
        else:
            juminent.insert(END, txt)

def onclicknumbtn(btnname,nowframe,imgname,text,xplace,yplace):
    btnname = Button(nowframe, image=imgname, relief="flat", command=lambda:onClicknum(text))
    btnname.place(x=xplace, y=yplace)

# to frame18
def incount(plus):
    count=plus
    eachmonytest = Label(frame18, width=6, font=("Times", 25), text=count, background='White')
    eachmonytest.place(x=500, y=890)
    return count
# to frame18
#매수,가격 함수
def insertcount(incount):
    global count
    count = incount
    return count
def insertprice(inprice):
    global price
    price = inprice
    return price
#===============frame16 다이얼처리====================================
def onClicknumframe16(txt):
    balgeub.insert(END, txt)
    global returntest, price
    if len(balgeub.get()) > 1:
        balgeub.delete(0, END)
        balgeub.insert(END, txt)
    if txt=="1":
        count=insertcount(1)
    elif txt=="2":
        count=insertcount(2)
    elif txt=="3":
        count=insertcount(3)
    elif txt=="4":
        count=insertcount(4)
    elif txt=="5":
        count=insertcount(5)
    elif txt=="6":
        count=insertcount(6)
    elif txt=="7":
        count=insertcount(7)
    elif txt=="8":
        count=insertcount(8)
    elif txt=="9":
        count=insertcount(9)
    return balgeub

def onclicknumbtn2(btnname,nowframe,imgname,text,xplace,yplace):
    btnname = Button(nowframe, image=imgname, relief="flat", command=lambda:onClicknumframe16(text))
    btnname.place(x=xplace, y=yplace)

#=============== frame16 다이얼처리 END ====================================



#sound 사용여부
def soundplaytest(filename):
    global soundtf
    if soundtf == True:
        playsound("D:\\pythonkshProject\\audio\\" + filename + ".mp3")
        print(soundtf)
    elif soundtf == False:
        print("soundtf is false")
    else:
        print ("soundtf ERROR")



#함수별 음성파일 지정
def deungaudio1():
    soundplaytest('02.등본_01')
def deungaudio2():
    soundplaytest('02.등본_02')
def deungaudio3():
    soundplaytest('02.등본_03')
def deungaudio4():
    soundplaytest('02.등본_04')
def deungaudio5():
    soundplaytest('02.등본_05')
def deungaudio6():
    soundplaytest('02.등본_06')
#===============  Jump to frame 17 ====================================
def a_function2(time):
    show_frame(frame17)
    threading.Timer(time, b_function2).start()
    framelabelresult()


def b_function2():
    global price
    if price == 200:
        show_frame(frame18)
    elif price == 0:
        show_frame(frame23)
    else:
        print('b_function2 err')
#===============  Jump to frame 17 END ====================================

def framelabelresult():
    global price, count
    balgeub4 = Label(frame18, width=6, font=("Times", 25), text=count, background='White')
    balgeub4.place(x=790, y=840)
    balgeub2 = Label(frame18, width=6, font=("Times", 30), text=price * count, background='White')
    balgeub2.place(x=740, y=984)
    # frame19
    balgeub3 = Label(frame19, width=6, font=("Times", 30), text=price * count, background='White')
    balgeub3.place(x=740, y=801)
    balgeub5 = Label(frame22, width=4, font=("Times", 30), text=price * count, background='White')
    balgeub5.place(x=407, y=918)
    #frame21
    #balgeub4 = Label(frame21, width=6, font=("Times", 30), text=text, background='White')
    #balgeub4.place(x=790, y=1184)

#===============  Jump to frame 17 END ====================================

#==================frame 18 choice card cash =================================
def onclickpayfree():
    global price
    price=insertprice(0)
    #paymoney='0'
    eachmony = Label(frame18, width=6, font=("Times", 25), text=price, background='White')
    eachmony.place(x=790, y=890)

def onclickpaymoney():
    global price
    price=insertprice(200)
    eachmony = Label(frame18, width=6, font=("Times", 25), text=price, background='White')
    eachmony.place(x=790, y=890)


#==================frame 18 choice card cash =================================
def a_function3(time):
    show_frame(frame21)
    threading.Timer(time, b_function3).start()

def b_function3():
    show_frame(frame22)
    threading.Timer(3, c_function3).start()
def c_function3():
    show_frame(frame23)




#프레임 이동 ---> 오디오 플레이를 위한 함수 최적화 생성중....

#선 프레임 이동 후 오디오 재생
def frameaudio(callaudio):
    show_frame(frame3)
    threading.Timer(0.3, callaudio).start()

def creatcallaudio(showframe,dename):
    show_frame(showframe)
    threading.Timer(0.3, dename).start()

# 후 오디오 플레이 작업 soundplaytest 에서 mp3형식으로 박아두었음. 파일명만 입력하면 됌.

#함수 끝=========함수 끝=========함수 끝=========함수 끝=========함수 끝=========


#프레임 찍어내기 시작
#찍어내기 시작 1~5 는 각구역에 최상단에 삽입되어있음
#setbackground를 통해 각프레임의 top, bot은 모두 동일한 이미지로 고정되어있고 가운데 wall라인을 각 프레임마다 다르게 세팅하여 사용.
setbackgroun(frame6,consub5)
setbackgroun(frame7,consub6)
setbackgroun(frame8,consub7)
setbackgroun(frame9,consub8)
setbackgroun(frame10,consub9)
setbackgroun(frame11,consub10)
setbackgroun(frame12,consub11)
setbackgroun(frame13,consub12)
setbackgroun(frame14,consub13)
setbackgroun(frame15,consub14)
setbackgroun(frame16,consub15)
setbackgroun(frame17,consub16)
setbackgroun(frame18,consub17)
setbackgroun(frame19,consub18)
setbackgroun(frame20,consub19)
setbackgroun(frame11_1,consub10_1)
setbackgroun(frame11_2,consub10_2)
setbackgroun(frame21,consub20)
setbackgroun(frame22,consub21)
setbackgroun(frame23,consub29)
setbackgroun(frame24,consub23)
#=======frame1===========frame1=========frame1==========frame1==========
#frame1 background
setbackgroun(frame1,wall)
#frame1_btn etc...
goframbtn(im.juminbtn,frame1,btn_jumin,frame2,80,760)
#goframbtn(landbtn,frame1,btn_land,frame2,310,760)
goframbtn(im.comprevbtn,frame1,btn_prev,frame23,30,30)
goframbtn(im.comhomebtn,frame1,btn_home,frame1,950,30)



#=======frame2===========frame2=========frame2==========frame2==========
#frame2 background
setbackgroun(frame2,consub1)
#frame2_btn etc...
#goframbtn(certbtn,frame2,btn_cert,frame3,390,860)
certbtn = Button(frame2, image=btn_cert, relief="flat", command=lambda: creatcallaudio(frame3,deungaudio1))
certbtn.place(x=390, y=860)
#goframbtn(abstbtn,frame2,btn_abst,frame3,390,1060) 초본 배경에 포함되어있으로 주석처리
goframbtn(im.comprevbtn,frame2,btn_prev,frame1,30,30)
goframbtn(im.comhomebtn,frame2,btn_home,frame1,950,30)
goframbtn(im.bothomebtn,frame2,bot_btn_home,frame1,75,1288)
goframbtn(im.botprevbtn,frame2,bot_btn_prev,frame1,201,1288)



#=======frame3============frame3==============frame3==============frame3========
#frame3 background
setbackgroun(frame3,consub2)
#frame3_btn etc...
goframbtn(im.comprevbtn,frame3,btn_prev,frame2,30,30)
goframbtn(im.comhomebtn,frame3,btn_home,frame1,950,30)
goframbtn(im.bothomebtn,frame3,bot_btn_home,frame1,75,1288)
goframbtn(im.botprevbtn,frame3,bot_btn_prev,frame2,201,1288)
# 주민번호 1,2 사이에 하이푼
getlabel(jumininput,frame3,502,800)

# 다이얼 버튼 클릭시 onclicknumbtn함수를 통해 값을 입력받음
juminent=Entry(frame3, width=6,font=("Times",30),show="*")
juminent.place(x=350,y=800)

juminent2=Entry(frame3, width=7,font=("Times",31),show="*")
juminent2.place(x=550,y=800)
#juminent.pack()

#frame3_dial btn
#onclicknumbtn 함수를 통해 값을 숫자값을 텍스트형태로 전달하여 후가공함.  추후 해당 함수 찾아 스코를을 줄이기 위해 1번버튼만 하드코딩해둠.
dialone = Button(frame3, image=dial_1, relief="flat", command=lambda: onClicknum(1))
dialone.place(x=590, y=890)
onclicknumbtn(im.dialtwo,frame3,dial_2,str(2),715,890)
onclicknumbtn(im.dialthree,frame3,dial_3,str(3),845,890)
onclicknumbtn(im.dialfour,frame3,dial_4,str(4),590,983)
onclicknumbtn(im.dialfive,frame3,dial_5,str(5),715,983)
onclicknumbtn(im.dialsix,frame3,dial_6,str(6),845,983)
onclicknumbtn(im.dialseven,frame3,dial_7,str(7),590,1073)
onclicknumbtn(im.dialeight,frame3,dial_8,str(8),715,1073)
onclicknumbtn(im.dialnine,frame3,dial_9,str(9),845,1073)
onclicknumbtn(im.dialzero,frame3,dial_0,str(0),715,1163)
onclicknumbtn(im.dialmod,frame3,dial_mod,str("mod"),845,1163)
onclicknumbtn(im.dialdel,frame3,dial_del,str("del"),590,1163)

#상단 임시 프레임 이동버튼 추후 삭제
frame3_title = tk.Label(frame3, text="This is frame 3", bg='blue')
frame3_title.pack(fill='x')
frame3_btn = tk.Button(frame3, text='enter', command=lambda: show_frame(frame4))
frame3_btn.pack()
#상단 임시 프레임 이동버튼 추후 삭제 END


#===========frame4============================================
#frame4 background
setbackgroun(frame4,consub3)
#frame4_btn etc...
goframbtn(im.comprevbtn,frame4,btn_prev,frame3,30,30)
goframbtn(im.comhomebtn,frame4,btn_home,frame1,950,30)
goframbtn(im.bothomebtn,frame4,bot_btn_home,frame1,75,1288)
goframbtn(im.botprevbtn,frame4,bot_btn_prev,frame3,201,1288)

frame4_title = tk.Label(frame4, text="This is frame 4", bg='green')
frame4_title.pack(fill='x')
frame4_btn = tk.Button(frame4, text='enter', command=lambda: function_a(1)) #show_frame(frame5))
frame4_btn.pack()


#===========frame5============================================
#frame5 background
setbackgroun(frame5,consub4)

#frame5_btn etc...
goframbtn(im.comprevbtn,frame5,btn_prev,frame4,30,30)
goframbtn(im.comhomebtn,frame5,btn_home,frame1,950,30)

#상단 임시 프레임 이동버튼 추후 삭제
frame5_title = tk.Label(frame5, text="This is frame 5", bg='green')
frame5_title.pack(fill='x')
frame5_btn = tk.Button(frame5, text='enter',command=lambda:show_frame(frame6))
frame5_btn.pack()
#상단 임시 프레임 이동버튼 추후 삭제 END


#프레임별 버튼 박아두기.
goframbtn(im.botokbtn,frame6,bot_btn_ok,frame7,880,1285)
"""
goframbtn(botokbtn,frame8,bot_btn_ok,frame9,880,1285)
goframbtn(botokbtn,frame9,bot_btn_ok,frame10,880,1285)
goframbtn(botokbtn,frame10,bot_btn_ok,frame11,880,1285)
goframbtn(botokbtn,frame11,bot_btn_ok,frame12,880,1285)
goframbtn(botokbtn,frame12,bot_btn_ok,frame13,880,1285)
goframbtn(botokbtn,frame13,bot_btn_ok,frame14,880,1285)
goframbtn(botokbtn,frame14,bot_btn_ok,frame15,880,1285)
goframbtn(botokbtn,frame15,bot_btn_ok,frame16,880,1285)
goframbtn(botokbtn,frame16,bot_btn_ok,frame17,880,1285)
goframbtn(botokbtn,frame17,bot_btn_ok,frame18,880,1285)
goframbtn(botokbtn,frame18,bot_btn_ok,frame19,880,1285)
goframbtn(botokbtn,frame19,bot_btn_ok,frame20,880,1285)
goframbtn(botokbtn,frame20,bot_btn_ok,frame1,880,1285)
"""

#===========frame7============================================



goframbtn(im.comprevbtn,frame7,btn_prev,frame3,30,30)
goframbtn(im.comhomebtn,frame7,btn_home,frame1,950,30)
#goframbtn(botokbtn,frame7,bot_btn_ok,frame15,880,1285)
goframbtn(im.selcourtbtn,frame7,sel_btn_court,frame8,29,770)
goframbtn(im.seledubtn,frame7,sel_btn_edu,frame9,29,865)
goframbtn(im.selpublicbtn,frame7,sel_brn_public,frame10,29,960)
goframbtn(im.sellandbtn,frame7,sel_btn_land,frame11,29,1055)
goframbtn(im.selhostbtn,frame7,sel_btn_host,frame12,29,1150)
goframbtn(im.selallbtn,frame7,sel_btn_all,frame11_1,700,715)
goframbtn(im.selnonebtn,frame7,sel_btn_none,frame11_2,880,715)
goframbtn(im.bothomebtn,frame7,bot_btn_home,frame1,75,1288)
goframbtn(im.botprevbtn,frame7,bot_btn_prev,frame4,201,1288)


#===========frame8============================================

goframbtn(im.comprevbtn,frame8,btn_prev,frame7,30,30)
goframbtn(im.comhomebtn,frame8,btn_home,frame1,950,30)
goframbtn(im.botokbtn,frame8,bot_btn_ok,frame15,880,1285)
#goframbtn(selcourtbtn,frame8,sel_btn_court,frame8,29,770)
goframbtn(im.seledubtn,frame8,sel_btn_edu,frame9,29,865)
goframbtn(im.selpublicbtn,frame8,sel_brn_public,frame10,29,960)
goframbtn(im.sellandbtn,frame8,sel_btn_land,frame11,29,1055)
goframbtn(im.selhostbtn,frame8,sel_btn_host,frame12,29,1150)
goframbtn(im.selallbtn,frame8,sel_btn_all,frame11_1,700,715)
goframbtn(im.selnonebtn,frame8,sel_btn_none,frame11_2,880,715)
goframbtn(im.bothomebtn,frame8,bot_btn_home,frame1,75,1288)

#===========frame9============================================

goframbtn(im.comprevbtn,frame9,btn_prev,frame7,30,30)
goframbtn(im.comhomebtn,frame9,btn_home,frame1,950,30)
goframbtn(im.botokbtn,frame9,bot_btn_ok,frame15,880,1285)
goframbtn(im.selcourtbtn,frame9,sel_btn_court,frame8,29,770)
#goframbtn(seledubtn,frame9,sel_btn_edu,frame9,29,865)
goframbtn(im.selpublicbtn,frame9,sel_brn_public,frame10,29,960)
goframbtn(im.sellandbtn,frame9,sel_btn_land,frame11,29,1055)
goframbtn(im.selhostbtn,frame9,sel_btn_host,frame12,29,1150)
goframbtn(im.selallbtn,frame9,sel_btn_all,frame11_1,700,715)
goframbtn(im.selnonebtn,frame9,sel_btn_none,frame11_2,880,715)
goframbtn(im.bothomebtn,frame9,bot_btn_home,frame1,75,1288)

#===========frame10============================================

goframbtn(im.comprevbtn,frame10,btn_prev,frame7,30,30)
goframbtn(im.comhomebtn,frame10,btn_home,frame1,950,30)
goframbtn(im.botokbtn,frame10,bot_btn_ok,frame15,880,1285)
goframbtn(im.selcourtbtn,frame10,sel_btn_court,frame8,29,770)
goframbtn(im.seledubtn,frame10,sel_btn_edu,frame9,29,865)
#goframbtn(selpublicbtn,frame10,sel_brn_public,frame10,29,960)
goframbtn(im.sellandbtn,frame10,sel_btn_land,frame11,29,1055)
goframbtn(im.selhostbtn,frame10,sel_btn_host,frame12,29,1150)
goframbtn(im.selallbtn,frame10,sel_btn_all,frame11_1,700,715)
goframbtn(im.selnonebtn,frame10,sel_btn_none,frame11_2,880,715)
goframbtn(im.bothomebtn,frame10,bot_btn_home,frame1,75,1288)


#===========frame11============================================

goframbtn(im.comprevbtn,frame11,btn_prev,frame7,30,30)
goframbtn(im.comhomebtn,frame11,btn_home,frame1,950,30)
goframbtn(im.botokbtn,frame11,bot_btn_ok,frame15,880,1285)
goframbtn(im.selcourtbtn,frame11,sel_btn_court,frame8,29,770)
goframbtn(im.seledubtn,frame11,sel_btn_edu,frame9,29,865)
goframbtn(im.selpublicbtn,frame11,sel_brn_public,frame10,29,960)
#goframbtn(sellandbtn,frame11,sel_btn_land,frame11,29,1055)
goframbtn(im.selhostbtn,frame11,sel_btn_host,frame12,29,1150)
goframbtn(im.selallbtn,frame11,sel_btn_all,frame11_1,700,715)
goframbtn(im.selnonebtn,frame11,sel_btn_none,frame11_2,880,715)
goframbtn(im.bothomebtn,frame11,bot_btn_home,frame1,75,1288)

#===========frame12============================================
goframbtn(im.botokbtn,frame12,bot_btn_ok,frame15,880,1285)


"""
goframbtn(selcourtbtn,frame12,sel_btn_court,frame8,29,770)
goframbtn(seledubtn,frame12,sel_btn_edu,frame9,29,865)
goframbtn(selpublicbtn,frame12,sel_brn_public,frame10,29,960)
goframbtn(sellandbtn,frame12,sel_btn_land,frame11,29,1055)
#goframbtn(selhostbtn,frame12,sel_btn_host,frame12,29,1150)
goframbtn(selallbtn,frame12,sel_btn_all,frame11_1,700,715)
goframbtn(selnonebtn,frame12,sel_btn_none,frame11_2,880,715)
"""
#===========frame11_1============================================

goframbtn(im.botokbtn,frame11_1,bot_btn_ok,frame15,880,1285)
goframbtn(im.selcourtbtn,frame11_1,sel_btn_court,frame8,29,770)
goframbtn(im.seledubtn,frame11_1,sel_btn_edu,frame9,29,865)
goframbtn(im.selpublicbtn,frame11_1,sel_brn_public,frame10,29,960)
goframbtn(im.sellandbtn,frame11_1,sel_btn_land,frame11,29,1055)
goframbtn(im.selhostbtn,frame11_1,sel_btn_host,frame12,29,1150)
#goframbtn(selallbtn,frame11_1,sel_btn_all,frame11_1,700,715)
goframbtn(im.selnonebtn,frame11_1,sel_btn_none,frame11_2,880,715)
goframbtn(im.bothomebtn,frame11_1,bot_btn_home,frame1,75,1288)

#===========frame11_2============================================

goframbtn(im.botokbtn,frame11_2,bot_btn_ok,frame15,880,1285)
goframbtn(im.selcourtbtn,frame11_2,sel_btn_court,frame8,29,770)
goframbtn(im.seledubtn,frame11_2,sel_btn_edu,frame9,29,865)
goframbtn(im.selpublicbtn,frame11_2,sel_brn_public,frame10,29,960)
goframbtn(im.sellandbtn,frame11_2,sel_btn_land,frame11,29,1055)
goframbtn(im.selhostbtn,frame11_2,sel_btn_host,frame12,29,1150)
goframbtn(im.selallbtn,frame11_2,sel_btn_all,frame11_1,700,715)
goframbtn(im.bothomebtn,frame11_2,bot_btn_home,frame1,75,1288)


#goframbtn(selnonebtn,frame11_2,sel_btn_none,frame11_2,880,715)



#=================frame15=================
goframbtn(im.botokbtn,frame15,bot_btn_ok,frame16,880,1285)
#goframbtn(sub14ok1btn,frame15,sub14_btn_ok1,frame16,100,1085)
#goframbtn(sub14ok2btn,frame15,sub14_btn_ok2,frame16,570,1085)
goframbtn(im.bothomebtn,frame15,bot_btn_home,frame1,75,1288)
goframbtn(im.botprevbtn,frame15,bot_btn_prev,frame11_2,201,1288)

paymoney = Button(frame15, image=sub14_btn_ok1, relief="flat", command=lambda: [show_frame(frame16),onclickpayfree() ])
paymoney.place(x=100, y=1085)

free = Button(frame15, image=sub14_btn_ok2, relief="flat", command=lambda: [show_frame(frame16),onclickpaymoney() ])
free.place(x=570, y=1085)
#=================frame16=================
#goframbtn(botokbtn,frame16,bot_btn_ok,frame17,880,1285)

balgeub=Entry(frame16, width=6,font=("Times",30))
balgeub.place(x=300,y=903)

#dial

onclicknumbtn2(dialone,frame16,dial_1,str(1),580,880)
onclicknumbtn2(im.dialtwo,frame16,dial_2,str(2),707,880)
onclicknumbtn2(im.dialthree,frame16,dial_3,str(3),835,880)
onclicknumbtn2(im.dialfour,frame16,dial_4,str(4),580,971)
onclicknumbtn2(im.dialfive,frame16,dial_5,str(5),707,971)
onclicknumbtn2(im.dialsix,frame16,dial_6,str(6),835,971)
onclicknumbtn2(im.dialseven,frame16,dial_7,str(7),580,1063)
onclicknumbtn2(im.dialeight,frame16,dial_8,str(8),707,1063)
onclicknumbtn2(im.dialnine,frame16,dial_9,str(9),835,1063)

goframbtn(im.bothomebtn,frame16,bot_btn_home,frame1,75,1288)
goframbtn(im.botprevbtn,frame16,bot_btn_prev,frame15,201,1288)

botokbtn = Button(frame16, image=bot_btn_ok, relief="flat", command=lambda:a_function2(3))
botokbtn.place(x=880, y=1285)


#=================frame17=================
#goframbtn(botokbtn,frame17,bot_btn_ok,frame18,880,1285)

#=================frame18=================
goframbtn(im.botokbtn,frame18,bot_btn_ok,frame19,880,1285)
goframbtn(im.sub17cardbtn,frame18,sub17_btn_card,frame19,115,1090)
#goframbtn(sub17cashbtn,frame18,sub17_btn_cash,frame21,560,1090)
goframbtn(im.bothomebtn,frame18,bot_btn_home,frame1,75,1288)
goframbtn(im.botprevbtn,frame18,bot_btn_prev,frame16,201,1288)


#=================frame19=================
goframbtn(im.botokbtn,frame19,bot_btn_ok,frame20,880,1285)
goframbtn(im.sub18cardbtn,frame19,sub18_btn_card,frame20,115,950)
goframbtn(im.bothomebtn,frame19,bot_btn_home,frame1,75,1288)
goframbtn(im.botprevbtn,frame19,bot_btn_prev,frame18,201,1288)


#=================frame20=================
#goframbtn(botokbtn,frame20,bot_btn_ok,frame21,880,1285)
botokbtn = Button(frame20, image=bot_btn_ok, relief="flat", command=lambda:a_function3(3))
botokbtn.place(x=880, y=1285)
#=================frame21=================
#goframbtn(botokbtn,frame21,bot_btn_ok,frame22,880,1285)

#=================frame22=================
#goframbtn(botokbtn,frame22,bot_btn_ok,frame23,880,1285)

#================= LAST frame23 ================
goframbtn(im.subokbtn,frame23,sub_btn_ok,frame1,880,1285)

frame6_title = tk.Label(frame6, text="This is frame 6", bg='green')
frame6_title.pack(fill='x')
frame6_btn = tk.Button(frame6, text='enter',command=lambda:show_frame(frame7))
frame6_btn.pack()

frame7_title = tk.Label(frame7, text="This is frame 7", bg='green')
frame7_title.pack(fill='x')
frame7_btn = tk.Button(frame7, text='enter',command=lambda:show_frame(frame8))
frame7_btn.pack()

frame8_title = tk.Label(frame8, text="This is frame 8", bg='green')
frame8_title.pack(fill='x')
frame8_btn = tk.Button(frame8, text='enter',command=lambda:show_frame(frame9))
frame8_btn.pack()

frame9_title = tk.Label(frame9, text="This is frame 8", bg='green')
frame9_title.pack(fill='x')
frame9_btn = tk.Button(frame9, text='enter',command=lambda:show_frame(frame1))
frame9_btn.pack()


#finish
window.mainloop()