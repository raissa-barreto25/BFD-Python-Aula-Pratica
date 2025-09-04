# try, except, else, finally, raise
# try:
#     num1 = int(input("Informe o primeiro numero:"))
#     num2 = int(input("Informe o segundo numero:"))
#     divisao = num1/num2
#
# except ZeroDivisionError:    (Pode adicionar mais de um except)
#     print("Algo errado não está certo.")
# except ValueError:
#     print("Informe apenas numeros")
# except:
#     print("Entre em contato com o suporte")
# else:
#     print("Nenhum erro")
# finally: (roda mesmo com o erro)(Pode ser utilizado para fechar arquivos)
#     print("Terminando o try")
# print("Depois da divisão")


# arquivo = open("nome do arquivo","r") (r para ler o arquivo)
# print(arquivo.read())
# arquivo.close()

# raise(chamar o erro antes de acontecer)
#     num1 = int(input("Informe o primeiro numero:"))
#     num2 = int(input("Informe o segundo numero:"))
#     if num2 <=:
#         raise ZeroDivisionError("segundo numero não pode ser zero")
#     soma = num1/num2

# idade = int(input("Informe sua idade:"))
# if idade <= 0:
#     raise ValueError("Idade não pode ser menor que zero")

# Criação de um tipo de erro
# class erroIdade(Exception):
#     pass
# idade = int(input("Informe sua idade:"))
# if idade <= 0:
#     raise erroIdade("Idade não pode ser menor que zero")

# class erroIdade(Exception):
#     pass
# try:
#    idade = int(input("Informe sua idade:"))
#    if idade <= 0:
#       raise erroIdade("Idade não pode ser menor que zero")
# except erroIdade as erro:
#    print(erro)
#    print(type(erro).__name__,":", erro)

