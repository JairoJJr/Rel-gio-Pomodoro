from tkinter import *
from time import *

class Tela:
    def __init__(self,root):
        root.title('Teste')
        root.geometry('600x320')
        root.configure(background= '#1d1d1d')

class itens:
    def __init__(self,root):
        self.data = Label(root , bg = '#1d1d1d' , fg = 'snow' )
        self.data.pack(pady=10)

        self.hora = Label(root , bg ="#1d1d1d" , fg = "snow" , font =("",30) )
        self.hora.pack()
    
    def get_data(self):
        data_atual = strftime('%a, %d, %b, %Y')
        self.data.config(text=data_atual)

    def get_hora(self):
        hora_atual = strftime("%H:%M:%S")
        self.hora.config(text=hora_atual)
        #itens.hora.after(10,get_hora)
        
    
    
    

