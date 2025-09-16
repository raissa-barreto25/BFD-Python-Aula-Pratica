# SOLID
"""é um acrônimo mnemônico que relaciona um tópico de 
boas práticas de programação a cada letra. 
A aplicação desses princípios tem por objetivo deixar o 
projeto mais coeso, reaproveitável e torna a sua manutenção 
mais simples. Criado por Robert Cecil Martin (Manifesto Agil)
S - Responsabilidade unica (Single Responsability)
O - Principio aberto(para expanções)/fechado(Para modificações) (Open/Closed Principle)
L - (Liskov's Substituion Principle)
I - (Interface segregation)
D - (Dependency Inversion)"""
# Herança

# class Animal:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def som(self):
#         print("som indefinido")
    
# class Cachorro(Animal):
#       def som(self):
#         print("Au Au")

# doguinho = Cachorro("Rex", 2)
# print(doguinho.nome, doguinho.idade)
# doguinho.som()

class Mamifero:
    def __init__(self, idade, habitat, som):
        self.idade = idade
        self.habitat = habitat
        self.som = som
        self.prole = "gestação"
        self.alimentacao_infantil = "Leite"

    def som(som):
        print(som)

class Morcego(Mamifero):
    def __init__(self, idade, habitat, som, locomocao = "Vôo"):
        super().__init__(idade, habitat, som)
        self.locomocao = locomocao


zubat = Morcego(1, "Laje", "Assobio")
print(zubat.idade, zubat.habitat, zubat.som, zubat.locomocao, zubat.prole, zubat.alimentacao_infantil, sep = "\n")