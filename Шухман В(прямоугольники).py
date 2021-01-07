from tkinter import *
from random import randint
root = Tk() 
canv = Canvas(root, width=1000, height=700, bg='white')
canv.pack()
color=['red','green','blue','black','yellow','brown','grey','pink','violet']
def dz(event):
        n=randint(1,len(color))
        c=color[n-1]
        weight=randint(10,100)
        height=randint(10,100)
        x=event.x
        y=event.y
        rect=canv.create_rectangle(x,y,x+weight,y+height,fill=c,outline="white")
        
canv.bind('<Button-1>',dz)

root.mainloop

