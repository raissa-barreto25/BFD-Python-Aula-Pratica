# Questão 01(Criar uma classe pessoa com suas caracteristicas e uma classe funcionario que herde pessoa).
class Pessoa:
    def __init__(self, nome, dn, endereco, cpf):
        self.nome = nome
        self.dn = dn
        self.endereco = endereco
        self.__cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome}, Data de nascimento: {self.dn}, Endereço: {self.endereco}, CPF: {self.__cpf}."

class Funcionario(Pessoa):
    def __init__(self, nome, dn, endereco, cpf, cargo, salario):
        super().__init__(nome, dn, endereco, cpf)
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{super().__str__()}, Cargo: {self.cargo}, Salario: {self.salario}"

    
funcionario1 = Funcionario("Raissa", "25/12/1994", "Rua A", 12345678910, "Estagiaria", 500)
print(funcionario1)

# Questão 02 
class Computador:
    def __init__(self, modelo, processador, quantidade_de_memoria, departamento):
        self.modelo = modelo
        self.processador = processador
        self.quantidade_de_memoria = quantidade_de_memoria
        self.departamento = departamento
    
    def __str__(self):
        return f"Computador de modelo: {self.modelo}, processador: {self.processador}, memoria: {self.quantidade_de_memoria}, do departamento: {self.departamento}"
    
class Placa(Computador):
    def __init__(self, modelo, processador, quantidade_de_memoria, departamento, placa_de_video):
        super().__init__(modelo, processador, quantidade_de_memoria, departamento)
        self.placa_de_video = placa_de_video

    def __str__(self):
        return f"{super().__str__()}, Placa de Video: {self.placa_de_video}"

comput = Placa("HP 256R G9", "Intel® Core™ i3", "256GB SSD", "Notebook ", "ntel Iris Xe Graphics G7 (80 EUs)")
print(comput)