# num = input("Informe um número de 1 a 5: ")
# match num:
#     case "1":
#         print("Você digitou 1")
#     case "2":
#         print("Você digitou 2")
#     case "3":
#         print("Você digitou 3")
#     case "4":
#         print("Você digitou 4")
#     case "5":
#         print("Você digitou 5")
#     case _:
#         print("O valor informado não encontrado, informe um número de 1 a 5:")

# num = input("Informe um numero de 1 a 5")
# match num:
#     case "1"|"2"|"3"|"4"|"5":
#         print(f"Voce digitou {num}")
#     case _:
#         print("O valor informado não encontrado, informe um número de 1 a 5:")

# função

# def nome_funcao():
#     codigo

# def saudacao():
#     print("Ola! Tudo bem?")

# saudacao()

# def saudacao():
#     return"Ola! Tudo bem?"

# print(saudacao())
# msg_saudacao = saudacao
# print(msg_saudacao)

# def saudacao(num):
#     if num > 4:
#         return "Maior que 4"
#     else:
#         return "Não é maior que 4"

# print(saudacao(5))
# msg_saudacao = saudacao(2)
# print(msg_saudacao)

# def saudacao(num):
#     if num >= 4:
#         return "Maior que 4"
#     if num <= 4:
#         return "Não é maior que 4"

# print(saudacao(4))

# def soma(num1, num2):
#     print(num1+num2)

# soma(2,3)

# def soma(*nuns):
#     resultado=0
#     for numero in nuns:
#         resultado+=numero
#     return(resultado)

# print(soma(2,3,5,2,7))

# def saudacao(nome = "João", sobrenome = "Silva"):
#    return f"Ola, {nome} {sobrenome}! Tudo bem?" 

# print(saudacao())
# print(saudacao(sobrenome="Favaro"))
# print(saudacao("Fred","Favaro"))

# def soma(num1,num2): 
#    return num1 + num2

# from funcao import soma

# resultado = soma(5+3)
# print(resultado)

# def soma(num1,num2): 
#     return num1 + num2
# def multiplicacao(num1,num2):
#     return num1 * num2
# operacao = multiplicacao(soma(3,2), soma(5,8))
# print(operacao)

# def calculadora(num1,num2):
#     soma = num1+num2

#     return num1, num2, soma
# resultado = calculadora(2,4)
# print(f"A soma de {resultado[0]} + {resultado[1]} é igual a {resultado[2]}")

# def soma(*args):
#     resultado = 0
#     for num in args:
#         resultado += num
#     return resultado
# print(soma(3,4,5,6,7,1,3))

# def usuario(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f"")