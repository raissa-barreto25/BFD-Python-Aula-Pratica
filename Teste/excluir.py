from bd import banco
import cadastro

def excluir(banco):
    if not banco:
        print("Atividade não localizada.")
        return
    
    for id in banco:
        if banco[id]== id:
            banco.remove(id)
            print("Atividade excluida com sucesso.")
            return