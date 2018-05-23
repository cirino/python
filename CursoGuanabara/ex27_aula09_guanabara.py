print("""
    Exercício 27 da aula 09 de Python
    Curso do Guanabara
    Day 7 Code Python - 06/05/2018
""")

nome = str(input('Qual o seu nome completo: ')).strip()
n = nome.split()

print('Seu primeito nome é {}'.format(n[0]))

print('Seu último nome é {}'.format(n[-2]))
print('Seu último nome é {}'.format(n[len(n)-1]))
