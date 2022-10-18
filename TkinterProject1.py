# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:58:04 2022

@author: Souvik Bhattacharya
"""

from tkinter import *
from PIL import Image
from PIL import ImageTk

# print('Hello')

root = Tk()
root.title("MY GUI BY SOUVIK")
root.config(bg = "yellow")

ww = 1200
wh = 500

root.geometry(f"{ww}x{wh}")
# root.geometry("1200x500")
root.minsize(1200,500)
root.maxsize(1500,800)

f2 = Frame(root,bg = "lightgreen",padx = 15,pady = 15)
f2.pack(side = LEFT, fill = "y")

Label(f2,text = "ENTER DATA",bg = "lightgreen",font = "bold",padx = 15,pady = 15).grid(row = 0,column = 1,padx = 5,pady = 5)

Label(f2,text = "Username : ",bg = "lightgreen",font = "bold").grid(row = 1,column = 0,padx = 5,pady = 5)
Label(f2,text = "Age : ",bg = "lightgreen",font = "bold").grid(row = 2,column = 0,padx = 5,pady = 5)

uval = StringVar()
aval = IntVar()
cval = IntVar()

Entry(f2,textvariable = uval).grid(row = 1,column = 1,pady = 15,padx = 15)
Entry(f2,textvariable = aval).grid(row = 2,column = 1,padx = 15,pady = 15)
Checkbutton(f2,text = "Are you confirmed?",font = "bold",variable = cval,bg = "lightgreen").grid(row = 3,column = 1,padx = 5,pady = 5)

def data():
    print(f"User name: {uval.get()}, Age: {aval.get()}, Confirmation: {cval.get()}\n")
    with open("record.txt","a") as f:
        f.write(f"User name: {uval.get()}, Age: {aval.get()}, Confirmation: {cval.get()}\n")
    uval.set("")
    aval.set(0)
    cval.set(0)
    with open("record.txt","r") as file:
        Texts = file.read()
    t.config(text = Texts)

Button(f2,bg = "red",fg = "white",text = "submit",command = data,padx = 5,pady = 5).grid(row = 4,column = 1,pady = 5,padx = 5)

f3 = Frame(root,bg = "lightgreen",padx = 15,pady = 15)
f3.pack(side = "right",fill = "y")

Label(f3,text = "MY DATA",bg = "lightgreen",font = "bold",padx = 15,pady = 15).pack(padx = 5,pady = 5)

with open("record.txt","r") as file:
    texts = file.read()

t = Label(f3,text = texts,bg = "lightgreen",padx = 5,pady = 5)
t.pack(padx = 5,pady = 5)

f4 = Frame(root,padx = 10,pady = 10,bg = "yellow")
f4.pack(anchor = "center",fill = "both")

Label(f4,text = "Welcome! Here you can add your data!",bg = "yellow",fg = "darkblue",font = "bold",padx = 25,pady = 25).pack(padx = 4,pady = 4)

image = Image.open("logo.png")
image = image.resize((200,200),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
lb_im = Label(f4,image = photo)
lb_im.pack(padx = 4,pady = 4)

f5 = Frame(root,padx = 25,pady = 25,bg = "yellow")
f5.pack(fill = "both",padx = 10,pady = 10)

Label(f5,text = "Width : ",bg = "yellow",font = "bold").pack(side = "left")

input_x = IntVar()
input_y = IntVar()

input_x.set(f"{ww}")
input_y.set(f"{wh}")

Entry(f5,textvariable=input_x).pack(side = "left")
Entry(f5,textvariable=input_y).pack(side = "right")

Label(f5,text = "Height : ",bg = "yellow",font = "bold").pack(side = "right")

f6 = Frame(root,padx = 15,pady = 9,bg = "yellow")
f6.pack(padx = 10,pady = 10)

def change():
    a = input_x.get()
    b = input_y.get()
    return root.geometry(f"{a}x{b}")

Button(f6,bg = "red",text = "Resize",padx = 5,pady = 5,fg = "white", command=change).pack(side = "left",padx = 8)

def quit(event):
    root.destroy()

eb = Button(f6,bg = "red",text = "Exit from GUI",padx = 5,pady = 5,fg = "white")
eb.pack(side = "left",padx = 8)
eb.bind("<Button-1>",quit)

root.mainloop()