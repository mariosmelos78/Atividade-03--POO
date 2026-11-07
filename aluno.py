# aluno.py

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
        self.faltas = 0

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            return True
        return False

    def registrar_falta(self):
        self.faltas += 1

    def calcular_media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self, total_aulas):
        if not self.notas:
            return False
            
        media = self.calcular_media()
        limite_faltas = 0.25 * total_aulas
        
        if media >= 7.0 and self.faltas <= limite_faltas:
            return True
        return False

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, matricula):
        if matricula and matricula.strip():
            self.matricula = matricula
            return True
        return False

    def __str__(self):
        media = self.calcular_media()
        return f"{self.nome} ({self.matricula}) | Média {media:.2f} | Faltas {self.faltas}"
