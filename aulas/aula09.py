# class Cachorro:
#     especie = "Canis lupus familiaris"
#     nome = "Toto"
#     raca = "caramelo"
#     idade = 2

# auau = Cachorro()
# print(auau)
# print(auau.especie, auau.nome, auau.raca, auau.idade)

# doguinho = Cachorro()
# print(auau.especie, auau.nome, auau.raca, auau.idade, sep="\n")

# dunder (double underscores) __init__ metodo construtor 

# class Cachorro:
#     especie = "Canis lupus familiaris"
#     def __init__(self,nome,raca,idade): #metodo construtor
#         self.nome = nome
#         self.raca = raca
#         self.idade = idade

# doguinho01 = Cachorro("Rex","caramelo",2)
# print(doguinho01)
# print(doguinho01.especie, doguinho01.nome, doguinho01.raca, doguinho01.idade, sep="\n")

# class Cachorro:
#     especie = "Canis lupus familiaris"
#     def __init__(self,nome,raca,idade): #metodo construtor
#         self.nome = nome
#         self.raca = raca
#         self.idade = idade
    
#     def __str__(self):
#         return f"Especie: {self.especie},\nNome: {self.nome}, \nIdade:{self.idade}, \nRaça: {self.raca}"
    
# doguinho01 = Cachorro("Rex","caramelo",2)
# print(doguinho01)

# class Cachorro:
#     especie = "Canis lupus familiaris"
#     def __init__(self,nome:str,raca:int,idade:int): #metodo construtor
#         self.nome = nome
#         self.raca = raca
#         self.idade = idade
    
#     def __str__(self):
#         return f"Especie: {self.especie},\nNome: {self.nome}, \nIdade:{self.idade}, \nRaça: {self.raca}"
    
#     def latir(self):
#         print("Au Au Au")

#     def correr(self,metro):
#         print(f"{self.nome} correu {metro}m²")
    
# auau1 = Cachorro("Bob","Caramelo",15)
# print(auau1)
# auau1.latir()
# auau1.correr(50)

class ContaBancaria:
    def __init__(self, nome, numero_conta, saldo=0):
        self.nome = nome
        self.numero = numero_conta
        self.saldo = saldo
        self.operacoes = []
    
    def __str__(self):
        return f"Conta numero {self.numero} do titular {self.nome} com saldo de {self.saldo}!"
    
    # def registro_operacoes(self,tipo,valor): - verificar
    #     self.operacoes.append([tipo,valor])


    def saque(self, valor):
        if valor >self.saldo:
            print("Saldo Insuficiente")
        else:
            self.saldo -= valor
            

    def deposito(self, valor):
        self.saldo += valor
        
        
    def extrato(self):
        for operacao in self.operacoes:
            print(operacao)

    
    
conta1=ContaBancaria("Raissa",123456)
conta2=ContaBancaria("Helton",1234567,50000)
conta1.deposito(500)
conta1.saque(100)
conta2.saque(500)
print(conta1)
print(conta2)