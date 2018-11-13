class Aluno:

    def __init__(self):
        self.matricula = ""
        self.nome = ""
        self.nota1 = ""
        self.faltas1 = ""
        self.nota2 = ""
        self.faltas2 = ""

    def __str__(self):
        return self.matricula + " - " + self.nome
