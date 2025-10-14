# Questão 01
from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        ...

class CartaoCredito(Pagamento):
    def processar(self, valor):
        print(f"Compra aprovada no valor de {valor} no cartão de credito")

class Boleto(Pagamento):
    def processar(self, valor):
        print(f"Pagamento do Boleto no valor de {valor} autorizado.")

credito = CartaoCredito()
boleto = Boleto()
credito.processar(250)
boleto.processar(150)

# Questão 02

from abc import ABC, abstractmethod

class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        ...

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        ...

class Computador(Ligavel, Desligavel):
    def ligar(self):
        print("O Computador foi ligado")

    def desligar(self):
        print("O Computador foi desligado")

comput = Computador()
comput.ligar()
comput.desligar()

# Questão 03

from abc import ABC, abstractmethod

class Imprimivel (ABC):
    @abstractmethod
    def imprimir(self):
        ...

class Exportavel (ABC):
    @abstractmethod
    def exportar(self):
        ...

class Relatorio (Imprimivel, Exportavel):
    def imprimir(self):
        print("O Documento foi impresso com sucesso.")

    def exportar(self):
        print("O documento está pronto para ser exportado para outra pasta.")

doc = Relatorio()
doc.imprimir()
doc.exportar()

# Questão 04

from abc import ABC, abstractmethod

class Repositorio (ABC):
    @abstractmethod
    def salvar(self, objeto):
        ...
    
    @abstractmethod
    def buscar (self, id):
        ...

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print(f"O {objeto} foi salvo no repositorio.")

    def buscar(self, id):
        print(f"O ID {id} que fez a ultima atualização.")

doc1 = RepositorioMemoria()
doc1.salvar("print")
doc1.buscar(10)

#TypeError: Can't instantiate abstract class RepositorioMemoria without an implementation for abstract method 'buscar'