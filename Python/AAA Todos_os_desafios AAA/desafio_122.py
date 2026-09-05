from rich import print
from rich.panel import Panel

class Controle():
    def __init__(self, volume=1, canal=1):
        self.Volume = volume
        self.Canal = canal
        self.Ligada = False

        while True:
            Canal_visual = "1 2 3 4 5"
            if self.Canal == 1:
                Canal_visual = "[yellow]1[/] 2 3 4 5"
            elif self.Canal == 2:
                Canal_visual = "1 [yellow]2[/] 3 4 5"
            elif self.Canal == 3:
                Canal_visual = "1 2 [yellow]3[/] 4 5"
            elif self.Canal == 4:
                Canal_visual = "1 2 3 [yellow]4[/] 5"
            elif self.Canal == 5:
                Canal_visual = "1 2 3 4 [yellow]5[/]"
            
            Volume_visual = "🟩🟩🟩🟩⬛"
            if self.Volume == 1:
                Volume_visual = "🟩⬛⬛⬛⬛"
            elif self.Volume == 2:
                Volume_visual = "🟩🟩⬛⬛⬛"
            elif self.Volume == 3:
                Volume_visual = "🟩🟩🟩⬛⬛"
            elif self.Volume == 4:
                Volume_visual = "🟩🟩🟩🟩⬛"
            elif self.Volume == 5:
                Volume_visual = "🟩🟩🟩🟩🟩"

            if self.Ligada == True:
                print(Panel(f"Canal: {Canal_visual}{"\n"}Volume: {Volume_visual}{"\n"}", title="<TV>", width=30))
            elif self.Ligada == False:
                print(Panel(f"🚫 [red]Desligada[/]", title="<TV>", width=30))
            Butão = str(input("Canal(< / >) Volume (- / +)   "))


            if Butão == "":
                break
            if Butão == "@" and self.Ligada == False:
                self.Ligada = True
            elif Butão == "@" and self.Ligada == True:
                self.Ligada = False
            if self.Ligada == True:
                if Butão == "-":
                    self.Volume -= 1
                elif Butão == "+":
                    self.Volume += 1
                elif Butão == "<":
                    self.Canal -= 1
                elif Butão == ">":
                    self.Canal += 1
            
            if self.Volume > 5:
                self.Volume = 5
            elif self.Volume < 1:
                self.Volume = 1
            
            if self.Canal > 5:
                self.Canal = 1
            elif self.Canal < 1:
                self.Canal = 5
            
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
        
controle = Controle(3, 3)

