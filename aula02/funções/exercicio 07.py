 
#Exercicio 01
def first():
    print('Minha primeira função')
first()

#Exercicio 02
def menssage(name, age):
    print("{nome} possui {idade} anos")

name = input('Digite seu nome: ')
age = int(input('Digite sua idade: '))

menssage(name, age)

#Exercicio 03
def mult(n1, n2):
    return (n1 * n2)

print(mult(5, 8))

#Exercicio 04
def double(a):
    return (a * 2)

x1 = float(input('Digite o primeiro número: '))
x2 = float(input('Digite o segundo número: '))
x3 = float(input('Digite o terceiro número: '))
print(double(max(x1, x2, x3)))

#Exercicio 05
def colocar(name, lista ):
    lista.append(name)
    
nameList = []
for i in range(5):
    n = input('Digite o %iº nome: ' %(i+1))
    colocar(n, nameList)

for na in nameList:    
    print(na)