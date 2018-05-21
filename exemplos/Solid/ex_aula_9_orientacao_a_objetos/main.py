from banco import Conta

print('''
    Exercício 09 de Python
    Curso da Solyd
    Day 22 Code Python - 21/05/2018
''')

cliente1 = Conta(12345, 'dag', 29)

print(cliente1.cpf)
print(cliente1.nome)
print(cliente1.idade)
print(cliente1.saldo)

cliente1.deposito(2200)
print(cliente1.saldo)

cliente1.sacar(1300)
print(cliente1.saldo)

print('')

cliente2 = Conta(12233, 'mih', 24)

print(cliente2.cpf)
print(cliente2.nome)
print(cliente2.idade)
print(cliente2.saldo)

cliente2.deposito(1400)
print(cliente2.saldo)

cliente2.sacar(500)
print(cliente2.saldo)
