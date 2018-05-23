from veiculo import Veiculo

print('''
    Aula 09 de Python
    Curso da Solyd
    Day 22 Code Python - 21/05/2018
''')

carro1 = Veiculo('azul', 'fiat', 4, 10)

print(carro1.cor)
print(carro1.marca)
print(carro1.tanque)
carro1.abastecer(25)
print(carro1.tanque)
carro1.abastecer(60)
print(carro1.tanque)
carro1.abastecer(60)
print(carro1.tanque)

print('')

carro2 = Veiculo('verde', 'ford', 4, 22)

print(carro2.cor)
print(carro2.marca)
print(carro2.tanque)
carro2.abastecer(15)
print(carro2.tanque)
carro2.abastecer(15)
print(carro2.tanque)
carro2.abastecer(15)
print(carro2.tanque)

print('')
