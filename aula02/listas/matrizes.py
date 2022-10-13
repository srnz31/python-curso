import os
os.system('cls')
""" 
l = int(input('Entre com o número de linhas: '))
c = int(input('Entre com o número de colunas: '))
matriz = list()

for nI in range(l):
    linha = []
    for j in range(c):
        linha.append("(%d,%d)"%(nI+1, j+1))
    matriz.append(linha)

for i in range(l):
    print(matriz[i]) 
"""

""" 
n = int(input('Tamanho da matriz: '))
linha = [0] * n
matriz = [linha] * n
print(matriz)

for l in range(n):
    linha = []
    for c in range(n):
        numero = int(
            input("Digite o número que ficara armazenado {},{} :".format(l, c)))
        linha.append(numero)
        matriz[l] = linha

for i in range(n):
    print(matriz[i])
"""

"""
l = int(input('Entre com o número de linhas: '))
c = int(input('Entre com o número de colunas: '))
matriz = list()

for nI in range(l):
    linha = []
    for j in range(c):
        linha.append(int(input("Digite o número para ficar armazenado (%d,%d): "%(nI+1, j+1))))
    matriz.append(linha)

for i in range(l):
    print(matriz[i]) 
"""