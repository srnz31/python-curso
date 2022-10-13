#minhaLista = [10, 50, 5, 2, 100]

#indice da lista
'''
print(minhaLista[0])
print(minhaLista[1])
print(minhaLista[2])
print(minhaLista[3])
print(minhaLista[4])
'''

#Imprime valores da lista
'''
print('De frente pra trás')
i = 0
while i < 5:
    print(minhaLista[i])
    i += 1

print('De trás pra frente')
i = 4
while i >= 0:
    print(minhaLista[i])
    i -= 1
'''

#Modifica o intem da lista
'''
minhaLista[3] = 200
print(minhaLista)
'''

#add utilizando método .append()
'''
nomes = [50, 10, 15, 20]
nomes.append('joãozinho')
nomes.append('chico de josé')
nomes.append('antönio')
nomes.append('zefinha')
for nome in nomes:
    print(nome)
'''

'''
alunos = []
qtdAlunos = int(input('Informe a quantidade de alunos na turma: '))
i = 0
while i< qtdAlunos:
    nome = input('Informe o nome do aluno %d: '%(i+1))
    alunos.append(nome)
    i += 1
    
print('\n\n========= LISTA DE ALUNOS =========\n\n')

i = 0
while i < qtdAlunos:
    print('Aluno %d: %s' %(i+1, alunos[i]))
    i += 1
'''

#minhaLista = [10, 50, 5, 2, 100, 500, 300]

#Deletando item utilizando comando del()
'''
print('lista original %s' %(minhaLista))
del(minhaLista[2])
print('lista original %s' %(minhaLista))
'''

#Deletando item utilizando método .pop()
'''
print('lista original :%s' %(minhaLista))
elementoRemovido = minhaLista.pop(2)
print('Elemento removido:', elementoRemovido)
print('lista original: %s' %(minhaLista))
'''

#Ver tamanho de uma lista utilizando método .len()
"""
tamanho = len(minhaLista)
print('O tamanho dessa lista é: %d'%tamanho) 
"""

#Funções que retornam o maior e menor de uma lista
"""
numeros = [15, 5, 0, 20, 10]
nomes = ['Caio', ' Alex', 'Renata', 'Patrícia', 'Bruno']

print('O maior número da lista "%s" é %s'%(max(numeros), numeros)) #Numa lista de números o max() retorna o maior valor
print('O menor número da lista "%s" é %s'%(min(numeros), numeros)) #Numa lista de números o min() retorna o menor valor
print('O nome primeiro nome em ordem alfabética da lista "%s" é %s'%(max(nomes), nomes)) #Numa lista de string o max() retorna o primeiro nome em ordem alfabética
print('O nome último nome em ordem alfabética da lista "%s" é %s'%(min(nomes), nomes)) #Numa lista de string o min() retorna o último nome em ordem alfabética
print('A soma de todos os elementos da lista %s  é %.2f'%(numeros, sum(numeros))) #Somar valores de uma lista com o sum()
"""

#Vendo valores de list, tuple, dict
professores = ['Carla', 'Daniel', 'Ingrid', 'Roberto']
estacoes = ('Primavera', 'Verão', 'Outono', 'Inverno')
cliente = {
    'Nome':'Fábio Garcia',
    'email':'fabio_garcia_9@outlook.com'
}
print(type(professores))
print(type(estacoes))
print(type(cliente))