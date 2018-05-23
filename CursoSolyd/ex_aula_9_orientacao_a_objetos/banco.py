print('''
    Exercício 09 de Python
    Curso da Solyd
    Day 22 Code Python - 21/05/2018
''')

class Conta:
    def __init__(self, cpf, nome, idade, saldo = 0):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo - valor < 1500:
            print('Seu limite não permite o saque.')
        else:
            self.saldo -= valor
    

