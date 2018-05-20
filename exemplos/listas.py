"""
    Listas em Python
    Day 1 Code Python - 29/04/2018
"""

print("\nListas do Cirino\n")

list1 = ['Maca', 'Banana', 'Melao']
list2 = ['Tomate', 'Cebola', 'Cenora']

for i, j in zip(list1, list2):
    print(i, j+'\n')

for i,j in enumerate(list1):
    print(i, j+'\n')