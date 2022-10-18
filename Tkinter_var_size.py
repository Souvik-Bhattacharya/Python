# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 18:45:39 2022

@author: Souvik Bhattacharya
"""

from tkinter import *

root = Tk()
root.geometry("500x400")

def change():
    a = input_x.get()
    b = input_y.get()
    return root.geometry(f"{a}x{b}")

input_x = IntVar()
input_y = IntVar()

x = Entry(root,textvariable=input_x)
y = Entry(root,textvariable=input_y)

x.pack()
y.pack()

Button(root, text="click for magic", command=change).pack()

root.mainloop()