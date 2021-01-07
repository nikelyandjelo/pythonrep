from tkinter import * 
root = Tk() 
c = Canvas(root, width=200, height=200, bg='white') 
c.pack() 
c.create_line(10, 10, 200, 10) 
c.create_line(100, 180, 100, 60, fill='green',width=5,arrow=FIRST, dash=(10,2), activefill='lightgreen') 
root.mainloop() 
