# Questão 01
cadastro = {}
cadastro.update({"Nome":"Lucas"})
cadastro.update({"Idade":25})
cadastro.update({"E-mail":"lucas@email.com"})
print(cadastro)

# Questão 02
cliente = {"Nome":"Amanda", "Idade":31}
if not cliente.get("Telefone"):
    print("Não informado")

# Questão 03
livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}
for itens in livro:
    print(itens)

# Questão 04
livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}
livro.update({"Disponivel":True})
print(livro)

# Questão 05
print(livro.pop("ano"))
print(livro)

# Questão 06
compras = {"Feijão": 7.0, "Arroz": 4.0, "Açucar": 4.5}
soma = 0
for itens in compras.values():
    soma += itens
print(soma)

# Questão 07
frutas = {"maçã": 3, "banana": 5, "laranja": 2}
for itens in frutas.items():
    if itens [1] > 2:
        print(itens[0])

# Questão 08
usuario = {"login":"joaosilva"}
if "senha" not in usuario:
    usuario.update({"senha":123456})
    print(usuario)

# Questão 09
capitais = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Belo Horizonte"}
for i,x in capitais.items():
    print(f"A capital de {i}, é {x}")

# Questão 10
produto = {"nome": "Teclado", "estoque": 15}
produto["estoque"] += 10
print(produto)
