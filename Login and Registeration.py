import re
from tkinter import *
from tkinter import messagebox
def a():
    messagebox.showerror("Error","Invalid Login")
def d():
    messagebox.showinfo("Redirecting.....","Successfully Logged In")
    page.destroy()
def f():
    messagebox.showerror("Error","Invalid Email Id")
def h():
    messagebox.showinfo("","Email Already Registered")
def i():
    messagebox.showwarning("Warning","Passwords Do Not Match")
def j():
    messagebox.showwarning("Warning","Password should contain atleast one capital letter,digit,a small letter")
def c():
    J=F.get()
    K=H.get()
    print(J)
    print(K)
    with open("LoginDetails.csv","r") as f:
        f.seek(0)
        X=f.read()
        Z=re.split(r'[,\n]',X)
        print(Z)
        if J not in Z:
            a()
            F.delete(0,END)
            H.delete(0,END)
        elif K!=Z[Z.index(J)+1]:
            a()
            F.delete(0,END)
            H.delete(0,END)
        elif K=='':
            a()
            F.delete(0,END)
            H.delete(0,END)
        elif J=='':
            a()
            F.delete(0,END)
            H.delete(0,END)
        else:d()
            
def b():
    root.destroy()
    global page
    page=Tk()
    page.title("Login Page")
    page.geometry("300x250")
    D=Label(page,text="Please enter details below to login")
    D.pack(side=TOP)
    E=Label(page,text='Username')
    E.place(x=120,y=50)
    global F
    F=Entry(page,width=30)
    F.place(x=60,y=70)
    G=Label(page,text='Password')
    G.place(x=120,y=110)
    global H
    H=Entry(page,show='*',width=30)
    H.place(x=60,y=130)
    I=Button(page,text='Login',command=c)
    I.pack(side=BOTTOM)
def g():
    T=N.get()
    U=Q.get()
    V=S.get()
    print(T)
    with open("LoginDetails.csv","a+") as file:
        file.seek(0)
        Y=file.read()
        print(Y)
        Z=re.split(r'[,\n]',Y)
        if re.search("[\ba-z][\w.]*[a-z]@[\w]+[.][\w.]*[a-z\b]",T)==None:
            f()
        elif T=='':
            f()
        elif T in Z:
            h()
        elif U!=V:
            i()
        elif re.search("[A-Z]",U)==None or re.search("[a-z]",U)==None or re.search("[0-9]",U)==None:
            j()
        else:
            W=T+","+U
            file.write("\n"+W)
            messagebox.showinfo("Thank You","Your Account Has Been Registered")
            page2.destroy()
def e():
    root.destroy()
    global page2
    page2=Tk()
    page2.title("Registeration Page")
    #page2.geometry("300x400")
    L=Label(page2,text="Registeration Page",font='25',fg='red').grid(row=0,column=0,pady=(10,20),padx=70)
    M=Label(page2,text="Enter Email : ").grid(row=1,column=0)
    global N
    N=Entry(page2,width=30)
    N.grid(row=2,column=0,pady=(0,20))
    P=Label(page2,text="Enter Password : ").grid(row=4,column=0)
    global Q
    Q=Entry(page2,show='*',width=30)
    Q.grid(row=5,column=0,pady=(0,20))
    R=Label(page2,text="Re-Enter Password : ").grid(row=6,column=0)
    global S
    S=Entry(page2,show='*',width=30)
    S.grid(row=7,column=0,pady=(0,40))
    O=Button(page2,text="Submit",command=g).grid(row=8,column=0,pady=(0,10))
root=Tk()
root.title("Account Login")
root.geometry("300x250")
A=Label(root,text="Welcome! Please Login",bg='pink',height=3,width=100)
A.pack(side=TOP)
B=Button(root,text="Login",width=20,command=b)
B.place(x=75,y=80)
C=Button(root,text="Register",width=20,command=e)
C.place(x=75,y=130)

        



