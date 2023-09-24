from tkinter import *
from time import *
from . import cores as cor

class Tela:
    def __init__(self,root):
        root.title('Teste')
        root.geometry('600x320')
        root.configure(background= cor.cor1)

class itens:
    def __init__(self,root):
        self.data = Label(root , bg = cor.cor1 , fg = cor.cor2 )
        self.data.pack(pady=10)

        self.hora = Label(root , bg = cor.cor1 , fg = cor.cor2 , font =("",30) )
        self.hora.pack()
    
    def get_data(self):
        data_atual = strftime('%a, %d, %b, %Y')
        self.data.config(text=data_atual)

    def get_hora(self):
        hora_atual = strftime("%H:%M:%S")
        self.hora.config(text=hora_atual)
        self.hora.after(10,self.get_hora)
        
    
    
    

