# Questão 01
#Crie uma classe abstrata Pessoa que tenha os métodos: Falar, Andar e Comer e subclasses Funcionario
#e Aluno, que herde as caracteristicas e Metodos de Pessoa. Instancie um objeto para cada subclasse. 

from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def falar(self):
        print("A pessoa está falando")
    
    @abstractmethod
    def andar(self):
        print("A pessoa está andando")

    @abstractmethod
    def comer(self):
        print("A pessoa está comendo")

class Funcionario(Pessoa):
    def falar(self):
        return super().falar()
    
    def andar(self):
        return super().andar()
    
    def comer(self):
        return super().andar()
    
class Aluno(Pessoa):
    def falar(self):
        return super().falar()
    
    def andar(self):
        return super().andar()
    
    def comer(self):
        return super().andar()
    
pedro = Funcionario()
pedro.falar()
pedro.andar()
pedro.comer()
joao = Aluno()
joao.falar()
joao.andar()
joao.comer()

# Questão 02
#Usando o mesmo exemplo da questão anterior, mas converta a classe pessoa em uma interface

from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def falar(self, palavras):
        ...
    
    @abstractmethod
    def andar(self, passos):
        ...

    @abstractmethod
    def comer(self, comida: str):
        ...

class Funcionario(Pessoa):
    def falar(self, palavras):
        print(f"O funcionario falou {palavras} palavras.")
    
    def andar(self, passos):
        print(f"O funcionario andou {passos} passos.")
    
    def comer(self, comida: str):
        print(f"O funcionario comeu {comida}.")

class Aluno(Pessoa):
    def falar(self, palavras):
        print(f"O aluno falou {palavras} palavras.")
    
    def andar(self, passos):
        print(f"O aluno andou {passos} passos.")
    
    def comer(self, comida: str):
        print(f"O aluno comeu {comida}.")

pedro = Funcionario()
pedro.falar(150)
pedro.andar(200)
pedro.comer("Pizza")
joao = Aluno()
joao.falar(50)
joao.andar(150)
joao.comer("Macarrão")