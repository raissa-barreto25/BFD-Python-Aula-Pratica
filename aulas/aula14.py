#POO: Classes abstratas - Essencialmente, são classes que não podem ser instanciadas diretamente, 
# mas servem de estrutura padrão, templete, para criação de novas classes. 
#Para usar classes abstratas no python, é necessário importar o módulo ABC:

# from abc import ABC

# class Animal(ABC):
#     def movimentar(self, metros:float):
#         print(f"O animal se deslocou {metros} metros")

# animal1 = Animal()
# animal1.movimentar(5)

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def movimentar(self, metros:float):
#         print(f"O animal se deslocou {metros} metros")

# class Cachorro(Animal):
#     def movimentar(self, metros):
#         return super().movimentar(metros)

# dog = Cachorro()
# dog.movimentar(4.5)

# from abc import ABC, abstractmethod

# class Pessoa(ABC):
#     @abstractmethod
#     def comer(self):
#         print("A pessoa esta comendo")

#     @abstractmethod
#     def andar(self):
#         print("A pessoa esta andando")
        
#     @abstractmethod
#     def correr(self):
#         print("A pessoa esta correndo")

# class Estudante(Pessoa):
#     def comer(self):
#         return super().comer()
#     def andar(self):
#         return super().andar()
#     def correr(self):
#         return super().correr()

# joao = Estudante()
# joao.correr()
# joao.andar()
# joao.comer()

#POO: Interfaces

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def movimentar(self, metros:float):
#         ...

# class Cachorro(Animal):
#     def movimentar(self, metros):
#         print(f"O Cachorro andou {metros} metros")

# dog = Cachorro()
# dog.movimentar(4.5)

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def movimentar(self, metros:float):
#         ...

#     @abstractmethod
#     def alimentar(self):
#         ...

# class Cachorro(Animal):
#     def movimentar(self, metros):
#         print(f"O Cachorro andou {metros} metros")

#     def deslocamento(animal: Animal):
#         animal.movimentar

# dog = Cachorro()
# dog.movimentar(4.5)
# dog.alimentar()


# Uma classe pode implementar várias interfaces(Heranças Multiplas), mas apenas


# POO - S O L I D
"""é um acrônimo mnemônico que relaciona um tópico de 
boas práticas de programação a cada letra. 
A aplicação desses princípios tem por objetivo deixar o 
projeto mais coeso, reaproveitável e torna a sua manutenção 
mais simples. Criado por Robert Cecil Martin (Manifesto Agil)
S - Responsabilidade unica (Single Responsability)
O - Principio aberto(para expanções)/fechado(Para modificações) (Open/Closed Principle)
L - Principio da Substituição de Liskov (Liskov's Substituion Principle)
I - Principio da Segregação de interfaces (Interface segregation)
D - Principio da Inversão de Dependência (Dependency Inversion)"""