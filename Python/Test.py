class Calc_Raio():
    def __init__(self, numero):
        self.Numero = numero
    
    def calcular_Perímetro(self):
        resultado = self.Numero * 2 * 3.14
        return f"O perímetro da circunferencia sendo o raio {self.Numero} é {resultado}"



Test = Calc_Raio(numero=10)
print(Test.calcular_Perímetro())
