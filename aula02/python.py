'''
num1 = 5
num2 = 2

soma = num1 + num2
subtracao = num1 - num2
multiplcacao = num1 * num2
divisao = num1 / num2
divisao_inteira = num1 // num2
modulo = num1 % num2
exponenciacao = num1 ** num2

print(num1,"+ ",num2,"=",soma)
print(num1,"- ",num2,"=",subtracao)
print(num1,"* ",num2,"=",multiplcacao)
print(num1,"/ ",num2,"=",divisao)
print(num1,"//",num2,"=",divisao_inteira)
print(num1,"% ",num2,"=",modulo)
print(num1,"**",num2,"=",exponenciacao)


x = 5
x += 1
print(x)
x -= 1
print(x)
x *= 3
print(x)
x /= 3
print(x)
x //= 2
print(x)
x %= 2
print(x)

numero = 5
numero += 5
print(numero)

soma1 = 7 + 8
soma2 = 10 + 5

if (soma1 == soma2):
    print("Os resultados são iguais")
else:
    print("Os resultados são diferentes")

a, b = 5, 10
print((a > 0) and (b == 0))
print((a > 0) and (b != 0))

print((a > 0) or (b == 0))
print((a != 0) or (b ==0))


print(not(a < b))
print(not(a == b))


a = int(input("Digite um número inteiro: "))

if ((a % 2) == 1):
    print("Númeor ímpar")
if ((a % 2) == 0):
    print("Número par")
    
print('Fim do programa')

a = int(input("Digite um número inteiro: "))

if ((a % 2) == 1):
    print("Númeor ímpar")
else:
    print("Número par")
    
print('Fim do programa')

n1 = float(input("DIGITE UM VALOR: "))
n2 = float(input("DIGITE UM VALOR: "))

if (n1 >= n2):
    print(n1,">=",n2)
else:
    print(n2,">",n1)

idade_lucas = int(input("Digite a idade de Lucas: "))
idade_carolina = int(input("Digite a idade de Carolina: "))

if (idade_lucas >= 18 or idade_carolina >=18):
    print("Pelo menos um dos dois é maior de idade")
else:
    print("Lucas e carolina não são maiores de idade")
    
if (idade_lucas >= 18 and idade_carolina >= 18):
    print("Lucas e Carolina são maiores de idade")
else:
    print("Pelo menos um dos dois não é maior de idade")
'''
""" 
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

import os
os.system('cls')

if (a>=b and b>=c):
    print(a,">=",b,">=",c)
else:
    if (a>c and c>b):
        print(a,">",c,">",b)
    else:
        if (b>a and a>c):
            print(b,">",a,">",c)
        else:
            if (b>c and c>a):
                print(b,">",c,">",a)
            else:
                if (c>a and a>b):
                    print(c,">",a,">",b)
                else:
                    if (c>b and b>a):
                        print(a,">",c,">",b) 
                         """

