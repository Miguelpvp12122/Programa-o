from rich import print
from rich.panel import Panel

class Gamer():
    def __init__(self, nome="", nick=""):
        self.Nome = nome
        self.Nick = nick
        self.Favoritos = list()
    
    def Adicionar(self, jogo=""):
        self.Favoritos.append(jogo)
        self.Favoritos.sort()
    def Mostrar(self):
        
        conteudo = f"Nome real: {self.Nome}"
        conteudo += f"{"\n"}Jogos favoritos:"
        for Jogo in self.Favoritos:
                conteudo += f"\n🎮 [blue]{Jogo}[/]"
        
        print(Panel(f"{conteudo}", title=f"Nick = <{self.Nick}>", width=40))

Jogador = Gamer("Miguel", "Bosta liquida")
Jogador.Adicionar("Hollow knight")
Jogador.Adicionar("Monster hunter world")
Jogador.Adicionar("Minecraft")
Jogador.Mostrar()
