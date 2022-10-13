from turtle import Vec2D


def quadrado(numero):
    if numero == 1:
        return
    print('%d\t'%(numero*numero))

quadrado(1)
def imprime_msg(nomePessoa):
    print('O usuário'+ nomePessoa +'escreveu uma mensagem')
    
nome = input('Digite o seu nome: ')
imprime_msg(nome)

def soma(v1, v2):
    return v1 + v2

print(soma(3, 4))

def f(a =5, d = 2):
    print(a,d)

f()