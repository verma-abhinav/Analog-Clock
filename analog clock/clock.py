from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import PIL
import time
from math import *

class clock:

    def __init__(self,root):

        self.root=root
        self.root.title("Analog Clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        title = Label(self.root, text="Analog Clock", font=("Times New Roman", 50, "bold"), bg="#04444a", fg="white").place(x=0,y=50,relwidth=1)

        self.lbl=Label(self.root,bg='white',bd=20,relief=RAISED)
        self.lbl.place(x=450,y=150,height=400,width=400)

        #self.clock_image()
        self.working()


    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw=ImageDraw.Draw(clock)
        bg=Image.open('clock.png')
        bg =bg.resize((350,300),Image.ANTIALIAS)
        clock.paste(bg,(30,50))


        origin=200,200
        #==========hour line
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill='green',width=4)
        # ==========hour line
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill='blue',width=3)
        # ==========hour line
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill='red',width=4)
        # ==========hour eclipse
        draw.ellipse((195,192,210,210),fill='black')

        clock.save('clock_new.jpg')


    def working(self):

        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        self.clock_image(hr,min_,sec_)
        self.im=PIL.Image.open('clock_new.jpg')
        self.img=ImageTk.PhotoImage(self.im)
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

root=Tk()
obj=clock(root)
root.mainloop()