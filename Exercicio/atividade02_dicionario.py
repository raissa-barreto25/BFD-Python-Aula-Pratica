# Questão 01
aluno = {"Nome":"", "Idade":0, "Nota":0.0}
aluno["Nome"] = "Raíssa Ruana"
aluno["Idade"] = 30
aluno["Nota"] = 8.5
print(aluno)

# Questão 02
produto = {"Nome":"Canetas", "Preço":2.5, "Estoque":100}
print("No estoque possui",produto["Estoque"],produto["Nome"],".")

# Questão 03
pessoa = {"Nome":"Carlos", "Idade":30}
pessoa.update({"Cidade":"São Paulo"})
print(pessoa)

# Questão 04
carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
print(carro)
carro.pop("ano")
print(carro)

# Questão 05
contato = {"nome": "Ana", "email": "ana@email.com"}
if "telefone" in contato:
    print("Telefone localizado")
else:
    print("Telefone não localizado")

# Questão 06
palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
contagem = {}
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
print(contagem)

# Questão 07
d = {"a": 1, "b": 2, "c": 3}
d_invert = {}
for chave,valor in d.items():
    d_invert[valor] = chave
print(d)
print(d_invert)

# Questão 08
ficha = {}
nome = str(input("Digite o nome do Aluno(a): "))
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
ficha.update({"nome":nome,"nota 1":n1, "nota 2":n2, "nota 3":n3})
print(ficha)
media = (n1 + n2 + n3) / 3
print("A média do(a) Aluno(a):",ficha["nome"], f"é: {media}.")

# Questão 09
dicio_1 = {"a":2, "b":6, "c":9}
dicio_2 = {"c":5, "d":8, "e":1}
mesclar = dicio_1 | dicio_2
print(mesclar)

# Questão 10
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
lista = [(valor, chave) for chave, valor in pontuacoes.items()]
lista.sort()
lista.reverse()
for valor,chave in lista:
    print(f"{chave}:{valor}")