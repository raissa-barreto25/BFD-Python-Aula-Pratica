# # POO - Associação (Tipo de relação entre classes, Relação fraca, um objeto usa o outro)

# class Ferramenta:
#     def __init__(self, nome: str, marca: str, cor: str):
#         self.nome = nome
#         self.marca = marca
#         self.cor = cor

# class Aluno:
#     def __init__(self, nome:str, idade: int):
#         self.nome = nome
#         self.idade = idade
    
#     def anotar_atividade(self, ferramenta: Ferramenta):
#         print(f"O aluno {self.nome}, esta anotandoa atividade usando{ferramenta.nome} {ferramenta.marca} {ferramenta.cor}")

# aluno1 = Aluno("João", 20)
# caneta1 = Ferramenta("Caneta", "Pentel", "Preta")
# caneta2 = Ferramenta("Caneta", "Pentel", "vermelha")

# aluno1.anotar_atividade(caneta1)
# aluno1.anotar_atividade(caneta2)

# # Agregação (Tipo de relação entre classe, Relação mais forte que a associação, um objeto tem o outro, mas eles são independente.)

# class Aluno:
#     def __init__(self, nome:str):
#         self.nome = nome

# class Turma:
#     def __init__(self, nome:str):
#         self.nome = nome
#         self.alunos = []

#     def adicionar_aluno(self,aluno:Aluno):
#         self.alunos.append(aluno)

#     def lista_alunos(self):
#         for aluno in self.alunos:
#             print(f"Aluno: {aluno.nome} na turma {self.nome}")

# a1 = Aluno("Ana")
# a2 = Aluno("João")

# turma = Turma("Turma A")
# turma.adicionar_aluno(a1)
# turma.adicionar_aluno(a2)

# turma.lista_alunos()
# del turma.alunos[1]

# turma.lista_alunos()

# # Composição
# class Motor:
#     def __init__(self, potencia:int):
#         self.potencia = potencia

#     def ligar(self):
#         print(f"Motor de {self.potencia} cavalos ligado.")

# class Carro:
#     def __init__(self, modelo: str, potencia_motor: int):
#         self.modelo = modelo
#         #composição: o motor só existe dentro do carro
#         self.motor = Motor(potencia_motor)

#     def ligar_carro(self):
#         print(f"Ligando o carro {self.modelo}...")
#         self.motor.ligar()

# carro02 = Carro("Uno com escada", 1000)
# carro = Carro("Fusca", 50)
# carro.ligar_carro()
# carro02.ligar_carro()

# class Marcapasso:
#     def __init__(self, modelo):
#         self.modelo = modelo

#     def __str__(self):
#         return f"Marcapasso modelo {self.modelo}"
    
#     def bate_coracao(self):
#         print("O coração esta batendo.")

# class Pessoa:
#     def __init__(self, nome, idade, marcapasso_modelo):
#         self.nome = nome
#         self.idade = idade
#         self.marcapasso = Marcapasso(marcapasso_modelo)

#     def continuarvivo(self):
#         self.marcapasso.bate_coracao()

# pessoa1 = Pessoa("João", 33, "g-tech")
# print(pessoa1.marcapasso)