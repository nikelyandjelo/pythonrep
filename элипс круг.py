from tkinter import * 
root = Tk() 
c = Canvas(root, width=700, height=500, bg='white') 
c.pack() 

c.create_oval(50, 50, 180, 170, width=2,fill='green',outline='white') 
c.create_oval(300, 50, 500, 170, fill='pink', outline='white')
c.create_text(120, 15, text="Круг",  
                justify=CENTER,font="calibri 14",fill='red')
c.create_text(400, 15, text="Эллипс",font="calibri 14",  
                justify=CENTER,fill='blue') 



root.mainloop() 
