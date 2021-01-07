from tkinter import * 

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
def du():
    root.destroy()
def c1():
    root['bg']='#F08080'
    root.geometry("500x700")
    f_top['bg']='#F08080'
    e1['bg']='#F08080'
    e2['bg']='#F08080'
    e3['bg']='#F08080'
    l1['bg']='#F08080'
    b1['bg']='#F08080'
    b2['bg']='#F08080'
    b3['bg']='#F08080'
    b4['bg']='#F08080'
def c2():
    root['bg']='#FFA500'
    root.geometry("500x700")
    f_top['bg']='#FFA500'
    e1['bg']='#FFA500'
    e2['bg']='#FFA500'
    e3['bg']='#FFA500'
    l1['bg']='#FFA500'
    b1['bg']='#FFA500'
    b2['bg']='#FFA500'
    b3['bg']='#FFA500'
    b4['bg']='#FFA500'
def c3():
    root['bg']='#00FFFF'
    root.geometry("500x700")
    f_top['bg']='#00FFFF'
    l1['bg']='#00FFFF'
    e1['bg']='#00FFFF'
    e3['bg']='#00FFFF'
    e2['bg']='#00FFFF'
    b1['bg']='#00FFFF'
    b2['bg']='#00FFFF'
    b3['bg']='#00FFFF'
    b4['bg']='#00FFFF'
root = Tk()
root.geometry("500x700")
mainmenu = Menu(root)  
color_menu=Menu()  
color_menu.add_command(label="светло-коралловый",command=c1) 
color_menu.add_command(label="оранжевый",command=c2) 
color_menu.add_command(label="синий",command=c3) 
color_menu.add_separator() 
mainmenu.add_cascade(label='Цветовая схема', menu=color_menu) 
mainmenu.add_cascade(label="Выход",command=du) 
root.config(menu=mainmenu) 
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
