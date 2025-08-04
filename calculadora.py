#Cálculadora básica em python#

def soma (a,b):
    return a + b

def subtracao (a,b):
    return a - b

def multiplicacao (a,b):
    return a * b

def divisao (a,b):
    return a // b

#Coletando informações#
operador = input("Digite a operação que deseja realizar (+, -, *, /): ")
primeiro_numero = int(input("Qual o primeiro número: "))
segundo_numero = int(input("Qual o segundo número: "))

#Realizando operações#
if operador == '+':
    print(soma(primeiro_numero, segundo_numero))

elif operador == '-':
    print(subtracao(primeiro_numero, segundo_numero))

elif operador == '*':
    print(multiplicacao(primeiro_numero, segundo_numero))

elif operador == '/':
    print(divisao(primeiro_numero, segundo_numero))

else:
    print("Operação inválida, tente de novo!")
    operador = input("Digite a operação que deseja realizar (+, -, *, /): ")
    primeiro_numero = int(input("Qual o primeiro número:"))
    segundo_numero = int(input("Qual o segundo número: "))    
