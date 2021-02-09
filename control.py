import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font

from PIL import Image, ImageTk

from button import CustomButton, PWNButton

import gpiozero


c_box_values= [
    'GPIO0', 'GPIO1', 'GPIO2', 'GPIO3', 'GPIO4', 'GPIO5', 'GPIO6', 'GPIO7',
    'GPIO8', 'GPIO9', 'GPIO10', 'GPIO11', 'GPIO12', 'GPIO13', 'GPIO14',
    'GPIO15', 'GPIO16', 'GPIO17', 'GPIO18', 'GPIO19', 'GPIO20', 'GPIO21',
    'GPIO22', 'GPIO23', 'GPIO24', 'GPIO25', 'GPIO26', 'GPIO27',
]
pin_funcs = [
    ['SDA0',        'SA5',      'PCLK',         'SPI3_CE0_N',   'TXD2',         'SDA6'],        # 0
    ['SCL0',        'SA4',      'DE',           'SPI3_MISO',    'RXD2',         'SCL6'],        # 1
    ['SDA1',        'SA3',      'LCD_VSYNC',    'SPI3_MOSI',    'CTS2',         'SDA3'],        # 2
    ['SCL1',        'SA2',      'LCD_HSYNC',    'SPI3_SCLK',    'RTS2',         'SCL3'],        # 3
    ['GPCLK0',      'SA1',      'DPL_D0',       'SPI4_CE0_N',   'TXD3',         'SDA3'],        # 4
    ['GPCLK1',      'SA0',      'DPL_D1',       'SPI4_MISO',    'RXD3',         'SCL3'],        # 5
    ['GPCLK2',      'SOE_N',    'DPL_D2',       'SPI4_MOSI',    'CTS3',         'SDA4'],        # 6
    ['SPI0_CE1_N',  'SWE_N',    'DPL_D3',       'SPI4_SCLK',    'RTS3',         'SCL4'],        # 7
    ['SPI0_CE0_N',  'SD0',      'DPL_D4',       '-',            'TXD4',         'SDA4'],        # 8
    ['SPI0_MISO',   'SD1',      'DPL_D5',       '-',            'RXD4',         'SCL4'],        # 9
    ['SPI0_MOSI',   'SD2',      'DPL_D6',       '-',            'CTS4',         'SDA5'],        # 10
    ['SPI0_SCLK',   'SD3',      'DPL_D7',       '-',            'RTS4',         'SCL5'],        # 11
    ['PWM0',        'SD4',      'DPL_D8',       'SPI5_CE0_N',   'TXD5',         'SDA5'],        # 12
    ['PWN1',        'SD5',      'DPL_D9',       'SPI5_MISO',    'RXD5',         'SCL5'],        # 13
    ['TXD0',        'SD6',      'DPL_D10',      'SPI5_MOSI',    'CTS5',         'TXD1'],        # 14
    ['RXD0',        'SD7',      'DPL_D11',      'SPI5_SCLK',    'RTS5',         'RXD1'],        # 15
    ['FL0',         'SD8',      'DPL_D12',      'CTS0',         'SPI1_CE2_N',   'CTS1'],        # 16
    ['FL1',         'SD9',      'DPL_D13',      'RTS0',         'SPI1_CE1_N',   'RTS1'],        # 17
    ['PCM_CLK',     'SD10',     'DPL_D14',      'SPI6_CE0_N',   'SPI1_CE0_N',   'PWM0'],        # 18
    ['PCM_FS',      'SD11',     'DPL_D15',      'SPI6_MISO',    'SPI1_MISO',    'PWM1'],        # 19
    ['PCM_DIN',     'SD12',     'DPL_D16',      'SPI6_MOSI',    'SPI1_MOSI',    'GPCLK0'],      # 20
    ['PCM_DOUT',    'SD13',     'DPL_D17',      'SPI6_SCLK',    'SPI1_SCLK',    'GPCLK1'],      # 21
    ['SD0_CLK',     'SD14',     'DPL_D18',      'SD1_CLK',      'ARM_TRST',     'SDA6'],        # 22
    ['SD0_CMD',     'SD15',     'DPL_D19',      'SD1_CMD',      'ARM_RTCK',     'SCL6'],        # 23
    ['SD0_DAT0',    'SD16',     'DPL_D20',      'SD1_DAT0',     'ARM_TDO',      'SPI3_CE1_N'],  # 24
    ['SD0_DAT1',    'SD17',     'DPL_D21',      'SD1_DAT1',     'ARM_TCK',      'SPI4_CE1_N'],  # 25
    ['SD0_DAT2',    'TE0',      'DPL_D22',      'SD1_DAT2',     'ARM_TDI',      'SPI5_CE1_N'],  # 26
    ['SD0_DAT3',    'TE1',      'DPL_D23',      'SD1_DAT3',     'ARM_TMS',      'SPI6_CE1_N'],  # 27

]

class ControlView(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.frame = tk.Frame.__init__(self, parent)
        print("init")
        #self.controller = controller
        

        self.grid_columnconfigure(0, weight=1)
        #self.grid_rowconfigure(0, weight=1)

        self.button_list = []

        # LOGO
        logo = Image.open('images/hella_logo.png').resize((128, 76), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(logo)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=0, column=0, columnspan=2, sticky="w")

        add_button = ttk.Button(self, text="Add", command=self.show_popup)
        add_button.grid(row=0, column=3, sticky="e")

        

    def draw_buttons(self):
        for i, button in enumerate(self.button_list):
            button.grid(row=1, column=i)

    
    def show_popup(self):
        self.popup = tk.Toplevel()
        self.popup.wm_title("Add button")
        self.popup.geometry("400x300")

        label_text = ttk.Label(self.popup, text="Text:")
        label_text.grid(row=0, column=0)
        self.text = tk.Text(self.popup, height=2, width=30)
        self.text.grid(row=0, column=1)

        l = tk.Label(self.popup, text="Select PIN")
        l.grid(row=1, column=0)
        self.combo_box = ttk.Combobox(self.popup, values=c_box_values)
        self.combo_box.grid(row=1, column=1)

        alt_l = ttk.Label(self.popup, text = "Function")
        alt_l.grid(row=2, column=0)
        self.alt_box = ttk.Combobox(self.popup, values=pin_funcs, postcommand = lambda: self.update_cbox(self.combo_box.current()))
        self.alt_box.grid(row=2, column=1)

        b = ttk.Button(self.popup, text="Add", command=lambda: self.add_button(self.text.get("1.0", "end"), self.combo_box.current(), self.alt_box.current()))
        b.grid(row=3, column=1)

    def update_cbox(self, pin):
        self.alt_box['values'] = pin_funcs[pin]


    def add_button(self, text, pin, function):
        #new_btn = ttk.Button(self, text=text, command=lambda: self.btn_press(pin))
        new_btn = PWNButton(self, text=text, pin=pin, command=lambda: self.press)
        self.button_list.append(new_btn)
        self.popup.destroy()
        self.draw_buttons()


    def btn_press(self, pin):
        print("PRESS" + str(pin))


