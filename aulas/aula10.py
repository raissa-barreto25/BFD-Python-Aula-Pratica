import datetime
class ContaBancaria:
    # Atributos
    def __init__(self, titular, num_conta, saldo=0):
        self.titular = titular
        self.num_conta = num_conta
        self.__saldo = saldo
        self.operacoes = []

    def __str__(self):
        return f"Conta n {self.num_conta} do titular {self.titular} tem {self.__saldo} de saldo"
    
    def __repr__(self):
        return f"ContaBancaria(titular={self.titular!r},num_conta={self.num_conta!r}, saldo={self.__saldo!r})"
    
    def get_saldo(self): #getters
        return self.__saldo
    
    def set_saldo(self, valor): #setters
        if valor < 0:
            print("Saldo não pode ser negativo")
        else:
            self.__saldo = valor

    # Metodo
    def deposito(self, valor):
        self.__saldo += valor
        data_operacao = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        self.operacoes.append([data_operacao, "Deposito", valor])
        print(f"Foi depositado {valor} reais na sua conta")
    
    def saque(self, valor):
        self.__saldo -= valor
        data_operacao = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        self.operacoes.append([data_operacao, "Saque", valor])
        print(f"Foi sacado {valor} reais na sua conta")

    def extrato(self):
        for operacao in self.operacoes:
            print(operacao)
        print(f"Saldo: {self.saldo}")

conta1 = ContaBancaria("Raíssa","0000000",50)
# conta1.__saldo = -34
# print(conta1.__saldo)
conta1.deposito(456)
print(conta1)
print(conta1.get_saldo())
conta1.set_saldo(-40)

### setters (defini valor); getters (pegar valor)
# Encapsulamento - privar funções no programa para proteção dos dados 