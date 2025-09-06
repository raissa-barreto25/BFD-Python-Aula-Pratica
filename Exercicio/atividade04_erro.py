# Questão 01
# try:
#     num = int(input("Digite um numero: "))
#     print(f"Você digitou o número {num}.")
# except ValueError:
#     print("Digite um número inteiro:")

# Questão 02
# try:
#     num1 = int(input("Digite o primeiro numero: "))
#     num2 = int(input("Digite o segundo numero: "))
#     multi = num1 * num2
#     print(f"{num1} multiplicado por {num2} é {multi}.")
# except ValueError:
#     print("Digite apenas numeros inteiros")

# Questão 03
# try:
#     num = input("Digite um numero: ")
#     num_int = int(num)
# except ValueError:
#     print("Digite um número inteiro:")
# else:
#     print(f"Você digitou o número {num}.")

# Questão 04
# try:
#     arquivo = open(dados.txt,"r")
#     print(arquivo.read())
# except NameError:
#     print("Arquivo não localizado")
# finally:
#     print("Arquivo fechado")

# Questão 05
# def dividir(a, b):
#     if b == 0:
#         raise ZeroDivisionError("segundo numero não pode ser zero")
#     else:
#         return a / b
# print(dividir(2,0))

# Questão 06
# class IdadeInvalidaError(Exception):
#     pass
# def cadastrar_idade(idade):
#     if idade <= 0:
#         raise IdadeInvalidaError("Idade não pode ser menor que zero")
#     else:
#         return f"Sua idade é {idade}"
# print(cadastrar_idade(-1))

# Questão 07
# try:
#     num1 = int(input("Informe o primeiro numero:"))
#     num2 = int(input("Informe o segundo numero:"))
#     divisao = num1/num2
#     print(divisao)
# except ZeroDivisionError:
#     print("segundo numero não pode ser zero")
# except ValueError:
#     print("Informe apenas numeros")

# Questão 08
# try:
#     num = input("Digite um numero: ")
#     num_int = int(num)
# except ValueError:
#     print("Informe apenas numeros")
# else:
#     if num_int % 2 == 0:
#         print("O numero digitado é par.")
#     else:
#         print("O numero digitado é impar")
# finally:
#     print("Fim do programa")

# Questão 09
def sacar(saldo, valor):
    class SaldoInsuficienteError(Exception):
        pass
    try:
        if valor > saldo:
            raise SaldoInsuficienteError("Saldo Insuficiente.")
        novo_saldo = saldo - valor
        print(f"Valor retirado com sucesso! Novo saldo é {novo_saldo}")
        return novo_saldo
    except SaldoInsuficienteError:
        print("Saldo insuficiente!")
    except ValueError:
        print("Erro: você deve digitar um número válido.")

saldo_atual = 1000
valor_saque = int(input("Digite o valor de retirada: "))
sacar(saldo_atual, valor_saque)