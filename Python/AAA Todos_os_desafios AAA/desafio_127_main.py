from rich import print
from desafio_127 import *
from abc import ABC, abstractmethod

p1 = Guerreiro(1000, "Manuel Gomes")
p2 = Mago(1000, "Palhaço Caçarola")

p1.atacar(p2, 1000)
p2.atacar(p1, 1000)
p2.curar(1000)
p1.curar(1000)
p1.atacar(p2, 1000)
p2.atacar(p1, 1000)