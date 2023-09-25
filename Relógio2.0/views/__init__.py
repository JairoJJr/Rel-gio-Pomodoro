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
        #labels
        self.data = Label(root , bg = estilo.cor1 , fg = estilo.cor2 , font=estilo.fonte1)
        #self.data.pack(pady=10)

        self.hora = Label(root , bg = estilo.cor1 , fg = estilo.cor2 , font = estilo.fonte2 )
        self.hora.pack()
        
        self.timer = Label(root , bg = estilo.cor1 , fg = estilo.cor2 , text = "00:00" , font=estilo.fonte3)
        self.timer.pack()

        self.text_min = Label(root , bg = estilo.cor1 , fg = estilo.cor2 , text = "min" , font = estilo.fonte1)
        #self.text_min.place(x = 350 , y = 227)

        #botão
        #Função do botão
        def iniciar():
            print("ok")
        self.botao_start = Button(root, text = "Iniciar", bg = estilo.cor1, fg = estilo.cor2, command = iniciar)
        self.botao_start.pack()
    
        #Função para buscar data e hora local
        def get_data():
            data_atual = strftime('%a, %d, %b, %Y')
            self.data.config(text=data_atual)
        get_data()

        def get_hora():
            hora_atual = strftime("%H:%M:%S")
            self.hora.config(text=hora_atual)
            self.hora.after(10,get_hora)
        get_hora()


"""class count_down:
    def __init__(self,root)"""
