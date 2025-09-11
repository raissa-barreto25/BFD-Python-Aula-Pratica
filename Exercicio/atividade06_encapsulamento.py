# Questão 01
# class ContaBancaria:
#     def __init__(self,titular,saldo=0):
#         self.titular = titular
#         self.__saldo = saldo
#         self.operacoes = []

#     def __str__(self):
#         return f"A conta de {self.titular} tem o saldo de {self.__saldo}"
    
#     def get_saldo(self):
#         return self.__saldo
    
#     def set_saldo(self, valor):
#         if valor < 0:
#             print("Saldo não pode ser negativo")
#         else:
#             self.__saldo = valor
    
#     def depositar(self, valor):
#         self.__saldo += valor
#         self.operacoes.append(["Deposito", valor])
#         print(f"Foi depositado {valor} na sua conta")

#     def sacar(self, valor):
#         if valor <= self.__saldo:
#             self.__saldo -+ valor
#             self.operacoes.append(["Saque", valor])
#             print(f"Foi sacado {valor} da sua conta")
#         else:
#             print("Saldo insuficiente")
    
#     def extrato(self):
#         for operacao in self.operacoes:
#             print(operacao)
#         print(f"Saldo : {self.operacoes}")

# conta1 = ContaBancaria("Raissa", 200)
# print(conta1)
# conta1.depositar(300)
# conta1.get_saldo()
# conta1.set_saldo(50)
# print(conta1)

# Questão 02
# class Pessoa:
#     def __init__(self, nome, data_de_nascimento, cpf, identidade):
#         self.nome = nome
#         self.data_de_nascimento = data_de_nascimento
#         self.__cpf = cpf
#         self.__identidade = identidade
    
#     def __str__(self):
#         return f"Usuario de nome: {self.nome}, data de nascimento: {self.data_de_nascimento}, CPF: {self.__cpf} e Identidade: {self.__identidade}"
    
#     def get_cpf(self):
#         return self.__cpf
    
#     def get_identidade(self):
#         return self.__identidade
    
#     def set_cpf(self, numero):
#         self.__cpf = numero

#     def set_identidade(self, numero):
#         self.__identidade = numero

# pessoa1 = Pessoa("Raissa", "25/12/1994", "123.456.789-10", "1.234.567")
# print(pessoa1)
# pessoa1.get_cpf()
# pessoa1.get_identidade()
# pessoa1.set_cpf("012.345.678-99")
# pessoa1.set_identidade("2.345.678")
# print(pessoa1)