from rich import print
from rich.panel import Panel

class churrasco():
    def __init__(self, titulo, quantidade):
        self.Titulo = titulo
        self.Quantidade = quantidade 
    
    def analise(self):
        tot = self.Quantidade

        Kg = 0
        g = 0

        dinheiro = 0
        Kilos = 0

        if tot > 0:
            while True:
                Kilos += 400
                tot -= 1
                if tot == 0:
                    break
        
        kilo = Kilos
        if kilo > 1000:
            while True:
                Kg += 1
                kilo -= 1000
                if kilo < 1000:
                    break


        if Kilos > 0:
            while True:
                Kilos -= 1
                dinheiro += 0.0824
                if Kilos == 0:
                    break
        
        mensagem = ""
        if kilo > 0:
            mensagem =  f"e {kilo}g"
        
        print(Panel(f"[red]Analisando {self.Titulo}[/] com [blue]{self.Quantidade}[/] convidados{"\n"}Cada participante vai comer 400g e cada Kg custa R$:82.40{"\n"}Recomendo [blue]{Kg}.{kilo}Kg[/] {"\n"}O custo geral vai ser de [blue]R$:{dinheiro:,.2f}[/]{"\n"}Cada pessoa pagará [blue]R$:{dinheiro/self.Quantidade:,.2f}[/]", title=f"{self.Titulo}", width=70))

a = churrasco("Churras", 15)
a.analise()
