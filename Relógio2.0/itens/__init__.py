from tkinter import *
import collors as cor
import Tela
from time import *

def get_data():
    data_atual = strftime('%a, %d, %b, %Y')
    Tela.data.config(text=data_atual)


    
