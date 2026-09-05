from random import randint
from rich import print
from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, vida=0, nome=""):
        self.Vida = vida
        self.Nome = nome
        self.Ataques = []
    
    def receber_dano(self, dano):
        if self.Vida == 0:
            print(f"[red]{self.Nome} está morto... O dano foi de {dano}[/]")
        else:
            print(f"[green]{self.Nome}[/]({self.Vida}) levou um dano de [red]{dano}[/]")
        print("\n")
    
    def atacar(self, alvo, força):
        força = randint(1, força)
        alvo.Vida -= força
        if alvo.Vida < 0:
            alvo.Vida = 0
        alea = randint(0, 3)
        print(f"[red]{self.Nome}[/]({self.Vida}) deu [red]um {self.Ataques[alea]}[/] em [green]{alvo.Nome}[/]({alvo.Vida})")
        alvo.receber_dano(força)
    
    @abstractmethod
    def curar(self):
        pass
    
class Guerreiro(Personagem):
    def __init__(self, vida=0, nome=""):
        super().__init__(vida, nome)
        self.Ataques = ["Chute", "Soco", "Vuadora", "Deu um gancho"]
    
    def curar(self, Vida=0):
        Vida = randint(1, Vida)
        self.Vida += Vida
        print(f"{self.Nome}({self.Vida}) tomou uma poção que [green]recuperou {Vida} de vida[/]")
        print("\n")

class Mago(Personagem):
    def __init__(self, vida=0, nome=""):
        super().__init__(vida, nome)
        self.Ataques = ["Bola de fogo", "Consumiu seu sangue", "Tiro de mana", "Corte de vento"]
    
    def curar(self, Vida=0):
        Vida = randint(1, Vida)
        self.Vida += Vida
        print(f"{self.Nome}({self.Vida}) fez uma magia onde [green]recuperou {Vida} de vida[/]")
        print("\n")
