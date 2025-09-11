# Questão 01
# class Pessoa:
#     def __init__(self,nome,idade):
#         self.nome = nome
#         self.idade = idade
    
# dados = Pessoa("Raíssa", 30)
# print(dados.nome, dados.idade, sep="\n")

# Questão 02
# class Pessoa:
#     def __init__(self,nome,idade):
#         self.nome = nome
#         self.idade = idade
    
#     def apresentar(self):
#         print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
    
# dados = Pessoa("Raíssa", 30)
# print(dados.nome, dados.idade, sep="\n")
# dados.apresentar()

# Questão 03
# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

# carro1 = Carro("Toyota","Corolla-Cross", 2024)
# carro2 = Carro("Hyundei", "HB20", 2018)
# carro3 = Carro("Chevrolet", "Onix", 2020)
# print(carro1.marca, carro1.modelo, carro1.ano)
# print(carro2.marca, carro2.modelo, carro2.ano)
# print(carro3.marca, carro3.modelo, carro3.ano)

# # Questão 04
# carro1.modelo = "Corolla"
# carro2.ano = 2025
# print("*-*-*-*-*-*- Modificações -*-*-*-*-*-*")
# print(carro1.marca, carro1.modelo, carro1.ano)
# print(carro2.marca, carro2.modelo, carro2.ano)

# Questão 05 e 06
# class ContaBancaria:
#     def __init__(self,titular,saldo=0):
#         self.titular = titular
#         self.saldo = saldo

#     def __str__(self):
#         return f"A conta de {self.titular} tem o saldo de {self.saldo}"
    
#     def depositar(self, valor):
#         self.saldo += valor
#         print(f"Foi depositado {valor} na sua conta")

#     def sacar(self, valor):
#         if valor <= self.saldo:
#             self.saldo -+ valor
#             print(f"Foi sacado {valor} da sua conta")
#         else:
#             print("Saldo insuficiente")
            
        
# conta1 = ContaBancaria("Raissa", 300)
# print(conta1)
# conta1.depositar(50)
# conta1.sacar(160)

# Questão 07 e 08
# class Aluno:
#     def __init__(self, nome, nota):
#         self.nome = nome
#         self.nota = nota

#     def __str__(self):
#         return f"Aluno de nome {self.nome}, tem a nota {self.nota}."
    
# class Turma:
#     def __init__ (self,nome):
#         self.nome = nome
#         self.alunos = []

#     def adicionar_aluno(self, aluno):
#         self.alunos.append(aluno)
#         print(f"Aluno {aluno.nome}, foi adicionado a turma")

#     def lista_aluno(self):
#         print(f"\nAlunos da turma {self.nome}:")
#         for aluno in self.alunos:
#             print(aluno)

# aluno1 = Aluno("Raissa", 7.0)
# aluno2 = Aluno("José", 5.9)
# aluno3 = Aluno("Aurora", 9.0)
# turma = Turma("Python")
# turma.adicionar_aluno(aluno1)
# turma.adicionar_aluno(aluno2)
# turma.adicionar_aluno(aluno3)
# turma.lista_aluno()

# Questão 09
# class Cachorro:
#     especie = "Canis familiaris"
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def __str__(self):
#         return f"O nome do cachorro é {self.nome} e tem {self.idade} anos."

# dog1 = Cachorro("Rex", 10)
# dog2 = Cachorro("Caramelo", 2)
# print(dog1, dog2, sep="\n")
# print(Cachorro.especie)
# print(dog1.especie, dog2.especie, sep="\n")
