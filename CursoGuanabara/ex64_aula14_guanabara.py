print('''
    Exercício 64 da aula 14 de Python
    Curso do Guanabara
    Day 23 Code Python - 22/05/2018
''')

print('Somando em loop')
print('-=' * 20)

cont = soma = 0
n = int(input('Digite um número. [999] para parar: '))

while n != 999:
    soma += n
    n = int(input('Digite um número. [999] para parar: '))
    cont += 1

print('-=' * 20)
print('Você digitou {} números, e a soma deles deu {}.'.format(cont, soma))
print('FIM')
print('-=' * 20)
