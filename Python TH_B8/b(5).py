from tkinter import *
window=Tk()
window.title("giao dien")
window.geometry('300x300')
a=Label(window,text="adc")
a.place(x=120,y=100)
def ShowChoice():
    a.configure(text="lll")
def clicked():
    a.configure(text="hjk")
def chot():
    a.configure(text="ck")
b=Button(window,text="cv",command=ShowChoice)
b.place(x=125,y=130)
c=Button(window,text="bk",command=clicked)
c.place(x=120,y=160)
d=Button(window,text="hk",command=chot)
d.place(x=123,y=190)
