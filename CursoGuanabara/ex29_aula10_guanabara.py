print("""
    Exercício 29 da aula 10 de Python
    Curso do Guanabara
    Day 7 Code Python - 06/05/2018
""")

velocidade = float(input('Qual a velocidade do carro: '))

if velocidade > 80:
    print('Você está acima da velocidade.')
    multa = (velocidade-80) * 7
    print('Valor da multa: R${:.2f}'.format(multa))
print('Tenha um bom dia.')
