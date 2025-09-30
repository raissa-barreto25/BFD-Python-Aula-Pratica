# Funções lambda - lambda argumentos : expressão (Conhecida como função anonima, 
# util quando precisa de funções rapidas.)
def dobro(num):
    return num * 2
dobro(5)

dobro = lambda num : num * 2
print(dobro(5))

print((lambda num : num * 2)(5))


def multiplica_lista(lista, funcao):
    for index, item in enumerate(lista):
        lista[index]=funcao(item)
        