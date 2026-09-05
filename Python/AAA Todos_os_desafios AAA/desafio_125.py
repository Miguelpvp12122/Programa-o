from abc import ABC, abstractmethod
from rich import print
from rich.table import Table

class Transporte(ABC):
    fator = 0
    def __init__(self, dist):
        self.Distancia = dist
        self.Frete = 0
    
    @abstractmethod
    def calc_frete():
        pass
    
class Moto(Transporte):
    fator = 0.50
    def calc_frete(self):
        self.Frete = (self.fator * self.Distancia)
        return f"[green]R$:{self.Frete:,.2f}[/]"

class Caminhao(Transporte):
    fator = 1.20
    def calc_frete(self):
        self.Frete = (self.fator * self.Distancia)
        if self.Distancia < 50:
            return "[red]Não aceitamos uma distancia menor doque 50Km[/]"
        return f"[green]R$:{self.Frete:,.2f}[/]"
    
class Drone(Transporte):
    fator = 9.50
    def calc_frete(self):
        self.Frete = (self.fator * self.Distancia)
        if self.Distancia > 10:
            return "[red]Não aceitamos uma distancia maior doque 10Km[/]"
        return f"[green]R$:{self.Frete:,.2f}[/]"

def Viagem(Num=0):
    drone = Drone(Num)
    moto = Moto(Num)
    caminhão = Caminhao(Num)

    tabela = Table(title="Tabela de frete")
    tabela.add_column("Distancia")
    tabela.add_column("Veiculo")
    tabela.add_column("Preço")

    tabela.add_row(f"{Num}Km", f"Moto", f"{moto.calc_frete()}")
    tabela.add_row(f"{Num}Km", f"Caminhão", f"{caminhão.calc_frete()}")
    tabela.add_row(f"{Num}Km", f"Drone", f"{drone.calc_frete()}")

    print(tabela)
    