from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome='', idade=0):
        self.Nome = nome
        self.Idade = idade
    
    def fazer_aniversario(self):
        self.Idade += 1
    
    @abstractmethod
    def estudar(self):
        pass



class Aluno(Pessoa):
    def __init__(self, nome="", idade=0, curso="", turma=""):
        super().__init__(nome, idade)
        self.Curso = curso
        self.Turma = turma

    def fazer_matricula(self):
        print(f"{self.Nome} fez a matricula")
    
    def estudar(self):
        print(f"{self.Nome} vai estudar {self.Curso} na turma {self.Turma}")

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.Especialidade = especialidade
        self.Nivel = nivel

    def dar_aula(self):
        print(f"Hoje {self.Nome} professor(a) de {self.Especialidade}, vai dar aula")
    
    def estudar(self):
        print(f"O prof:(a) {self.Nome} é nivel {self.Nivel} em {self.Especialidade}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.Cargo = cargo
        self.Setor = setor

    def bater_ponto(self):
        print(f"O funcionario(a) {self.Nome} vai bater ponto")
    
    def estudar(self):
        print(f"O funcionario(a) {self.Nome} tem o cargo de {self.Cargo} no setor {self.Setor}")
