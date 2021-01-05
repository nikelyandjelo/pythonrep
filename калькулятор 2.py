from tkinter import * 
def du():
    root.destroy()
def c1():
    root['bg']='red'
    root.geometry("400x350")
def c2():
    root['bg']='blue'
    root.geometry("500x450")
def c3():
    root['bg']='green'
    root.geometry("600x550")
def t1():
    e3.delete(0, END)
    a1=float(e1.get())
    a2=float(e2.get())
    s=a1+a2
    e3.insert(0,float(s))
def t2():
    e3.delete(0, END)
    a1=float(e1.get())
    a2=float(e2.get())
    s=a1-a2
    e3.insert(0,float(s))
def t3():
    e3.delete(0, END)
    a1=float(e1.get())
    a2=float(e2.get())
    s=a1*a2
    e3.insert(0,float(s))
def t4():
    e3.delete(0, END)
    a1=float(e1.get())
    a2=float(e2.get())
    s=a1/a2
    e3.insert(0,float(s))
root = Tk()
root.title("Калькулятор")
root.geometry("500x700")
mainmenu = Menu(root)  
nika=Menu()
kui=Menu()
nika.add_command(label="red",command=c1)
nika.add_command(label="blue",command=c2)
nika.add_command(label="green",command=c3)
kui.add_command(label="exit",command=du)
nika.add_separator()
mainmenu.add_cascade(label='Цветовая схема',menu=nika)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='Выход',menu=kui)
e1=Entry(justify=CENTER)
e1.pack()
e2=Entry(justify=CENTER)
e2.pack()
f_top = LabelFrame(root,text="Функции")
f_top.pack()
b1=Button(f_top,text="+",justify=CENTER,width=5,command=t1)
b2=Button(f_top,text="-",justify=CENTER,width=5,command=t2)
b3=Button(f_top,text="*",justify=CENTER,width=5,command=t3)
b4=Button(f_top,text="/",justify=CENTER,width=5,command=t4)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)
l1=Label(text="Результат")
l1.pack()
e3=Entry(justify=CENTER)
e3.pack()
root.mainloop()

