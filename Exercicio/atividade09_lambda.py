from functools import reduce

# Questão 01
numero = [1, 2, 3, 4, 5]
print(list(map(lambda num : num * 2, numero)))

# Questão 02
lista = [10, 15, 20, 25, 30]
print(list(filter(lambda num : num % 2 == 0, lista)))

# Questão 03 
num = [1, 2, 3, 4, 5]
print(reduce(lambda x, y : x + y, num))

# Questão 04
frutas = ["uva", "banana", "maçã", "laranja"]
print(sorted(frutas, key=lambda item: len(item) ))

# Questão 05
nome = ["ana", "pedro", "maria"]
print(list(map(lambda item : item[:].title(), nome)))

# Questão 06
mult = [2, 3, 4, 5]
print(reduce(lambda x, y : x * y, mult))

# Questão 07
frut = ["banana", "uva", "maçã", "laranja"]
print(sorted(frut, key=lambda item : item [-1]))