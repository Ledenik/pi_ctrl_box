from tkinter import *
from tkinter.ttk import *
from tkinter.font import Font

from PIL import Image, ImageTk

class Logo():
    def __init__(self):
        super().__init__()

        logo = Image.open('images/hella_logo.png')
        logo = logo.resize((128, 76), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(logo, size="128x76")
        img = Label(self, image=render)
        img.image = render