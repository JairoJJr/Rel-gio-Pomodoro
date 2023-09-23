from tkinter import *
#import cores as cor
import Tela
from time import *

def get_data():
    data_atual = strftime('%a, %d, %b, %Y')
    Tela.data.config(text=data_atual)

def get_hora():
    hora_atual = strftime("%H:%M:%S")
    Tela.hora.config(text=hora_atual)
    Tela.hora.after(10,get_hora)
    
