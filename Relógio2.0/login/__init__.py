import tkinter as tk
from tkinter import *
import usuario as user
import cores as cor


def logar():
    user.nome = nome.get()
    nome.destroy()
    root.destroy()


root = tk.Tk()
root.title('Cronômetro da Produtividade')
root.geometry('600x320')
root.maxsize(600,360)
root.minsize(600,360)
root.configure(background= cor.cor1)

nome = Entry(root, bg= cor.cor1,fg=cor.cor2, width=10, font= ("",55))
nome.pack(pady=50)

login = Button(root, text= 'Login', bg= cor.cor1, fg=cor.cor2, command = logar)
login.pack(pady=10)

root.mainloop()