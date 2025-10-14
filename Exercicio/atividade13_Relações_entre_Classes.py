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

class Departamento:
    def __init__(self, area_atuacao, horario):
        self.area_atuacao = area_atuacao
        self.horario = horario
