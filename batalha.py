import json

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} Ataca {inimigo.nome} e Causa {self.ataque} de Dano!")

    def __str__(self):
        return f"{self.nome} {self.vida}"

class Guerreiro(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)

    def especial(self, inimigo):
        SpecialDmg = self.ataque+15
        inimigo.vida -= SpecialDmg
        print(f"{self.nome} usa Golpe Poderoso em {inimigo.nome} e Causa {SpecialDmg} de Dano!")


class Mago(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)

    def especial(self):
        Cura = 25
        self.vida += Cura
        print(f"{self.nome} usa Cura e Ganha {Cura} Pontos de Vida!")

class Arqueiro(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)

    def especial(self, inimigos):
        SpecialDmg = 15
        for inimigo in inimigos:
            if(inimigo == self):
                pass
            else:
                inimigo.vida -= SpecialDmg
        print(f"{self.nome} usa Chuva de Flechas e Causa {SpecialDmg} de Dano a Todos os Inimigos!")
        

def importar_personagens(caminho):
    chars = []

    with open(caminho, 'rt') as ficheiro:
        data = json.load(ficheiro)

    #print(data)

    for char in data:
        if char["classe"] == "Guerreiro":
            chars.append(Guerreiro(char["nome"], char["vida"], char["ataque"]))
        elif char["classe"] == "Arqueiro":
            chars.append(Arqueiro(char["nome"], char["vida"], char["ataque"]))
        elif char["classe"] == "Mago":
            chars.append(Mago(char["nome"], char["vida"], char["ataque"]))

    return chars, len(chars)

def ordenar_personagens_por_vida(personagens):
    return sorted(personagens, key=lambda char: char.vida)
    #return personagens
     

personagens, num_personagens = importar_personagens('personagens.json')
print(f"{num_personagens} Personagens Entram em Batalha!")

personagens = ordenar_personagens_por_vida(personagens)

print(personagens[0])
print(personagens[1])
print(personagens[2])

personagens[0].atacar(personagens[1])
print(personagens[1])

personagens[1].atacar(personagens[2])
print(personagens[2])

personagens[2].atacar(personagens[0])
print(personagens[0])

personagens[0].especial()
print(personagens[0])

personagens[1].especial([personagens[0], personagens[1]])
print(personagens[0])
print(personagens[1])

personagens[2].especial(personagens[1])
print(personagens[1])