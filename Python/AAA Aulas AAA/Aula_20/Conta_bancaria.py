import random
from rich import print
from rich import inspect

class Conta_bancaria:
    """
    - Conta_bancaria você faz uma nova conta

    Como criar:
    Variavel = Conta_bancaria()

    Funções:
        Depositar():
            Você bota um valor que vai ser depositado na conta
        Sacar():
            Você saca um valor escolhido na conta
            !!! Se o valor for maior doque o saldo não ira funcionar !!!
    
    !!! Print() mostrarar as informações da conta !!!
    """

    

    def __init__(self, nome = "", saldo = 0):
        self.ID = random.randint(100, 10000)
        self.Nome = nome
        self.Saldo = saldo
        print("")
        print(f"Conta {self.ID} criada com sucesso")
        print(f"Saldo R$:{self.Saldo:,.2f} ; Nome {self.Nome}")
        print("")
    
    def __str__(self):
        return f"ID = {self.ID} ; Nome = {self.Nome} ; Saldo = R$:{self.Saldo:,.2f}"

    def Depositar(self, num = 0):
        self.Saldo += num
        print(f"O deposito de R$:{num:,.2f} foi depositado com sucesso.")
        print("")
    
    def Sacar(self, num):
        if self.Saldo < num:
            print(f"Saque \033[31mNEGADO\033[m, seu saldo é de R$:{self.Saldo:,.2f}")
            print("")
        else:
            self.Saldo -= num
            print(f"Saque completo! Seu saldo agora está de R$:{self.Saldo:,.2f}")
            print("")

Pessoa_1 = Conta_bancaria(nome="Miguel", saldo=1000000000)
inspect(Pessoa_1)
