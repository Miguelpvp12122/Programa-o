class Pessoa:
    def __init__(self, nome='', idade=0):
        self.Nome = nome
        self.Idade = idade
    
    def fazer_aniversario(self):
        self.Idade += 1



class Aluno(Pessoa):
    def __init__(self, nome="", idade=0, curso="", turma=""):
        super().__init__(nome, idade)
        self.Curso = curso
        self.Turma = turma

    def fazer_matricula(self):
        print(f"{self.Nome} fez a matricula")

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.Especialidade = especialidade
        self.Nivel = nivel

    def dar_aula(self):
        print(f"Hoje {self.Nome} professor de {self.Especialidade}, vai dar aula")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.Cargo = cargo
        self.Setor = setor

    def bater_ponto(self):
        print(f"O funcionario {self.Nome} vai bater ponto")
