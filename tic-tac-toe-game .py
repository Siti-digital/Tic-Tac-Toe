import tkinter
from tkinter import*
import random

root=Tk()
root.title("Tic Tac Toe Game")
root.configure(bg="darkgrey")
w,l,bot=False,False,"  "
x11,x12,x13,x21,x22,x23,x31,x32,x33=0,0,0,0,0,0,0,0,0
lis=[11,12,13,21,22,23,31,32,33]
lab3=Label(text='TIC-TAC-TOE',font=('algerian',15),background="lightblue").grid(row=1,pady=3,column=2)
lab4=Label(text=" GAME STARTED !! ",font=('arial',15),background="lightgreen").grid(row=2,pady=3,column=2,columnspan=2)

def result():
    global x11,x12,x13,x21,x22,x23,x31,x32,x33,w,l
    win,lose=(1,1,1),(2,2,2)
    combnatn=((x11,x12,x13),(x21,x22,x23),(x31,x32,x33),(x11,x21,x31),(x12,x22,x32),(x13,x23,x33),(x11,x22,x33),(x13,x22,x31))
    dummylist=(x11,x12,x13,x21,x22,x23,x31,x32,x33)
    for i in combnatn:
        if i==win:
            w=True
            lab4=Label(text="      YOU WON !!       ",font=('arial',15),background="lightgreen").grid(row=2,pady=3,column=2,columnspan=2)
            return None;break
#        elif i==lose:
#            l=True
#            lab4=Label(text="     YOU LOSE !!      ",font=('arial',15),background="lightgreen").grid(row=2,pady=3,column=2,columnspan=2)
#            return None;break
        elif (0 not in dummylist):
            lab4=Label(text="      GAME DRAW !!    ",font=('arial',15),background="lightgreen").grid(row=2,pady=3,column=2,columnspan=2)
    if w==False:
        for i in combnatn:
            if i==lose:
                l=True
                lab4=Label(text="     YOU LOSE !!      ",font=('arial',15),background="lightgreen").grid(row=2,pady=3,column=2,columnspan=2)
                return None;break

    
def working_alg():
    global x11,x12,x13,x21,x22,x23,x31,x32,x33,k11,k12,k13,k21,k22,k23,k31,k32,k33,lis
    if len(lis)==0:
        print(lis)
        print(x11,x12,x13,x21,x22,x23,x31,x32,x33)
        result()
        return None
    if (x11,x12,x13,x21,x22,x23,x31,x32,x33)==(1,0,0,0,0,0,0,0,0):
        x22=2;lis.remove(22)
        k22=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=4,column=2,ipadx=28,ipady=24)
    elif (x11,x12,x13,x21,x22,x23,x31,x32,x33)==(0,1,0,0,0,0,0,0,0):
        x22=2;lis.remove(22)
        k22=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=4,column=2,ipadx=28,ipady=24)
    elif (x11,x12,x13,x21,x22,x23,x31,x32,x33)==(0,0,1,0,0,0,0,0,0):
        x22=2;lis.remove(22)
        k22=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=4,column=2,ipadx=28,ipady=24)
    elif (x11,x12,x13,x21,x22,x23,x31,x32,x33)==(0,0,0,1,0,0,0,0,0):
        x22=2;lis.remove(22)
        k22=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=4,column=2,ipadx=28,ipady=24)
    elif (x11,x12,x13,x21,x22,x23,x31,x32,x33)==(0,0,0,0,0,1,0,0,0):
        x22=2;lis.remove(22)
        k22=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=4,column=2,ipadx=28,ipady=24)
    elif (x11,x12,x13,x21,x22,x23,x31,x32,x33)==(0,0,0,0,0,0,1,0,0):
        x22=2;lis.remove(22)
        k22=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=4,column=2,ipadx=28,ipady=24)
    elif (x11,x12,x13,x21,x22,x23,x31,x32,x33)==(0,0,0,0,0,0,0,1,0):
        x22=2;lis.remove(22)
        k22=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=4,column=2,ipadx=28,ipady=24)
    elif (x11,x12,x13,x21,x22,x23,x31,x32,x33)==(0,0,1,0,0,0,0,0,1):
        x22=2;lis.remove(22)
        k22=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=4,column=2,ipadx=28,ipady=24)
    elif (x11,x12,x13,x21,x22,x23,x31,x32,x33)==(0,0,0,0,1,0,0,0,0):
        demolis=list(lis)
        demolis.remove(12);demolis.remove(21);demolis.remove(23);demolis.remove(32)
        var=random.choice(demolis)
        if var==11:
            x11=2;lis.remove(11)
            k11=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=3,column=1,ipadx=28,ipady=24)
        elif var==13:
            x13=2;lis.remove(13)
            k13=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=3,column=3,ipadx=28,ipady=24)
        elif var==31:
            x31=2;lis.remove(31)
            k31=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=5,column=1,ipadx=28,ipady=24)
        elif var==33:
            x33=2;lis.remove(33)
            k33=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=5,column=3,ipadx=28,ipady=24)
    else:
        var=random.choice(lis)
        if var==11:
            x11=2;lis.remove(11)
            k11=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=3,column=1,ipadx=28,ipady=24)
        elif var==12:
            x12=2;lis.remove(12)
            k12=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=3,column=2,ipadx=28,ipady=24)
        elif var==13:
            x13=2;lis.remove(13)
            k13=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=3,column=3,ipadx=28,ipady=24)
        elif var==21:
            x21=2;lis.remove(21)
            k21=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=4,column=1,ipadx=28,ipady=24)
        elif var==22:
            x22=2;lis.remove(22)
            k22=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=4,column=2,ipadx=28,ipady=24)
        elif var==23:
            x23=2;lis.remove(23)
            k23=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=4,column=3,ipadx=28,ipady=24)
        elif var==31:
            x31=2;lis.remove(31)
            k31=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=5,column=1,ipadx=28,ipady=24)
        elif var==32:
            x32=2;lis.remove(32)
            k32=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=5,column=2,ipadx=28,ipady=24)
        elif var==33:
            x33=2;lis.remove(33)
            k33=Button(root,text='O',font=('algerian',25),bd=1,bg='white').grid(row=5,column=3,ipadx=28,ipady=24)
        result()

def k11f():
    global x11,k11,w,l,lis
    if (w,l)==(False,False):
        x11=1
        k11=Button(root,text='X',font=('algerian',25),bd=1,bg='white').grid(row=3,column=1,ipadx=28,ipady=24)
        lis.remove(11)
        working_alg()
def k12f():
    global x12,k12,w,l,lis
    if (w,l)==(False,False):
        x12=1
        k12=Button(root,text='X',font=('algerian',25),bd=1,bg='white').grid(row=3,column=2,ipadx=28,ipady=24)
        lis.remove(12)
        working_alg()
def k13f():
    global x13,k13,w,l,lis
    if (w,l)==(False,False):
        x13=1
        k13=Button(root,text='X',font=('algerian',25),bd=1,bg='white').grid(row=3,column=3,ipadx=28,ipady=24)
        lis.remove(13)
        working_alg()
def k21f():
    global x21,k21,w,l,lis
    if (w,l)==(False,False):
        x21=1
        k21=Button(root,text='X',font=('algerian',25),bd=1,bg='white').grid(row=4,column=1,ipadx=28,ipady=24)
        lis.remove(21)
        working_alg()
def k22f():
    global x22,k22,w,l,lis
    if (w,l)==(False,False):
        x22=1
        k22=Button(root,text='X',font=('algerian',25),bd=1,bg='white').grid(row=4,column=2,ipadx=28,ipady=24)
        lis.remove(22)
        working_alg()
def k23f():
    global x23,k23,w,l,lis
    if (w,l)==(False,False):
        x23=1
        k23=Button(root,text='X',font=('algerian',25),bd=1,bg='white').grid(row=4,column=3,ipadx=28,ipady=24)
        lis.remove(23)
        working_alg()
def k31f():
    global x31,k31,w,l,lis
    if (w,l)==(False,False):
        x31=1
        k31=Button(root,text='X',font=('algerian',25),bd=1,bg='white').grid(row=5,column=1,ipadx=28,ipady=24)
        lis.remove(31)
        working_alg()
def k32f():
    global x32,k32,w,l,lis
    if (w,l)==(False,False):
        x32=1
        k32=Button(root,text='X',font=('algerian',25),bd=1,bg='white').grid(row=5,column=2,ipadx=28,ipady=24)
        lis.remove(32)
        working_alg()
def k33f():
    global x33,k33,w,l,lis
    if (w,l)==(False,False):
        x33=1
        k33=Button(root,text='X',font=('algerian',25),bd=1,bg='white').grid(row=5,column=3,ipadx=28,ipady=24)
        lis.remove(33)
        working_alg()

def restart():
    global k11,k12,k13,k21,k22,k23,k31,k32,k33,x11,x12,x13,x21,x22,x23,x31,x32,x33,lis,w,l,lab4
    lab4=Label(text=" GAME STARTED !! ",font=('arial',15),background="lightgreen").grid(row=2,pady=3,column=2,columnspan=2)
    k11=Button(root,text=bot,font=('algerian',13),bd=1,bg='white',command=k11f).grid(row=3,column=1,ipadx=34,ipady=34)
    k12=Button(root,text=bot,font=('algerian',13),bd=1,bg='white',command=k12f).grid(row=3,column=2,ipadx=34,ipady=34)
    k13=Button(root,text=bot,font=('algerian',13),bd=1,bg='white',command=k13f).grid(row=3,column=3,ipadx=34,ipady=34,pady=5)
    k21=Button(root,text=bot,font=('algerian',13),bd=1,bg='white',command=k21f).grid(row=4,column=1,ipadx=34,ipady=34)
    k22=Button(root,text=bot,font=('algerian',13),bd=1,bg='white',command=k22f).grid(row=4,column=2,ipadx=34,ipady=34)
    k23=Button(root,text=bot,font=('algerian',13),bd=1,bg='white',command=k23f).grid(row=4,column=3,ipadx=34,ipady=34,pady=5)
    k31=Button(root,text=bot,font=('algerian',13),bd=1,bg='white',command=k31f).grid(row=5,column=1,ipadx=34,ipady=34)
    k32=Button(root,text=bot,font=('algerian',13),bd=1,bg='white',command=k32f).grid(row=5,column=2,ipadx=34,ipady=34)
    k33=Button(root,text=bot,font=('algerian',13),bd=1,bg='white',command=k33f).grid(row=5,column=3,ipadx=34,ipady=34,pady=5)
    x11,x12,x13,x21,x22,x23,x31,x32,x33=0,0,0,0,0,0,0,0,0
    lis,w,l=[11,12,13,21,22,23,31,32,33],False,False

restar=Button(root,text=' Restart ',font=('algerian',13),bd=5,bg='yellow',command=restart).grid(row=2,pady=20,padx=11,column=1)
restart()
lab5=Label(text="Developer:- Kunal Kashyap",font=('arial',12),background="darkgrey").grid(row=7,pady=3,column=1,columnspan=2)
lab6=Label(text="© Copyleft Reserved: KKtechnologies pvt.ltd",font=('arial',12),background="darkgrey").grid(row=8,pady=3,column=1,columnspan=7)
root.resizable(False,False)
root.geometry("365x560")
root.mainloop()
