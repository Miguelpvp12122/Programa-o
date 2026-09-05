class Nova_pessoa:
    #Metodo contrutor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1
        print(f"Parabéns {self.nome} você agora está com {self.idade} anos")
    def mudando_nome(self):
        self.nome = str(input("Novo nome: "))
    def mensagem(self):
        return f"Seu nome é {self.nome} e sua idade é {self.idade}"

G1 = Nova_pessoa("Miguel", 14)
G1.aniversario()
print(G1.mensagem())
