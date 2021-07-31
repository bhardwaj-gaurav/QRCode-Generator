import os
from tkinter import *

import numpy as numpy
from PIL import ImageTk, Image
import qrcode
from pathlib import Path

root= Tk()
root.geometry('950x390')
clrs = ['misty rose', 'LemonChiffon2', 'peach puff', 'burlywood1', 'DarkSeaGreen2', 'bisque', 'papaya whip',
        'seashell2']
# ['misty rose','LemonChiffon2','peach puff','burlywood1','DarkSeaGreen2','bisque','papaya whip','seashell2']
# ['star','fleur','heart','pirate','shuttle','spider','man','cross','cirle','target','trek']

color = numpy.random.choice(clrs)

print(color)
root.config(bg=color, cursor="dot green")
l0 = Label( root, text="QR CODE GENERATOR", relief=FLAT,bg=color, font=('Tempus Sans ITC',32, 'bold'), fg="black")
l = Label( root, text="Enter URL", bg=color, relief=FLAT)
bg = Label( root, bg='white', relief=FLAT,width=42, height=19)
t=Text(root, height=2,width=52)


def cQr():
    global img
    inputValue=t.get("1.0","end-1c")
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, border=2, box_size=20)
    qr.add_data(inputValue)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("xy.png")
    image = Image.open('xy.png')
    image=image.resize((300,300), Image.ANTIALIAS)
    images = ImageTk.PhotoImage(image)
    global l1
    l1 = Label(image=images)
    l1.image = images
    l1.place(x=600,y=26)
    b["state"] = DISABLED
    b1["state"] = NORMAL

def dQr():
    img.save(str(os.path.join(Path.home(), "Downloads","Qrcode.png")))

def RQr():
    l1.place_forget()
    t.delete("1.0", "end")
    b["state"] = NORMAL
    b1["state"] = DISABLED

b=Button(root,text="Create QR Code",bg=color,activebackground=color,command=cQr)
b0=Button(root,text="Reset",bg=color,activebackground=color, command=RQr)
b1=Button(root,text="Download QR Code",bg=color,activebackground=color,command=dQr)
b1["state"] = DISABLED

b.place(x=200,y=300)
b0.place(x=350,y=300)
b1.place(x=690,y=355)

bg.place(x=600,y=26)
l0.place(x=10,y=50)
l.place(x=10,y=200)
t.place(x=100,y=200)

root.mainloop()
