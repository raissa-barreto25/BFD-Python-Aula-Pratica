from bd import banco

class Cadastrar_Tarefa:
    def __init__(self, id, titulo, descricao, responsavel, status):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.responsavel = responsavel
        self.status = status

    def __str__(self):
        return f"Cadastrado tarefa de ID {self.id}, Titulo: {self.titulo}, Descrição: {self.descricao}, Responsável: {self.responsavel} e o Status: {self.status}."

adc = Cadastrar_Tarefa("02", "Dependente", "Pendencia de documentação de dependente", "RH", "Pendente")
adicionar = banco.append(adc)

