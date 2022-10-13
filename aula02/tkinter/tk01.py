from tkinter import *

#Definindo janela
root = Tk()
root.title('Sistema 1.0')
root.geometry('500x300')
root.iconbitmap('python.ico') #Define uma icon para o programa
root.resizable(True, True) #Limita a redefinição de tela o primeiro é a largura e o segunda a autura
#root.configure(background='#0f0') #Muda a cor do fundo

""" 
#Texto label
label = Label(root, text= "introdução", font=('arial bold', 50))
label.grid(column=1, row=1)

#Botão do clique aqui
bot = Button(root, text='Clica Aqui', bg='black', fg='white')
bot.grid(column=1, row=2)

#Caixa de texto
txtbox = Entry(root, width=10)
txtbox.grid(column=1, row= 3)
"""

#Criando frame para dividir a tela
f_1 = Frame(root, width=820, height=40, bg='#4f67bd')
f_1.grid(column=0, row=0, columnspan=5)

f_2 = Frame(root, width=200, height=160, bg='#cec')
f_2.grid(column=0, row=1)

f_3 = Frame(root, width=400, height=160, bg='#fff')
f_3.grid(column=1, row=1)

f_4 = Frame(root, width=100, height=160, bg='#fff')
f_4.grid(column=2, row=1, padx=10)

f_5 = Frame(root, width=100, height=160, bg='#000')
f_5.grid(column=3, row=1)

root.mainloop()