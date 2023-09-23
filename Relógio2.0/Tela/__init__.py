import tkinter as tk
from tkinter import *
import os
from time import *
import cores as cor
import itens
import usuario as user

#Configurações da Janela
root = tk.Tk()
root.title('Cronômetro da Produtividade')
root.geometry('600x320')
root.maxsize(600,360)
root.minsize(600,360)
root.configure(background= cor.cor1)

#Labels
data = Label(root, bg= cor.cor1, fg= cor.cor2)
data.pack(pady=10)

hora = Label(root, bg= cor.cor1, fg= cor.cor2, font= ("",30))
hora.pack(pady=10)

texto_ola = Label(root, text= f'Olá {user.nome}!', bg= cor.cor1, fg= cor.cor2, )
texto_ola.pack(pady=10)

itens.get_data()
itens.get_hora()

root.mainloop()
