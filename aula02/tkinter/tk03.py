#Importando biblioteca tkinter
from tkinter import *
import tkinter

#Criando jenela
root = tkinter.Tk()

#Criando frame para os 3 primeiros botões
frame = tkinter.Frame(root)
frame.pack()

#Criando frame para o quarto e último botão
aframe = tkinter.Frame(root)
aframe.pack()

#Criação de button vermelho
btn_red = tkinter.Button(frame, text='Vermelho', fg="red")
btn_red.pack(side=LEFT)

#Criação de button verde
btn_green = tkinter.Button(frame, text='Verde', fg="green")
btn_green.pack(side=LEFT)

#Criação de button azul
btn_blue = tkinter.Button(frame, text='Azul', fg="blue")
btn_blue.pack(side=LEFT)

#Criação de button preto
btn_black = tkinter.Button(aframe, text='Preto', fg="black")
btn_black.pack(side=BOTTOM)

root.mainloop()