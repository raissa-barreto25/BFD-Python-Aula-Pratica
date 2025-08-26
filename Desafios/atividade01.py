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

