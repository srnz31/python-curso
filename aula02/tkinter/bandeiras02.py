import tkinter
from tkinter import *

#Função que cria bandeira
def bandeira(root, w, h, t):

    root.geometry('300x300')
    root.resizable(False, False)
    
    frame_blue = tkinter.Frame(root, width=w, height=h, background= '#ff0000')
    frame_red = tkinter.Frame(root, width=w, height=h, background= '#0000ff')
    frame_white = tkinter.Frame(root, width=w, height=h, background= '#fff')

    frame_blue.pack(side=t)
    frame_white.pack(side=t)
    frame_red.pack(side=t)

    root.mainloop() 

bandeira(Tk(), 100, 300, LEFT)
bandeira(Tk(), 300, 100, TOP)