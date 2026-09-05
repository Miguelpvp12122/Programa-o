from rich import print

class Caneta():
    def __init__(self, cor=""):
        self.Cor = cor
        self.Tampada = True

        if self.Cor == "vermelho" or self.Cor == "Vermelho":
            self.Cor = "red"
        elif self.Cor == "Preto" or self.Cor == "preto":
            self.Cor = "black"
        elif self.Cor == "Amarelo" or self.Cor == "amarelo":
            self.Cor = "yellow"

    def Destanpar(self):
        if self.Tampada == True:
            self.Tampada = False
        else:
            self.Tampada = True
        
    def Escrever(self, escrever=""):
        if self.Tampada == False:
            print(f"[{self.Cor}]{escrever}[/]", end=" ", flush=True)
        else:
            print("[red]Destanpe a caneta pra escrever![/]")
    
    def Quebrar_linha(self, quantas=0):
        for linhas in range(0, quantas):
            print("")


C1 = Caneta("preto")
C1.Destanpar()
C1.Escrever("Eu escrever preto")
C1.Quebrar_linha(2)

C2 = Caneta("Vermelho")
C2.Destanpar()
C2.Escrever("Cor vermelho")

    
