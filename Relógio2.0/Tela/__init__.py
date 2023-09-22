import tkinter as tk
from tkinter import *
import os
from time import *


root = tk.Tk()
root.title('Pomodore Chronomer')
root.geometry('600x320')
root.maxsize(600,360)
root.minsize(600,360)
root.configure(background= '#1d1d1d')

def get_data():
    data_atual = strftime('%a, %d, %b, $Y')
    data.config(text=data_atual)

data = Label( root, bg = '#1d1d1d' , fg = 'snow')
data.pack(pady=10)

root.mainloop()
