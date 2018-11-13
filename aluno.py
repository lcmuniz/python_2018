class Aluno:

    def __init__(self):
        self.matricula = ""
        self.nome = ""
        self.nota1 = 0
        self.faltas1 = 0
        self.nota2 = 0
        self.faltas2 = 0

    def __str__(self):
        media = (self.nota1 + self.nota2) / 2
        faltas = self.faltas1 + self.faltas2
        return 'Matrícula: ' + self.matricula + ", Nome: " + self.nome + \
               ', Média: ' + str(media) + ', Faltas: ' + str(faltas)
