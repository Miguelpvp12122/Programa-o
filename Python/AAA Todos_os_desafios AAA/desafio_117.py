from rich import print
from rich.panel import Panel


class Produto():
    def __init__(self, nome = "", preço = ""):
        self.Nome = nome
        self.Preço = preço

    def tag(self):
        Nome_visual = f"{self.Nome.center(30 ," ")}"
        Nome_visual += f"{"-" * 30}"
        Preço_visual = f"R$:{self.Preço:,.2f}"
        Nome_visual += f"{Preço_visual.center(30, ".")}"
        print(Panel(f"{Nome_visual}", title="Produto", width=34))


produto = Produto(nome="Iphone", preço=2000)
produto.tag()
