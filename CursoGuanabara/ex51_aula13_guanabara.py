print('''
    Exercício 51 da aula 13 de Python
    Curso do Guanabara
    Day 22 Code Python - 21/05/2018
''')

primeira = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

décima = primeira + (10 - 1) * razao
print('Os primeiros 10 termos são:', end=' ')
for n in range(primeira, décima + razao, razao):
    print('{}'.format(n), end=' -> ')
print('FIM')
