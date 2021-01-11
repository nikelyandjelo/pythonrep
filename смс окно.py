from tkinter import *
from tkinter import messagebox
root = Tk() 
e1 = Entry(width=50) 
def insert(): 
     e1.insert(0,"Tkinter - GUI ")
def display():
    messagebox.showinfo( 'первое окно сообщения',name_entry.get() ) 
b = Button(text="Вставить", command=insert)
root.title("GUI на Python") 
name_label = Label(text="Введите имя:") 
name_entry = Entry()
name_entry.insert(0, "Tom") 
button1 = Button(text="Display", command=display) 
name_label.pack() 
name_entry.pack()
button1.pack()  
e1.pack() 
b.pack()
root.mainloop()
