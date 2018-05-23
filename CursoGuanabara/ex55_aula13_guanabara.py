print('''
    Exercício 55 da aula 13 de Python
    Curso do Guanabara
    Day 22 Code Python - 21/05/2018
''')

maior = 0
menor = 0

for n in range(1, 6):
    peso = float(input('Peso {}ª: '.format(n)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        else:
            menor = peso

print('O maior peso foi {}'.format(maior))
print('O menor peso foi {}'.format(menor))
