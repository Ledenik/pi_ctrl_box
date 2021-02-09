import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import font as tkfont 

from PIL import Image, ImageTk

from configure import ConfigureView
from control import ControlView


class Application:
    def __init__(self, parent):
        self.root = parent
        self.frame = None
        self.refresh()
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.frame.pack(side="top", fill="both", expand=True)
        #self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

    def refresh(self):
        if self.frame is not None:
            self.frame.destroy()
            print("destroy")
        self.frame = ControlView(self.root)

        

        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.tkraise()
        print("news")
        


    # def __init__(self, *args, **kwargs):
    #     Tk.__init__(self, *args, **kwargs)

    #     self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
    #     self.geometry("800x600")
    #     # the container is where we'll stack a bunch of frames
    #     # on top of each other, then the one we want visible
    #     # will be raised above the others
    #     container = Frame(self)
    #     container.pack(side="top", fill="both", expand=True)
    #     container.grid_rowconfigure(0, weight=1)
    #     container.grid_columnconfigure(0, weight=1)

    #     self.frames = {}
    #     for F in (ControlView, ConfigureView):
    #         page_name = F.__name__
    #         frame = F(parent=container, controller=self)
    #         self.frames[page_name] = frame

    #         # put all of the pages in the same location;
    #         # the one on the top of the stacking order
    #         # will be the one that is visible.
    #         frame.grid(row=0, column=0, sticky="nsew")

    #     self.show_frame("ControlView")

    # def show_frame(self, page_name):
    #     '''Show a frame for the given page name'''
    #     frame = self.frames[page_name]
    #     frame.tkraise()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Control")
    root.geometry("800x600")
    app = Application(root)
    #controlbox = Application()
    root.mainloop()
