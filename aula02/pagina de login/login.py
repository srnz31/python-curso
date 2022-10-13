from tkinter import *

#Criando janela
root = Tk()
root.title('Portal de cursos')
root.geometry('490x560+610+153')
root.iconbitmap('ico.ico')
root.resizable(True, True)

def new_root():
    root.destroy()

#importar imagens
img_fundo = PhotoImage(file='fundo.png')
lb = Label(root, image=img_fundo)
lb.pack()

img_btn = PhotoImage(file='bt-img.png')
btn = Button(lb, image=img_btn, cursor='hand2', bd=0, command=new_root)
btn.place(x=185, y=448)

entry_id = Entry(lb, width=21, font='arial 25', bd=0)
entry_id.place(x=48, y=138)

entry_email = Entry(lb, width=21, font='arial 25', bd=0, justify=RIGHT)
entry_email.place(x=48, y=243)

entry_password = Entry(lb,show='*', width=21, font='arial 25', bd=0)
entry_password.place(x=48, y=354)

root.mainloop()