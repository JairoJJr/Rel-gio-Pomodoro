from tkinter import *
from time import *
from . import estilo

class Tela:
    def __init__(self,root):
        root.title('Teste')
        root.geometry('600x320')
        root.configure(background= estilo.cor1)

class itens:
    def __init__(self,root):
        self.data = Label(root , bg = estilo.cor1 , fg = estilo.cor2 , font=estilo.fonte1)
        self.data.pack(pady=10)

        self.hora = Label(root , bg = estilo.cor1 , fg = estilo.cor2 , font = estilo.fonte2 )
        self.hora.pack()
        self.timer = Label(root , bg = estilo.cor1 , fg = estilo.cor2 , text = "00:00" , font=estilo.fonte3)
        self.timer.pack()
    
    def get_data(self):
        data_atual = strftime('%a, %d, %b, %Y')
        self.data.config(text=data_atual)

    def get_hora(self):
        hora_atual = strftime("%H:%M:%S")
        self.hora.config(text=hora_atual)
        self.hora.after(10,self.get_hora)
        
    
    
    

