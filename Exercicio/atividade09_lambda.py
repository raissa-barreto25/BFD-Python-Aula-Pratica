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

# Questão 05
nome = ["ana", "pedro", "maria"]
print(list(map(lambda item : item[0].upper, nome)))