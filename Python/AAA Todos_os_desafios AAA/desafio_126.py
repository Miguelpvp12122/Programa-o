from abc import ABC
from rich.panel import Panel
from rich import print


class Funcionario():
    def __init__(self, nome="", salario_bruto=0):
        self.Nome = nome
        self.Salario_bruto = salario_bruto
        self.Salario = 0
        self.Salario_min = 1612
        self.Salario_min_quant = 0
        self.INSS = 7.5
    
    def calcular_salario():
        pass

    def analisar_salario(self):
        return Panel(f"O salario de [blue]{self.Nome}[/] ([purple]{__class__.__name__}(a)[/]) é de [green]{self.Salario:,.2f}[/] e corresponde a [red]{self.Salario_min_quant:,.1f}[/] salarios minimo", width=55)


class Funcionario_Horista(Funcionario):
    def __init__(self, nome="", horas_trabal=0, valor_hora=0):
        super().__init__(nome)
        self.Valor_hora = valor_hora
        self.Horas_trabal = horas_trabal

    def calcular_salario(self):
        self.Salario = self.Valor_hora * self.Horas_trabal
        self.Salario -= (self.Salario * (self.INSS / 100))
        Salario_visual = self.Salario
        while True:
            if Salario_visual > 1612:
                self.Salario_min_quant += 1
                Salario_visual -= 1612
            elif Salario_visual > 161.2:
                self.Salario_min_quant += 0.1
                Salario_visual -= 161.2
            else:
                break


class Funcionario_Mensarista(Funcionario):
    def __init__(self, nome="", salario_bruto=0):
        super().__init__(nome, salario_bruto)

    def calcular_salario(self):
        self.Salario = self.Salario_bruto
        self.Salario -= (self.Salario * (self.INSS / 100))
        Salario_visual = self.Salario
        while True:
            if Salario_visual > 1612:
                self.Salario_min_quant += 1
                Salario_visual -= 1612
            elif Salario_visual > 161.2:
                self.Salario_min_quant += 0.1
                Salario_visual -= 161.2
            else:
                break


f1 = Funcionario_Horista("CJ", 200, 100)
f1.calcular_salario()
print(f1.analisar_salario())

f2 = Funcionario_Mensarista("Flasiuda", 9500)
f2.calcular_salario()
print(f2.analisar_salario())





