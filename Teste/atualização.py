from bd import banco
import cadastro

def atualizar_tarefa(banco):
    for id in banco:
        if banco[id] == id:
            tarefa_encontrada = id

    if tarefa_encontrada:
        for chave, valor in banco.item():
            print(f"{chave}, {valor}")

