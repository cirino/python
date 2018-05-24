print('''
    Exercício 71 da aula 15 de Python
    Curso do Guanabara
    Day 24 Code Python - 23/05/2018
''')

print('{:^30}'.format('BANCO DO CIRINO'))
print('=' * 30)

n = int(input('Qual o valor para sacar? R$ '))

total = n
nota = 50   # começar de cima para baixo na estrutura
qtdNota = 0

while True:
    if total >= nota:
        total -= nota
        qtdNota += 1
    else:
        if qtdNota > 0:
            print(f'Total de {qtdNota} notas de {nota}')

        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1

        qtdNota = 0

        if total == 0:
            break

print('=' * 30)

print('{:^30}'.format('FIM'))
print('=' * 30)
