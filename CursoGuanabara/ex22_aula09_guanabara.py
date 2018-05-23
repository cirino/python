print("""
    Exercício 22 da aula 09 de Python
    Curso do Guanabara
    Day 7 Code Python - 06/05/2018
""")

nomeCompleto = str(input('Digite seu nome completo: ')).strip()

print('Analisando o seu nome...')

print('Seu nome é {}'.format(nomeCompleto.upper()))
print('Seu nome é {}'.format(nomeCompleto.lower()))
print('Seu nome tem {} letras'.format(len(nomeCompleto.replace(' ', ''))))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nomeCompleto.split()[0], len(nomeCompleto.split()[0])))