# 1° questão
# num = int(input("Digite um número: "))

# if num % 2 == 0 :
#     print("Esse número é par!")
# else: 
#     print("Esse número é impar")
#****************************************

#2° questão
# nota = float(input("Digite a nota do aluno: "))

# if nota >= 7.0:
#     print("Aprovado")
# elif nota >= 5.0:
#     print("Recuperação")
# else:
#     print("Reprovado")
#*****************************************

#3° Questão
# num1 = int(input("Digite o primeiro numero: "))
# num2 = int(input("Digite o segundo numero: "))

# if num1 >= num2:
#     print(f"{num1} é maior/igual {num2}")
# else:
#     print(f"{num2} é maior/igual {num1}")
#***********************************************

#4° Questão
# idade = int(input("Me informe sua idade: "))

# if idade <= 12:
#     print("Criança")
# elif idade <= 17:
#     print("Adolescente")
# elif idade <= 64:
#     print("Adulto")
# else: 
#     print("Idoso")
#******************************************

#5° Questão 
# for x in range(1,11):
#     print(x)
#****************************************

#6° Questão
# num = int(input("Digite um numero: "))
# for i in range(11):
#     resultado = num * i
#     print(f"{num} x {i} : {resultado}")
#***********************************************

#7° Questão
soma = 0
while True:
    x = int(input('Informe um numero: '))
    if x == 0:
        break
    else:
         print(x)
    soma += x
print("A soma dos numero é: ",soma)
