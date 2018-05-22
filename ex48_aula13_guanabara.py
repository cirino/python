print('''
    Exercício 48 da aula 13 de Python
    Curso do Guanabara
    Day 22 Code Python - 21/05/2018
''')

soma = 0
cont = 0

for n in range(1, 501, 2):
    if n % 2 != 0:
        soma += n
        cont += 1
print('Contagem: {}. Soma: {}'. format(cont, soma))
