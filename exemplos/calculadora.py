"""
    Calculadora em Python
    Day 1 Code Python - 29/04/2018
"""

print("Calculadora do Cirino\n")

nome = str(input('Qual o seu nome? '))
giria = 'Vida Loka'

print('Boas vindas {}, {}!\n'.format(nome, giria))

def selecionaCalculo():
    listCalculo = ['Calcular', 'Soma', 'Subtração', 'Divisão', 'Multiplicação']

    for i, j in enumerate(listCalculo):
        print(i, j)

    itemCalculo = int(input('\nQual continha marota você quer fazer? '))

    if itemCalculo in range(1, 5):
        primeiroNumero = int(input('\nPrimeiro número: '))
        segundoNumero = int(input('Segundo número: '))

        opcoes = {1:soma, 2:subtracao, 3:divisao, 4:multiplicacao}
        opcoes.get(itemCalculo)(primeiroNumero, segundoNumero)
    else:
        print('\nMano, só digite os números da lista\n')
        selecionaCalculo()

def soma(a = 0, b = 0):
    aux = a + b
    print(aux)

def subtracao(a = 0, b = 0):
    aux = a - b
    print(aux)

def divisao(a = 1, b = 1):
    if (b <= 0) or (a <= 0):
        aux = 'Não pode dividir por 0 ou negativos: a / b'
    else:
        aux = a / b
    
    print(aux)

def multiplicacao(a = 0, b = 0):
    aux = a * b
    print(aux)

selecionaCalculo()

print('\n====FIM====')
