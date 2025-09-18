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
class Usuario:
    def __init__ (self, nome, email):
        self.nome = nome
        self.email = email

    def saudacao(self):
        return "Olá, usuário"

    def exibir_informacoes(self):
        return f"Cliente de nome: {self.nome}, E-mail: {self.email}"

class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo

    def saudacao(self):
        return f"Olá, Cliente"
    

cliente1 = Cliente("Raíssa", "rrbsiilva@gmail.com", 500)
print(cliente1.exibir_informacoes())
print(cliente1.saudacao())
print(f"Seu saldo é {cliente1.saldo}")