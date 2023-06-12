from tkinter import *
root=Tk()
#root.geometry("250x250")
A=Canvas(root,width=250,height=200)
A.pack()
A.create_line(0,20,250,20,fill='green',dash=(5,15))
A.create_rectangle(100,40,150,90,fill='blue')
A.create_oval(115,100,135,120,fill='orange')
