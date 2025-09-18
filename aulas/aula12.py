# Herança Multipla - Herda duas ou mais classes pai/mae
class Mamifero:
    def __init__(self, especie, habitat):
        self.especie = especie
        self.habitat = habitat
    
    def __str__(self):
        return f"O mamífero da espécie {self.especie}, pode ser localizado no {self.habitat}"

    def movimentar(self):
        print("Caminhando")

    def amamentar(self):
        print("alimentando o filhote")

class AnimaisVoador:
    def __init__(self,cor):
        self.cor = cor
    def movimentar(self):
        print("Voar")

class Morcego(AnimaisVoador, Mamifero):
    def __init__(self, cor, especie, habitat):
        AnimaisVoador.__init__(self, cor)
        Mamifero.__init__(self, especie, habitat)

zubat = Morcego("Preto", "Desmodus rotundus", "pé de jambo")
print(zubat)
zubat.movimentar() 