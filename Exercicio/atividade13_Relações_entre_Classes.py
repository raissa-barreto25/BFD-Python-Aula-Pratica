# Questão 01

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Livro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero 

    def alugar_livro(self, pessoa : Pessoa):
        print(f"{pessoa.nome} alugou o livro {self.titulo}, do autor {self.autor} e do Gênero {self.genero}")

pessoa1 = Pessoa("Raíssa", 30)
livro1 = Livro("Harry Potter", "J. K. Rowling", "Fantasia")

livro1.alugar_livro(pessoa1)

# Questão 02

class Aluno:
    def __init__(self, nome, idade, serie):
        self.nome = nome
        self.idade = idade
        self.serie = serie

class Onibus:
    def __init__(self, itinerario, horario):
        self.itinerario = itinerario
        self.horario = horario

    def horario_escolar(self, aluno : Aluno):
        print(f"O(A) Aluno(a) {aluno.nome}, da serie {aluno.serie}, pega o onibus que vai para {self.itinerario} às {self.horario}")

aluno = Aluno("Aurora", 1, "Jardim de infancia")
onibus = Onibus("Caxanga", "12:30")

onibus.horario_escolar(aluno)

# Questão 03

class Funcionario:
    def __init__(self, nome, id, funcao):
        self.nome = nome
        self.id = id
        self.funcao = funcao

    def __str__(self):
        return f"{self.nome} - {self.id} - {self.funcao}"

class Departamento:
    def __init__(self, empresa, horario):
        self.empresa = empresa
        self.horario = horario
        self.funcionario = []

    def adicionar_funcionario(self, funcionario):
        self.funcionario.append(funcionario)

    def lista_funcionario(self):
        print(f"Funcionario da empresa {self.empresa} no horário {self.horario}.")
        for x in self.funcionario:
            print(f" - {x}")

f1 = Funcionario("Raíssa", "15", "Dev")
f2 = Funcionario("Helton", "02", "Adm")

empresa = Departamento("B4", "09h às 18h")

empresa.adicionar_funcionario(f1)
empresa.adicionar_funcionario(f2)

empresa.lista_funcionario()

# Questão 04

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

    def __str__(self):
        return f"{self.nome} - {self.posicao}"

class Time:
    def __init__(self, clube):
        self.clube = clube
        self.jogadores = []

    def adicionar_jogadores(self, jogador):
        self.jogadores.append(jogador)

    def lista_jogadores(self):
        print(f"Jogadores do time {self.clube}")
        for j in self.jogadores:
            print(f" - {j}")

jogador1 = Jogador("Pedro", "Goleiro")
jogador2 = Jogador("Miguel", "Volante")
jogador3 = Jogador("Arthur", "Atacante")

time1 = Time("Juniores")

time1.adicionar_jogadores(jogador1)
time1.adicionar_jogadores(jogador2)
time1.adicionar_jogadores(jogador3)

time1.lista_jogadores()

# Questão 05