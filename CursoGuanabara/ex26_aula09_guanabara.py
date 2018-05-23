print("""
    Exercício 26 da aula 09 de Python
    Curso do Guanabara
    Day 7 Code Python - 06/05/2018
""")

frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra A aparece {} vezes'.format(frase.count('a')))

print('A primeira letra A aparece na posição {}'.format(frase.find('a')+1))

print('A última letra A aparece na posição {}'.format(frase.rfind('a')+1))