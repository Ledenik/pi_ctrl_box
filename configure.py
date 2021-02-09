import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font

from PIL import Image, ImageTk

class ConfigureView(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)

        label = ttk.Label(self, text="This is a very important configure message.")
        label.place(relx=0.5, rely=0.3, anchor='center')