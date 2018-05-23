print('''
    Exercício 57 da aula 14 de Python
    Curso do Guanabara
    Day 23 Code Python - 22/05/2018
''')

lista = {'M': 'MASCULINO', 'F': 'FEMININO'}

aux = '' #input('Qual o sexo [M/F] ? ').strip().upper()

while aux not in lista:
    aux = input('Qual o sexo [M/F] ? ').strip().upper()

print(aux)
