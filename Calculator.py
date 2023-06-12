from functools import partial
from tkinter import messagebox
import re
from tkinter import *
root=Tk()
root.title("Calculator")
X=StringVar()
X.set('')
def string(Y):
    global X
    if X.get()=='0' and Y!='.':
        X.set('')
    X.set(X.get()+Y)
    print(X.get())
    A["text"]=X.get()
def evaluation():
    if X.get()=='':
        messagebox.showwarning("Warning","No Inputs")
    else:
        try:
            X.set(re.sub("[x]","*",X.get()))
            X.set(eval(X.get()))
            print(X.get())
            A["text"]="="+X.get()
        except ZeroDivisionError:
            X.set(re.sub("[*]","x",X.get()))
            messagebox.showerror("Error","Can't Divide By Zero")
        except SyntaxError:
            X.set(re.sub("[*]","x",X.get()))
            messagebox.showerror("Error","Wrong Inputs")
def percentage():
    try:
        X.set(float(X.get())/100)
        A["text"]=X.get()
    except ValueError:
        messagebox.showerror("Error","Wrong Inputs")
def empty():
    X.set('')
    A["text"]=X.get()
def backspace():
    X.set(X.get()[0:(len(X.get())-1)])
    A["text"]=X.get()
A=Label(root,text=X.get(),height=3,font=(10))
root.update()
A.grid(row=0,column=0,columnspan=4)
B=Button(root,text="AC",width=9,height=3,font=(10),fg="orange",bg="white",border=0,command=empty).grid(row=1,column=0)
W=PhotoImage(file="backspace.png")
C=Button(root,image=W,width=103,height=80,font=(10),fg="orange",bg="white",border=0,command=backspace).grid(row=1,column=1)
D=Button(root,text="%",width=9,height=3,font=(10),fg="orange",bg="white",border=0,command=percentage).grid(row=1,column=2)
E=Button(root,text="/",width=9,height=3,font=(10),fg="orange",bg="white",border=0,command=partial(string,"/")).grid(row=1,column=3)
F=Button(root,text="7",width=9,height=3,font=(10),bg="white",border=0,command=partial(string,"7")).grid(row=2,column=0)
G=Button(root,text="8",width=9,height=3,font=(10),bg="white",border=0,command=partial(string,"8")).grid(row=2,column=1)
H=Button(root,text="9",width=9,height=3,font=(10),bg="white",border=0,command=partial(string,"9")).grid(row=2,column=2)
I=Button(root,text="x",width=9,height=3,font=(10),fg="orange",bg="white",border=0,command=partial(string,"x")).grid(row=2,column=3)
J=Button(root,text="4",width=9,height=3,font=(10),bg="white",border=0,command=partial(string,"4")).grid(row=3,column=0)
K=Button(root,text="5",width=9,height=3,font=(10),bg="white",border=0,command=partial(string,"5")).grid(row=3,column=1)
L=Button(root,text="6",width=9,height=3,font=(10),bg="white",border=0,command=partial(string,"6")).grid(row=3,column=2)
M=Button(root,text="-",width=9,height=3,font=(10),fg="orange",bg="white",border=0,command=partial(string,"-")).grid(row=3,column=3)
N=Button(root,text="1",width=9,height=3,font=(10),bg="white",border=0,command=partial(string,"1")).grid(row=4,column=0)
O=Button(root,text="2",width=9,height=3,font=(10),bg="white",border=0,command=partial(string,"2")).grid(row=4,column=1)
P=Button(root,text="3",width=9,height=3,font=(10),bg="white",border=0,command=partial(string,"3")).grid(row=4,column=2)
Q=Button(root,text="+",width=9,height=3,font=(10),fg="orange",bg="white",border=0,command=partial(string,"+")).grid(row=4,column=3)
R=Button(root,text="0",width=9,height=3,font=(10),bg="white",border=0,command=partial(string,"0")).grid(row=5,column=1)
S=Button(root,text=".",width=9,height=3,font=(10),bg="white",border=0,command=partial(string,".")).grid(row=5,column=2)
V=PhotoImage(file="equalto.png")
T=Button(root,image=V,bg="white",border=0,width=102,height=80,command=evaluation).grid(row=5,column=3)
U=Button(root,text="",width=9,height=3,font=(10),bg="white",border=0).grid(row=5,column=0)

    
    
