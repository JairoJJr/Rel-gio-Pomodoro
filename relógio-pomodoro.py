import tkinter as tk
from tkinter import *
import os
from time import *

#CONFIGURAÇÕES DA JANELA

root = tk.Tk()
root.title('Pomodore Chronometer')
root.geometry('600x320')
root.maxsize(600,360)
root.minsize(600,360)
root.configure(background= '#1d1d1d')

#FUNÇÕES

#Data
def get_data():        
    data_atual = strftime('%a, %d, %b, %Y')
    data.config(text=data_atual)
    
#Relógio
def get_hora():
    hora_atual = strftime("%H:%M:%S")
    hora.config(text=hora_atual)
    hora.after(10,get_hora)

#Botão + início do timer
def iniciar():
    text_min.place(x = 500)
    print(session_time.get())
    tempo_timer = int(session_time.get())
    tempo_texto.destroy()
    session_time.destroy()
    botao_start.destroy()
    def count_down():
        session.pack()
        sec = tempo_timer*60
        while sec > -1:
            timer["text"] = sec//60,":",sec % 60
            sec -= 1 
            timer.pack()   
            root.update()
            sleep(1)
#Timer da pausa
    def breaktime():
        breakk.pack()
        sec = tempo_timer*12
        while sec > -1:
            timer["text"] = sec//60,":",sec % 60
            sec -= 1
            timer.pack()   
            root.update()
            sleep(1) 

#Chamando funções dentro da função botão (arrumar depois pra ficar mais otimizado)   
    count_down()
    session["text"] = " "
    breaktime()
    breakk["text"] = " "
    session["text"] = "SESSION 2"
    count_down()
    session["text"] = " "
    breakk["text"] = "BREAK 2"
    breaktime()
    breakk["text"] = " "
    session["text"] = "SESSION 3"
    count_down()
    session["text"] = " "
    breakk["text"] = "BREAK 3"
    breaktime()
    breakk["text"] = ""
    session["text"] = "SESSION 4"
    count_down()
    session["text"] = " "
    breakk["text"] = "BREAK 4"
    breaktime()
    breakk["text"] = ""
    session["text"] = "FIM"

#LABELS

data = Label(root , bg = '#1d1d1d' , fg = 'snow' )
data.pack(pady=10)

hora = Label(root , bg ="#1d1d1d" , fg = "snow" , font =("",30) )
hora.pack()

tempo_texto = Label(root , text = "Digite o tempo da sessão:" , bg = '#1d1d1d' , fg = 'snow' , font = (" ", 18))
tempo_texto.pack(pady=10)

session_time = Entry(root, bg = '#1d1d1d' , fg = 'snow', width=10 , font = ("",55))
session_time.place(x = 250 , y = 150, width = 100 , height = 100)

botao_start = Button(root , text= "Iniciar" , bg = "#1d1d1d" , fg = 'snow', command=iniciar)
botao_start.place(x = 266 , y = 260)

timer = Label(root , bg = "#1d1d1d" , fg = 'snow' , text = "00:00" , font=(" ", 100))

session = Label(root , bg = "#1d1d1d" , fg = 'green', text = "SESSION 1" )

breakk = Label(root , bg = "#1d1d1d" , fg = "red" , text = "BREAK 1")

text_min = Label(root , bg = "#1d1d1d" , fg = "snow" , text = "min" , font = (" " , 16))
text_min.place(x = 350 , y = 227)


#CHAMANDO FUNÇÕES
get_data()
get_hora()


root.mainloop()
