import tkinter
from tkinter import *

#Criando a primeira janela para ser a bandeira da frança
root = tkinter.Tk()
root.geometry('300x300')
root.resizable(False, False)

#Criando a segunda janela para ser a bandeira da holanda
root2 = tkinter.Tk()
root2.geometry('300x300')
root2.resizable(False, False)

#Criando cores da banceira da frança
frame_blue = tkinter.Frame(root, width=100, height=300, background= '#ff0000')
frame_red = tkinter.Frame(root, width=100, height=300, background= '#0000ff')
frame_white = tkinter.Frame(root, width=100, height=300, background= '#fff')

#Inserindo no frames na página
frame_blue.pack(side=tkinter.LEFT)
frame_white.pack(side=tkinter.LEFT)
frame_red.pack(side=tkinter.LEFT)

frame_blue2 = tkinter.Frame(root2, width=300, height=100, background= '#ff0000')
frame_red2 = tkinter.Frame(root2, width=300, height=100, background= '#0000ff')
frame_white2 = tkinter.Frame(root2, width=300, height=100, background= '#fff')

frame_blue2.pack(side=TOP)
frame_white2.pack(side=TOP)
frame_red2.pack(side=TOP)

root.mainloop()
root2.mainloop()