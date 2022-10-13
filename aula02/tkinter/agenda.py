import tkinter as tk
from tkinter import filedialog

class Tela: #Criando classe tela
    #Iniciando construtor para receber o janela inicial
    def __init__(self, master):
        self.root = master #O parâmetro master é o objeto que representar a janela
        self.arquivoAberto = None
        self.criarWidgets()

    #Método que cria/posiciona os widgets da interface gráfica
    def criarWidgets(self):
        #Campo para entrada de nome
        self.lb1 = tk.Label(self.root, text='Entre com o nome', font=('arial', 12))
        self.entradaNome = tk.Entry(self.root, font=('Arial', 12))
        
        #Campo para entrada de telefone
        self.lb2 = tk.Label(self.root, text='Entre com o telefone', font=('arial', 12))
        self.entradaTelefone = tk.Entry(self.root, font=('Arial', 12))

        self.btn = tk.Button(self.root, text='Cadastrar', command=self.salvar)    
        
        #Posicionando entrada de nome
        self.lb1.grid(column=0, row=0)
        self.entradaNome.grid(column=1, row=0, padx=20)
        
        #Posicionando entrada de telefone
        self.lb2.grid(column=0, row=1)
        self.entradaTelefone.grid(column=1, row=1, padx=20)
        
        #Posicionando botão
        self.btn.grid(column=0, row=2, columnspan=2, pady=20)
        
    #Método que salva os dados num arquivo .txt
    def salvar(self):
        nome = self.entradaNome.get()
        telefone = self.entradaTelefone.get()
        
        if(self.arquivoAberto is None):
            self.arquivoAberto = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Aquivos de texto", '*.txt'),('Todos arquivos', "*.*")))
            
        #Se existir um arquivo já aberto para salvamento
        if(self.arquivoAberto is not None):
            #Abre o caminho em modo de append
            dados = open(self.arquivoAberto, 'a') #Obtem os dados do arquivo .txt
            dados.write("\n Nome: {} \n --> Telefone: {}".format(nome, telefone))
            dados.close()
        else:
            print('Errou')
            
janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()