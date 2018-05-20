from time import sleep

print('''
    Exercicio 07 de Python
    Curso da Solyd
    Day 21 Code Python - 20/05/2018
''')

def maiorNumero(args):
    maximo = max(args)
    return maximo

def menorNumero(args):
    minimo = min(args)
    return minimo

valores = [7, 3, 12, 2.6, 14, 9, 10]

maior = maiorNumero(valores) 
menor = menorNumero(valores)

print('\nCalculando...')
sleep(1)

print('O maior número é', maior)
print('O menor número é', menor)

print('-=-'*20)
