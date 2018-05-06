print("""
    Exercício 30 da aula 10 de Python
    Curso do Guanabara
    Day 8 Code Python - 06/05/2018
""")

numero = int(input('Digite o número: '))

tipo = numero % 2


if tipo == 0:
    print('O número {} é par.'.format(numero))
else:
    print('O número {} é ímpar'.format(numero))
print('Tenha um bom dia.')
