from rich import print
from rich.table import Table

tabela = Table(title="Produtos", style="blue")

tabela.add_column("Produto")
tabela.add_column("Preço")

tabela.add_row("Cholate", "R$:10,00")
tabela.add_row("Controle", "R$:100,00")

print(tabela)
