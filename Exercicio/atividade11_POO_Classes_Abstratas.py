# Questão 01
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def falar(self, som):
#         print(f"O animal faz o som {som}")

# class Cachorro(Animal):
#     def falar(self, som):
#         return super().falar(som)
    
# class Gato(Animal):
#     def falar(self, som):
#         return super().falar(som)
    
# dog = Cachorro()
# cat = Gato()
# dog.falar("Au Au")
# cat.falar("Miau")

# Questão 02

# animal = Animal()
# TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'falar'

# Questão 03

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self, area):
        print(f"A área é {area}")

    @abstractmethod
    def perimetro(self, perimetro):
        print(f"O perimetro é {perimetro}")

class Retangulo(FormaGeometrica):
    def area(self, area):
        return super().area(area)

    def perimetro(self, perimetro):
        return super().perimetro(perimetro)
    
retang = Retangulo()
retang.perimetro(20)
retang.area(16)

# Questão 04

from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        print("O Veiculo está em movimento")

    @abstractmethod
    def parar(self):
        print("O veiculo está parado")

class Carro(Transporte):
    def mover(self):
        return super().mover()
    
    def parar(self):
        return super().parar()

veiculo = Carro()
veiculo.mover()
veiculo.parar()

# TypeError: Can't instantiate abstract class Carro without an implementation for abstract method 'parar'