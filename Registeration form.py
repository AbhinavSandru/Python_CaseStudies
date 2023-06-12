from tkinter import *
from tkinter import messagebox
import re
def a():
    if M["state"]==DISABLED:
        M["state"]=NORMAL
        M["bg"]="brown"
        M["fg"]="white"
    else:
        M["state"]=DISABLED
        M["bg"]="lightgrey"
        M["fg"]="black"
def c():
    messagebox.showerror("Error","Invalid Email")
def d():
    messagebox.showerror("Error","Invalid Phone Number")
def b():
    N=C.get()
    O=E.get()
    P=key.get()
    Q=I.get()
    R=K.get()
    with open("StudentDetails.csv","a+") as file:
        file.seek(0)
        X=file.read()
        Z=re.split("[,\n]",X)
        if N=='':
            messagebox.showwarning("MissingDetails","Enter Fullname")
        elif O=='':
            c()
        elif re.search("[\ba-z][\w.]*[a-z]@[\w]+[.][\w.]*[a-z\b]",O)==None:
            c()
            E.delete(0,END)
        elif O in Z:
            messagebox.showinfo("Redirecting...","Student Already Registered")
            E.delete(0,END)
        elif P=='':
            messagebox.showwarning("Warning","Select Gender")
        elif Q=='':
            messagebox.showwarning("MissingDetails","Enter Age")
        elif R=='':
            d()
        elif re.search(r"[7-9][0-9]{9}",R)==None:
            d()
            K.delete(0,END)
        else:
            Y=N+","+O+","+P+","+Q+","+R
            file.write("\n"+Y)
            messagebox.showinfo("Success","Student Has Been Successfully Registered")
            root.destroy()
root=Tk()
root.title("New Members Page")
A=Label(root,text="Registration Form",font=25).grid(row=0,column=0,columnspan=3,pady=(50,30),padx=150)
B=Label(root,text="Full Name :").grid(row=1,column=0,pady=(0,15),padx=(40,0))
C=Entry(root,width=25)
C.grid(row=1,column=1,columnspan=2,pady=(0,15),padx=(0,40))
D=Label(root,text="Email :").grid(row=2,column=0,pady=(0,15),padx=(40,0))
E=Entry(root,width=25)
E.grid(row=2,column=1,columnspan=2,pady=(0,15),padx=(0,40))
F=Label(root,text="Gender :").grid(row=3,column=0,pady=(0,15),padx=(40,0))
key=StringVar()
G1=Radiobutton(root,text="Male",variable=key,value="Male",tristatevalue=0).grid(row=3,column=1,pady=(0,15),padx=(20,0))
G2=Radiobutton(root,text="Female",variable=key,value="Female",tristatevalue=0).grid(row=3,column=2,pady=(0,15),padx=(0,65))
H=Label(root,text="Age :").grid(row=4,column=0,pady=(0,15),padx=(40,0))
I=Entry(root,width=25)
I.grid(row=4,column=1,columnspan=2,pady=(0,15),padx=(0,40))
J=Label(root,text="Phone Number :").grid(row=5,column=0,pady=(0,15),padx=(40,0))
K=Entry(root,width=25)
K.grid(row=5,column=1,columnspan=2,pady=(0,15),padx=(0,40))
L=Checkbutton(root,text="Terms and Conditions",command=a)
L.grid(row=6,column=0,columnspan=2,pady=(30,0))
M=Button(root,text="Submit",width=20,bg="lightgrey",fg="black",state=DISABLED,command=b)
M.grid(row=7,column=0,columnspan=3,pady=(30,50))




