# Questão 01
# class Usuario:
#     def __init__ (self, nome, email):
#         self.nome = nome
#         self.email = email

# class Cliente(Usuario):
#     ...

#     def __str__(self):
#         return f"Cliente de nome: {self.nome}, E-mail: {self.email}"

# cliente1 = Cliente("Raíssa", "rrbsiilva@gmail.com")
# print(cliente1)

# Questão 02
# class Usuario:
#     def __init__ (self, nome, email):
#         self.nome = nome
#         self.email = email

#     def exibir_informacoes(self):
#         return f"Cliente de nome: {self.nome}, E-mail: {self.email}"

# class Cliente(Usuario):
#     ...

# cliente1 = Cliente("Raíssa", "rrbsiilva@gmail.com")
# print(cliente1.exibir_informacoes())


# Questão 03 
# class Usuario:
#     def __init__ (self, nome, email):
#         self.nome = nome
#         self.email = email

#     def saudacao(self):
#         return "Olá, usuário"


#     def exibir_informacoes(self):
#         return f"Cliente de nome: {self.nome}, E-mail: {self.email}"

# class Cliente(Usuario):
#     ...

#     def saudacao(self):
#         return "Olá, Cliente"

# cliente1 = Cliente("Raíssa", "rrbsiilva@gmail.com")
# print(cliente1.exibir_informacoes())
# print(cliente1.saudacao())

# Questão 04
# class Usuario:
#     def __init__ (self, nome, email):
#         self.nome = nome
#         self.email = email

#     def saudacao(self):
#         return "Olá, usuário"

#     def exibir_informacoes(self):
#         return f"Cliente de nome: {self.nome}, E-mail: {self.email}"

# class Cliente(Usuario):
#     def __init__(self, nome, email, saldo):
#         super().__init__(nome, email)
#         self.saldo = saldo

#     def saudacao(self):
#         return f"Olá, Cliente"
    

# cliente1 = Cliente("Raíssa", "rrbsiilva@gmail.com", 500)
# print(cliente1.exibir_informacoes())
# print(cliente1.saudacao())
# print(f"Seu saldo é {cliente1.saldo}")

# # Questão 05
# class Funcionario(Usuario):
#     def __init__(self, nome, email, funcao):
#         super().__init__(nome, email)
#         self.funcao = funcao
    
# class Gerente(Funcionario):
#     def __init__(self, nome, email, funcao, setor):
#         super().__init__(nome, email, funcao)
#         self.setor = setor

#     def __str__(self):
#         return f"Olá, Gerente {self.nome},E-mail: {self.email}, Cargo: {self.funcao}, Setor: {self.setor}"

# gerente_departamento = Gerente("Raissa", "rrbsiilva@gmail.com", "Gerente", "TI")
# print(gerente_departamento)

# Questão 06 e 07
# class Autenticacao:
#     def login(self):
#         return "Usuario Autenticado com Sucesso."
    
#     def status(self):
#         return "Status da Autenticação: OK"
    
# class Permissao:
#     def verificar_permissao(self):
#         return "Permissão Concedida"
    
#     def status(self):
#         return "Status de Permissão: OK"
    
# class Administrador (Autenticacao, Permissao):
#     ...

# admin = Administrador()
# admin.login()
# admin.verificar_permissao()
# print(Administrador.__mro__)