class funcionario():
    empresa = "Curso em video"
    def __init__(self, Nome = "", Setor = "", Cargo = ""):
        self.nome = Nome
        self.setor = Setor
        self.cargo = Cargo
    
    def mensagem(self):
        return f"🤜🤛 Ola eu {self.nome} e sou {self.cargo} do setor {self.setor} da empresa de {self.empresa}"

funcionario.empresa = "Apple"

P1 = funcionario("Maria", "Admistrador", "Diretora")
print(P1.mensagem())

P2 = funcionario("João", "Checagem", "Diretor")
print(P2.mensagem())
