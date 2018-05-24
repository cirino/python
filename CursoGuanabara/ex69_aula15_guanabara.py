print('''
    Exercício 69 da aula 15 de Python
    Curso do Guanabara
    Day 24 Code Python - 23/05/2018
''')

print('Cadastro de Pessoas')
print('-=' * 23)

qtdHomem = qtdMaior = qtdMulherMenor = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = continuar = ' '

    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]

    if sexo == 'M':
        qtdHomem += 1

    if idade >= 18:
        qtdMaior += 1

    if sexo == 'M' and idade < 20:
        qtdMulherMenor += 1

    if continuar == 'N':
        break

print('-=' * 23)

print(f'Você cadastrou {qtdMaior} pessoas com mais de 18 anos.')
print(f'{qtdHomem} homens cadastrados.' if qtdHomem > 0 else 'Nenhum homem cadastrado')
print(f'{qtdMulherMenor} mulheres com menos de 20 anos.' if qtdMulherMenor > 0 else 'Nenhuma mulher com menos de 20 anos cadastrada.')

print('FIM')
print('-=' * 23)
