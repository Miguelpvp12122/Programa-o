from rich import print, inspect
from Classe_Pessoas import Funcionario, Aluno, Professor
from abc import ABC


Aluno_1 = Aluno("Jonathar", 14, "Robotica", "9ª")
Aluno_1.fazer_aniversario()
Aluno_1.fazer_matricula()
Aluno_1.estudar()

Professor_1 = Professor("Jeffeson", 40, "Matemática", "Mestre")
Professor_1.dar_aula()
Professor_1.estudar()

Funcionario_1 = Funcionario("Josecraudia", 60, "Espetora", "Primario")
Funcionario_1.bater_ponto()
Funcionario_1.estudar()
