from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, tamanho_lado=0):
        self.Tamanho_lado = tamanho_lado
    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def perimetro(self):
        return f"{self.Tamanho_lado * 4:,.2f}"
    def area(self):
        return f"{self.Tamanho_lado * self.Tamanho_lado:,.2f}"
    
class Circulo(Poligono):
    def perimetro(self):
        return f"{self.Tamanho_lado * 2  * 3.14:,.2f}"
    def area(self):
        return f"{(self.Tamanho_lado * self.Tamanho_lado)  * 3.14:,.2f}"
