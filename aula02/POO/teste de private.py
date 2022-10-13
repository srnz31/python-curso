""" 
class __Teste1:
    a = 1 #atributo publico
    b = 2 #atributo privado

t1 = __Teste1()
print(t1.a)
print(t1.b)
"""
""" 
class Pessoa:
    __cpf = None
    
    def __init__(self, cpf):
        self.cpf = cpf
        
    def __validarCPF(self, valor):
        return (valor == self.cpf)
    
    def setcpf(self, valor):
        if self.__validarCPF(valor):
            self.__cpf = valor
            
        else:
            print("CPF invalido")
            
pessoa01 = Pessoa(123)
pessoa01.setcpf(12553) 
"""

class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhada = 0
        self.__salario = 0
        
    @property
    def salario(self):
        return self.__salario
    
    @property
    def hora(self):
        return self.__horas_trabalhada
    
    @salario.setter
    def salario(self, novo_salario):
        raise ValueError('Impossível alterar salario diretamente')
    """ 
    def registra_hora_trabalhada(self):
        self.__horas_trabalhada += 1
         """
    def calcula_salario(self):
        self.__salario = self.__horas_trabalhada * self.valor_hora_trabalhada
        
jose = Funcionario('josé carlos', 'menino da TI', 50)
h = int(input("Digite suas horas trabalhadas: "))
jose.__horas_trabalhada = h
print(jose.__hora)
jose.calcula_salario()
print(jose.salario)