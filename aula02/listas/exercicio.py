import os

#Exercício 01
""" 
familys = ['filho', 'pai', 'mae', 'irmã']
for x in familys:
    print(x)
"""

#Exercício 02
""" 
names = list()
for x in range(0, 3):
    names.append(input('DIGITE O %iº  NOME: '%x))
os.system('cls')
print(names)
"""

#Exercício 03
'''
numbers = [1, 5, 9, 8, 7]
number = int(input('DIGITE UM NÚMERO: '))
if number in numbers:
    print('O NÚMERO %i está na lista %s'%(number, numbers))
else:
    print('O NÚMERO %i não está na lista %s'%(number, numbers))
'''

#Exercício 04
'''
names = list()
for x in range(0, 5):
    names.append(input('DIGITE O %iº  NOME: '%(x+1)))

x = int(input('DIGITE UMA POSIÇÃO DE 0 a 4: '))
removeName = names.pop(x)
os.system('cls')
print('VOCÊ REMOVEU O NOME "%s" DA LISTA %s'%(removeName, names))
'''
