from tkinter import *
#root
root = Tk()
root.title("calculator")
# input box
e = Entry(root,borderwidth=3)
e.grid(row=0,column=0,columnspan=4)

def plus():
    first_num = e.get()
    e.delete(0,END)
    global fnum
    global op
    fnum = first_num
    op = "+"
def minus():
    first_num = e.get()
    e.delete(0,END)
    global fnum
    global op
    fnum = first_num
    op = "-"
def multiply():
    first_num = e.get()
    e.delete(0,END)
    global fnum
    global op
    fnum = first_num
    op = "*"
def divide():
    first_num = e.get()
    e.delete(0,END)
    global fnum
    global op
    fnum = first_num
    op = "/"
def equal():
    snum = e.get()
    e.delete(0,END)
    if op=="+":
        e.insert(0,int(fnum)+int(snum))
    if op=="-":
        e.insert(0,int(fnum)-int(snum))
    if op=="*":
        e.insert(0,int(fnum)*int(snum))
    if op=="/":
        e.insert(0,int(fnum)/int(snum))
def clear():
    e.delete(0,END)
#all buttons
button_1 = Button(root,text="1",padx=30,pady=40,command=lambda:text(1))
button_2 = Button(root,text="2",padx=30,pady=40,command=lambda:text(2))
button_3 = Button(root,text="3",padx=30,pady=40,command=lambda:text(3))
button_4 = Button(root,text="4",padx=30,pady=40,command=lambda:text(4))
button_5 = Button(root,text="5",padx=30,pady=40,command=lambda:text(5))
button_6 = Button(root,text="6",padx=30,pady=40,command=lambda:text(6))
button_7 = Button(root,text="7",padx=30,pady=40,command=lambda:text(7))
button_8 = Button(root,text="8",padx=30,pady=40,command=lambda:text(8))
button_9 = Button(root,text="9",padx=30,pady=40,command=lambda:text(9))
button_0 = Button(root,text="0",padx=30,pady=40,command=lambda:text(0))
button_plus = Button(root,text="+",padx=30,pady=40,command=plus)
button_equal = Button(root,text="=",padx=30,pady=40,command=equal)
button_clear = Button(root,text="clear",padx=20,pady=40,command=clear)
button_minus = Button(root,text="-",padx=30,pady=40,command=minus)
button_multiply = Button(root,text="*",padx=30,pady=40,command=multiply)
button_divide = Button(root,text="/",padx=30,pady=40,command=divide)
button_1.grid(row=3,column=1)
button_2.grid(row=3,column=2)
button_3.grid(row=1,column=0)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=3,column=0)
button_plus.grid(row=4,column=0)
button_equal.grid(row=4,column=1)
button_clear.grid(row=4,column=2)
button_minus.grid(row=5,column=0)
button_multiply.grid(row=5,column=1)
button_divide.grid(row=5,column=2)
def text(num):
    current = e.get()
    e.delete(0,END)
    e.insert(0,current+str(num))


root.mainloop()