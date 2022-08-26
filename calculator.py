from tkinter import*
def btnclick(number):
    global val
    val=val+str(number)
    data.set(val)
def btnClear():
    global val
    val=""
    data.set("")
def btnEqual():
    global val
    result=str(eval(val))
    data.set(result)
root=Tk()
root.title("my calculator")
# root.geometry("700x400")
val=""
data=StringVar()
dispaly=Entry(root,textvariable=data,justify="right",bd=8,bg="pink",font=("roman 30 bold")).grid(row=0,columnspan=6)
b1=Button(root,text="1",command=lambda:btnclick(1),bd=8,font=("roman 30 bold"),bg="pink").grid(row=1,column=1)
b2=Button(root,text="2",command=lambda:btnclick(2),bd=8,font=("roman 30 bold"),bg="yellow").grid(row=2,column=1)
b3=Button(root,text="3",command=lambda:btnclick(3),bd=8,font=("roman 30 bold"),bg="red").grid(row=3,column=1)
b4=Button(root,text="4",command=lambda:btnclick(4),bd=8,font=("roman 30 bold"),bg="green").grid(row=4,column=1)
b5=Button(root,text="5",command=lambda:btnclick(5),bd=8,font=("roman 30 bold"),bg="pink").grid(row=5,column=1)
b6=Button(root,text="6",command=lambda:btnclick(6),bd=8,font=("roman 30 bold"),bg="yellow").grid(row=1,column=2)
b7=Button(root,text="7",command=lambda:btnclick(7),bd=8,font=("roman 30 bold"),bg="red").grid(row=2,column=2)
b8=Button(root,text="8",command=lambda:btnclick(8),bd=8,font=("roman 30 bold"),bg="green").grid(row=3,column=2)
b9=Button(root,text="9",command=lambda:btnclick(9),bd=8,font=("roman 30 bold"),bg="pink").grid(row=4,column=2)
b10=Button(root,text="0",command=lambda:btnclick(0),bd=8,font=("roman 30 bold"),bg="yellow").grid(row=5,column=2)
b11=Button(root,text="+",command=lambda:btnclick("+"),bd=8,font=("roman 30 bold"),bg="red").grid(row=1,column=3)
b12=Button(root,text="-",command=lambda:btnclick("-"),bd=8,font=("roman 30 bold"),bg="green").grid(row=2,column=3)
b1=Button(root,text="*",command=lambda:btnclick("*"),bd=8,font=("roman 30 bold"),bg="pink").grid(row=3,column=3)
b1=Button(root,text="%",command=lambda:btnclick("%"),bd=8,font=("roman 30 bold"),bg="white").grid(row=4,column=3)
b1=Button(root,text="/",command=lambda:btnclick("/"),bd=8,font=("roman 30 bold"),bg="yellow").grid(row=5,column=3)
b1=Button(root,text="//",command=lambda:btnclick("//"),bd=8,font=("roman 30 bold"),bg="red").grid(row=2,column=4)
btn_Clear=Button(root,text="clear",font=("roman 30 italic"),bd=8,command=btnClear).grid(row=3,column=4)
btnEqual=Button(root,text="=",font=("roman 30 italic"),bd=8,command=btnEqual).grid(row=4,column=4)
root.mainloop()





from tkinter import*
win=Tk()
win.geometry("500x250")
root=Label(win,text="my first application",font=("bold 30 underline"))
root.pack()
win.mainloop()


