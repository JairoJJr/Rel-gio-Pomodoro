import tkinter as tk
from tkinter import *
import os
from time import *
import collors as cor
import itens


root = tk.Tk()
root.title('Cronômetro da Produtividade')
root.geometry('600x320')
root.maxsize(600,360)
root.minsize(600,360)
root.configure(background= cor.cor1)

data = Label( root, bg = cor.cor1, fg = 'snow')
data.pack(pady=10)

itens.get_data()



root.mainloop()
