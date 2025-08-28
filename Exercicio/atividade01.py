# Questão 01
livros = ["Harry Potter", "Trono de Vidro", "Verity"]
print(livros)

# Questão 02
livros = ["Harry Potter", "Trono de Vidro", "Verity"]
print(livros[0], livros[-1])

# Questão 03
livros.append("O Principe Cruel")
livros.append("Fourth Wind")
print(livros)

# Questão 04
livros.insert(1, "Duna")
print(livros)

# Questão 05
if "Silencio dos inocentes" in livros:
    livros.remove("Silencio dos inocentes")
    print("Livro removido")
else:
    print("Livro não encontrado.")

# Questão 06
numeros = [1, 2, 3, 2, 4, 2, 5]
qtd = numeros.count(2)
print(f"O numero 2 aparece {qtd}.")

# Questão 07
for livros in livros:
    print(f"O livro {livros} é interessante")

# Questão 08
idades = [12, 18, 25, 14, 30]
for idades in idades:
    if idades >= 18:
        print(idades)

# Questão 09
valores = [10, 20, 30, 40]
result = 0
for i in valores:
    result += i
print(f"O resultado da soma dos valores {valores} é: {result}!")

# Questão 10
notas = []  

print("Digite as 3 notas do aluno 1:")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
notas.append([n1, n2, n3])  

print("\nDigite as 3 notas do aluno 2:")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
notas.append([n1, n2, n3])  
print("\nNotas armazenadas:", notas)

media1 = sum(notas[0]) / 3
media2 = sum(notas[1]) / 3

print(f"Média do aluno 1: {media1:.2f}")
print(f"Média do aluno 2: {media2:.2f}")

# Questão 11
import numpy as np

tabuleiro = [["[ ]" for _ in range(8)] for _ in range(8)]
pecas = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]
tabuleiro[0] = pecas
tabuleiro[1] = ["pea"] * 8
tabuleiro[6] = ["pea"] * 8
tabuleiro[7] = pecas
tabuleiro_np = np.array(tabuleiro)

print(tabuleiro_np)