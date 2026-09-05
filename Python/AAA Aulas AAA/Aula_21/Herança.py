from rich import print, inspect
from Classe_Pessoas import Funcionario, Aluno, Professor, Pessoa


Aluno_1 = Aluno("Jonathar", 14, "Robotica", "9ª")
Aluno_1.fazer_aniversario()
Aluno_1.fazer_matricula()

Professor_1 = Professor("Jeffeson", 40, "Matemática", "Mestre")
Professor_1.dar_aula()

Funcionario_1 = Funcionario("Josecradia", 60, "Espetora", "Primario")
Funcionario_1.bater_ponto()


