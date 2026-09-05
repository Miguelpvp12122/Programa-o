from abc import ABC, abstractmethod

class Cafeteria(ABC):
    def preparar(self):
        return f"--- Iniciando preparo ---\n1. {self.fever()}\n2. {self.misturar()}\n3. {self.servi()}\n--- Bebida terminada ---"
    
    def fever(self):
        return f"Fervendo a água a 100 graus celsius"
    @abstractmethod
    def misturar(self):
        pass
    @abstractmethod
    def servi(self):
        pass

class Leite(Cafeteria):
    def misturar(self):
        return f"Passando o vapor pressurizado pelo bico do leite"
    def servi(self):
        return f"Servindo numa caneca grande, já com café"

class Cafe(Cafeteria):
    def misturar(self):
        return f"Passando o vapor pressurizado pelo pó do cafe muído"
    def servi(self):
        return f"Servindo numa xicara pequena"

class Cha(Cafeteria):
    def misturar(self):
        return f"Mergulhando o sachê de ervas na água"
    def servi(self):
        return f"Servindo numa canelca de porcerana com limão"


