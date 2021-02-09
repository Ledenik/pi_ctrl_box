import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font

import gpiozero

class CustomButton(ttk.Button):
    def __init__(self, parent, text, pin, function, *args, **kwargs):
        ttk.Button.__init__(self, text=text, *args, **kwargs)
        self.text = text
        self.pin = pin
        self.function = function

        #self.command = self.press(self.pin)

    def press(self, pin):
        print("Pressed" + str(self.pin))


class PWNButton(ttk.Button):
    def __init__(self, parent, text, pin, *args, **kwargs):
        ttk.Button.__init__(self, text=text, *args, **kwargs)
        self.text = text
        self.pin = pin
        #self.function = function
        self.func = gpiozero.PWMOutputDevice(pin=pin, active_high=True, initial_value=0, frequency=100)

    def press(self):
        print("press")
        func.toggle()
        print("after")

