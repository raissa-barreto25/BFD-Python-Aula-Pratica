# Questão 01
def saudacao():
    return"Olá, bem-vindo ao Python!"

print(saudacao())

# Questão 02
def dobro(num1):
    return num1 * 2

result = dobro(9)
print(result)

# Questão 03
def soma(num1,num2):
    return num1 + num2
operacao = soma(10,20)
print(operacao)

# Questão 04
def mensagem(nome = "Visitante"):
    return f"Olá,{nome}"
print(mensagem("Raíssa"))

# Questão 05
def operacao(num1,num2):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    return num1, num2, soma, subtracao, multiplicacao
resultado = operacao(8,4)
print(resultado)

# Questão 06
def media(num1,num2,num3):
    return(num1 + num2 + num3) / 3
resultmedia = media(4,8,6)
print(resultmedia)

# Questão 07
def dados_pessoais(**kwargs):
    for chave,valor in kwargs.items():
        print(f"{chave.capitalize()}: {valor}")
dados_pessoais(nome="Raissa", idade=30, cidade="Recife")

# Questão 08 

def calculadora(x,y,oper):
    def soma(num1,num2):
        return num1 + num2
    def subtracao(num1,num2):
        return num1 - num2
    def multi(num1,num2):
        return num1 * num2
    def divisao(num1,num2):
        return num1 / num2
    if oper == "soma":
        return soma(x , y)
    elif oper == "subtracao":
        return subtracao(x , y)
    elif oper == "multi":
        return multi(x , y)
    elif oper == "divisao":
        return divisao(x , y)
    else:
        return "Operação invalida"
print(calculadora(10,5, "subtracao"))

# Questão 09
def aplica_operacao(num1,num2,operacao):
    return operacao(num1,num2)
def soma(a,b): 
    return a + b
def multiplicacao(a,b):
    return a * b
resut_soma = aplica_operacao(3,7,soma)
print(resut_soma)
resut_multi = aplica_operacao(7,5,multiplicacao)
print(resut_multi)