from tkinter import *  
from tkinter import filedialog as fd
def extractText():  
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
    ("HTML files", "*.html;*.htm"),("All files", "*.*") ))
    f=open(file_name)  
    s=text.get(1.0, END)  
    f.write(s)  
    f.close()
def insertText():  
    file_name = fd.askopenfilename()  
    f = open(file_name)  
    s=f.read()  
    text.insert( 1.0,s)  
    f.close()   

root = Tk()
mainmenu = Menu(root)  
menu=Menu()
menu.add_command(label="открыть",command=insertText)
menu.add_command(label="сохранить",command=extractText)
mainmenu.add_cascade(label='опции',menu=menu)
root.config(menu=mainmenu)
text = Text(width=100, height=50) 
text.pack() 
root.mainloop()
