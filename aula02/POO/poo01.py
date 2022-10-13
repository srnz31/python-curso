#self equivale ao this em JS
""" 
class Pessoa:
    
    nome = None
    idade = None
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def getAnoNascimento(self, anoAtual):
        return anoAtual - self.idade
    
pessoa = Pessoa('José Carlos', 19)
print(pessoa.getAnoNascimento(2022))
"""
class Cliente:
    nome, sobrenome, cpf = None, None, None
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome =
class Conta:
    titular, numeroConta, saldo, limite = None, None, None, None
    
    def __init__(self, titular, numero, saldo, limite):
        print("Inicializando uma conta")
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
    def imprimir(self):
        return f"O titular {self.titular} tem saldo de {self.saldo}"
    

conta = Conta('123-4', 'Bill', 120.0, 1000.0)
print(conta.imprimir())