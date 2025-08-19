# matriz = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

# print(matriz)

# tridimensional = [[[1,2,3],[4,5,6],[7,8,9]],
#                   [[1,2,3],[4,5,6],[7,8,9]],
#                   [[1,2,3],[4,5,6],[7,8,9]]]
# print(tridimensional[1][1][2])

# lista1 = []
# for i in range(10):
#     lista1.append(i)
# print(lista1)

# lista2 = [i for i in range(10)]
# print(lista2)

# lista2 = [i for i in range(10) if i%2==0]
# print(lista2)

# lista2 = [[linha for linha in range(3)] for coluna in range(3)]
# print(lista2)

# nome = "Raíssa"
# print(list(nome))

######### TUPLAS #########

# tupla1 = (1,2,3,4)
# for num in tupla1:
#     print(num+5)
# print(type(tupla1))

# tupla1 = ("Fred", "Fred", "João")
# print(tupla1.count("Fred"))

#### Conjunto set

# teste = {"Raíssa"}
# print(type(teste))

# teste = {1,2}
#teste.add(4)
#teste.clear()
# teste2 = teste.copy()
# print(teste)

# frutas = {"Banana", "Limão", "Tomate"}
# legumes = {"Cenoura", "Tomate", "Beterraba"}
#print(frutas.difference(legumes))
#print(legumes.difference_update(frutas))
#print(legumes.discard("Tomate"))
#print(legumes.intersection(frutas))
#print(legumes & frutas)
#print(legumes | frutas) = união das set
#print(frutas)

###### Dicionario

lista_alunos = {"Nome":"Raíssa",
                "Idade":"30",
                "Endereço": "Rua X",
                "Turmas": ("Turma 34", "Turma 36")}
print(lista_alunos)