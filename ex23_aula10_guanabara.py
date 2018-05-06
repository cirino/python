print("""
    Exercício 23 da aula 10 de Python
    Curso do Guanabara
    Day 7 Code Python - 06/05/2018
""")

num = int(input('Digite um número de 0 até 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {} ...'.format(num))
print('\tUnidade: {}'.format(u))
print('\tDezena: {}'.format(d))
print('\tCenteza: {}'.format(c))
print('\tMilhar: {}'.format(m))