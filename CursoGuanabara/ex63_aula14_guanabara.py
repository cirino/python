print('''
    Exercício 63 da aula 14 de Python
    Curso do Guanabara
    Day 23 Code Python - 22/05/2018
''')

print('Sequência de Fibonacci')
print('-=' * 15)

n = int(input('Quantos termos quer mostrar? '))

t1 = 0
t2 = 1
cont = 3

print('-=' * 15)
print('{} -> {}'.format(t1, t2), end='')

while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1

print('-> FIM')
print('-=' * 15)
