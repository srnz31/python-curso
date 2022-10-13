vogais = ('a', 'e', 'i', 'o', 'u')
letras = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
n = [1, 2, 3, 4, 5]
print(letras[1:4])
print(letras[:3])

dados = [
    {'dia':12, 'mes': 2, 'ano': 2019, 'temp': 30.5},
    {'dia':18, 'mes': 3, 'ano': 2019, 'temp': 29.1},
    {'dia':22, 'mes': 4, 'ano': 2019, 'temp': 28.5},
    {'dia':17, 'mes': 5, 'ano': 2019, 'temp': 26.4}
]

for dado in dados:
    print(f"# 0{dado['dia']}/{dado['mes']}/{dado['ano']} temperatura: {dado['temp']} C")