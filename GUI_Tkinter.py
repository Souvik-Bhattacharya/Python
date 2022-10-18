# from tkinter import *
# import tkinter.messagebox as tmsg
# # from PIL import Image, ImageTk

# root = Tk()
# root.geometry("800x400")
# root.title("MY GUI BY SOUVIK")
# # root.wm_iconbitmap('icon.ico') # to set the favicon
# # root.config(bg = "yellow")
# screenwidth = root.winfo_screenwidth() # taking my system screen width
# screenheight = root.winfo_screenheight() # taking my system screen width
# print(screenwidth,'x',screenheight)

# # ww = 1200
# # wh = 500

# # root.geometry(f"{ww}x{wh}")
# # root.minsize(1200,500)
# # root.maxsize(1500,800)

# # # IMPORTANT LABEL OPTIONS
# # # text = for text
# # # bg = background
# # # fg = foreground
# # # font = fonts
# # # padx = x padding
# # # pady = y padding
# # # borderwidth
# # # relief = border styling = SUNKEN, RAISED, GROOVE, RIDGE

# # # IMPORTANT PACK OPTIONS
# # # anchor = "nw", "se"
# # # side
# # # fill
# # # padx
# # # pady

# # # lb = Label(text = "Hi! This is my GUI", bg = "green", fg = "yellow", padx = 45, pady = 45, font = ("comicsansms",20,"bold"), borderwidth = 5, relief = SUNKEN )
# # # lb.pack(side = TOP, fill = X, padx = 2,pady = 2)

# # # # for png files only
# # # photo1 = PhotoImage(file = "clipboard.png", width = 240, height = 240)
# # # lb_im1 = Label(image = photo1)
# # # lb_im1.pack()

# # # # for both png and jpg files
# # # image = Image.open("logo.png")
# # # photo2 = ImageTk.PhotoImage(image)
# # # lb_im2 = Label(image = photo2)
# # # lb_im2.pack()

# # def greet():
# #     print('Hello!')

# # # f1 = Frame(root,bg = "darkblue")
# # # f1.pack(side = 1TOP,fill = "x")

# # # l = Label(f1,text = "SAY! HELLO!",bg = "darkblue",fg = "goldenrod")
# # # l.pack(pady = 4,side = LEFT)

# # # b = Button(f1,bg = "red",fg = "white",text = "print",command = greet,padx = 5,pady = 5)
# # # b.pack(pady = 4,side = RIGHT)

# # # VARIABLE CLASSES IN TKINTER
# # # BooleanVar() , StringVar() , DoubleVar() , IntVar()

# # f2 = Frame(root,bg = "lightgreen",padx = 15,pady = 15)
# # f2.pack(side = LEFT, fill = "y")

# # Label(f2,text = "ENTER DATA",bg = "lightgreen",font = "bold",padx = 15,pady = 15).grid(row = 0,column = 1,padx = 5,pady = 5)

# # Label(f2,text = "Username : ",bg = "lightgreen",font = "bold").grid(row = 1,column = 0,padx = 5,pady = 5)
# # Label(f2,text = "Age : ",bg = "lightgreen",font = "bold").grid(row = 2,column = 0,padx = 5,pady = 5)

# # uval = StringVar()
# # aval = IntVar()
# # cval = IntVar()

# # Entry(f2,textvariable = uval).grid(row = 1,column = 1,pady = 15,padx = 15)
# # Entry(f2,textvariable = aval).grid(row = 2,column = 1,padx = 15,pady = 15)
# # Checkbutton(f2,text = "Are you confirmed?",font = "bold",variable = cval,bg = "lightgreen").grid(row = 3,column = 1,padx = 5,pady = 5)

# # def data():
# #     print(f"User name: {uval.get()}, Age: {aval.get()}, Confirmation: {cval.get()}\n")
# #     with open("record.txt","a") as f:
# #         f.write(f"User name: {uval.get()}, Age: {aval.get()}, Confirmation: {cval.get()}\n")
# #     uval.set("")
# #     aval.set(0)
# #     cval.set(0)
# #     with open("record.txt","r") as file:
# #         Texts = file.read()
# #     t.config(text = Texts)

# # Button(f2,bg = "red",fg = "white",text = "submit",command = data,padx = 5,pady = 5).grid(row = 4,column = 1,pady = 5,padx = 5)

# # f3 = Frame(root,bg = "lightgreen",padx = 15,pady = 15)
# # f3.pack(side = "right",fill = "y")

# # Label(f3,text = "MY DATA",bg = "lightgreen",font = "bold",padx = 15,pady = 15).pack(padx = 5,pady = 5)

# # with open("record.txt","r") as file:
# #     texts = file.read()

# # t = Label(f3,text = texts,bg = "lightgreen",padx = 5,pady = 5)
# # t.pack(padx = 5,pady = 5)

# # f4 = Frame(root,padx = 10,pady = 10,bg = "yellow")
# # f4.pack(anchor = "center",fill = "both")

# # # cv = Canvas(f3,width = 250,height = 250,bg = "lightgreen")
# # # cv.pack(side = "right")

# # # # photo = PhotoImage(file = "clipboard.png",width = 240,height = 240)
# # # # cv.create_image(125,125,image = photo)

# # # cv.create_oval(10,10,240,240,fill = "goldenrod")
# # # cv.create_text(125,125,text = "Hello!",fill = "darkgreen")

# # Label(f4,text = "Welcome! Here you can add your data!",bg = "yellow",fg = "darkblue",font = "bold",padx = 25,pady = 25).pack(padx = 4,pady = 4)

# # image = Image.open("logo.png")
# # image = image.resize((200,200),Image.ANTIALIAS)
# # photo = ImageTk.PhotoImage(image)
# # lb_im = Label(f4,image = photo)
# # lb_im.pack(padx = 4,pady = 4)

# # f5 = Frame(root,padx = 25,pady = 25,bg = "yellow")
# # f5.pack(fill = "both",padx = 10,pady = 10)

# # def change():
# #     a = input_x.get()
# #     b = input_y.get()
# #     return root.geometry(f"{a}x{b}")

# # Label(f5,text = "Width : ",bg = "yellow",font = "bold").pack(side = "left")

# # input_x = IntVar()
# # input_y = IntVar()

# # input_x.set(f"{ww}")
# # input_y.set(f"{wh}")

# # Entry(f5,textvariable=input_x).pack(side = "left")
# # Entry(f5,textvariable=input_y).pack(side = "right")

# # Label(f5,text = "Height : ",bg = "yellow",font = "bold").pack(side = "right")

# # f6 = Frame(root,padx = 15,pady = 9,bg = "yellow")
# # f6.pack(padx = 10,pady = 10)

# # Button(f6,bg = "red",text = "Resize",padx = 5,pady = 5,fg = "white", command=change).pack(side = "left",padx = 8)

# # def quit(event):
# #     root.destroy()

# # eb = Button(f6,bg = "red",text = "Exit from GUI",padx = 5,pady = 5,fg = "white")
# # eb.pack(side = "left",padx = 8)
# # eb.bind("<Button-1>",quit)

# # # LISTBOX

# # def add():
# #     global i
# #     l.insert('active',f'{i}')
# #     i += 1
# # i = 0

# # l = Listbox(root)
# # l.pack()
# # l.insert('anchor','HELLO!')
# # Button(root,text = 'Add',command = add,pady = 5).pack()

# def func():
#     print('Saved!')
    
# def Greet():
#     # print('Hello!')
#     will = tmsg.askquestion('Rate Us','Do you like our GUI?')
#     # print(will)
#     if will == 'yes':
#         tmsg.showinfo('Thanks','Rate us on playstore')
#     else:
#         er = tmsg.askretrycancel('Experience','Do you want to retry this GUI?')
#         if not er:
#             tmsg.showinfo('Trouble Shooting','We will give you a feedback form plz submit!')

# mymenu = Menu(root)

# m = Menu(mymenu,tearoff = 0)
# n = Menu(m,tearoff = 0)
# n.add_command(label = "print",command = func)
# n.add_separator()
# n.add_command(label = "rate us",command = Greet)
# m.add_cascade(label = "save as",menu = n)

# mymenu.add_cascade(label = "file",menu = m)
# root.config(menu = mymenu)

# def rate():
#     ms.set('Processing...')
#     stb.update()
#     with open('rating.txt','a') as f:
#         m = f'rating is {slide.get()} and gender is {var.get()}\n'
#         f.write(m)
#     tmsg.showinfo('Thanks',f'You have rate us {slide.get()} and your gender is {var.get()}')
#     ms.set('Thanks for visiting !')

# Label(root,text = 'Rate Us Now').pack()
# slide = Scale(root,from_ = 0, to = 10, orient = 'horizontal', tickinterval = 2)
# slide.set(5)
# slide.pack(padx = 8,pady = 8)

# rf = Frame(root)
# rf.pack()
# Label(rf,text = 'Select your gender :').pack(side = 'left')
# # var = IntVar()
# var = StringVar()
# var.set('abstract')
# Radiobutton(rf,text = 'Male',variable = var,value = 'Male').pack(side = 'left')
# Radiobutton(rf,text = 'Female',variable = var,value = 'Female').pack(side = 'left')
# Radiobutton(rf,text = 'Other',variable = var,value = 'Other').pack(side = 'left')

# Button(rf,text = 'Rate',command = rate).pack(side = 'left')

# sf = Frame(root)
# sf.pack(fill = 'both')
# sc = Scrollbar(sf)
# sc.pack(side = 'right',fill = 'y')
# ta = Text(sf,height = 10,yscrollcommand = sc.set)
# ta.pack(padx = 4,pady = 4,fill = 'both')
# sc.config(command = ta.yview)

# ms = StringVar()
# ms.set('Thanks for visiting !')
# stb = Label(root,textvariable = ms,font = 'bold',anchor = 'w',padx = 7,pady = 5)
# stb.pack(side = 'bottom',fill = 'x')

# root.mainloop()