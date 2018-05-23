print('''
    Exercício 61 da aula 14 de Python
    Curso do Guanabara
    Day 23 Code Python - 22/05/2018
''')

print('Gerador de PA')
print('-=' * 15)

primeira = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeira
cont = 1

while cont <= 10:
    print('{}'.format(termo), end=' -> ')
    termo += razao
    cont += 1
print('FIM')
