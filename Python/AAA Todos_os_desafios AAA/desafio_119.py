import time
from rich import print

class Livro():
    Num_pagina = 1

    def __init__(self, titulo = "", paginas = 0):
        self.Titulo = titulo
        self.Paginas = paginas
        print(f"Você iniciou o livro {self.Titulo} agora está na Pág:1")
    
    def passar_pagina(self, Avançar = 0):
        Numero_avançado = Avançar

        while True:
            if self.Num_pagina > self.Paginas:
                print(f"[red]Você no final do livro '{self.Titulo}'[/]", flush=False)
                break
            if Avançar == 0:
                print(f"[blue]Você avançou Pág:{Numero_avançado} e agora está na Pág:[yellow]{self.Num_pagina}[/]", flush=False)
                break

            self.Num_pagina += 1
            Avançar -= 1
            print(f"Pág:{self.Num_pagina} »",end=" ", flush=True)
            time.sleep(0.5)

livro = Livro("Como ser pegador", 10)
livro.passar_pagina(4)
livro.passar_pagina(7)
