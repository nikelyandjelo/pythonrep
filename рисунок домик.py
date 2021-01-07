from tkinter import * 
root = Tk() 
canv = Canvas(root, width=800, height=600, bg='white') 
canv.pack()
canv.create_rectangle(200,300,600,600,fill="white",outline="black")
canv.create_polygon([200,300],[400,150],[600,300],outline="black",fill='white')
canv.create_polygon([480,160],[520,160],[520,240],[480,210],outline="black",fill='white')
canv.create_oval(360, 180,440,260, width=2) 
canv.create_rectangle(300,400,500,500,fill="aqua",outline="black")
canv.create_line(400,400,400,500)
canv.create_line(300,450,500,450)
canv.create_text(100,100, text="Домик",fill='red',  
                justify=CENTER, font="Verdana 14") 
root.mainloop()
