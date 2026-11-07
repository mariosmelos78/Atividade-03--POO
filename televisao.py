# televisao.py

class Televisao:
    def __init__(self, marca, polegadas):
        self.marca = marca
        self.polegadas = polegadas
        self.ligada = False
        self.canal = 1
        self.volume = 10

    def ligar(self):
        if not self.ligada:
            self.ligada = True
            return True
        return False

    def desligar(self):
        if self.ligada:
            self.ligada = False
            return True
        return False

    def aumentar_volume(self, quantidade):
        if not self.ligada or quantidade <= 0:
            return False
        if self.volume == 100:
            return False
        
        self.volume = min(self.volume + quantidade, 100)
        return True

    def disminuir_volume(self, quantidade):
        if not self.ligada or quantidade <= 0:
            return False
        if self.volume == 0:
            return False
            
        self.volume = max(self.volume - quantidade, 0)
        return True

    def trocar_canal(self, canal):
        if not self.ligada:
            return False
        if canal < 1 or canal > 100:
            return False
            
        self.canal = canal
        return True

    def __str__(self):
        if self.ligada:
            return f"{self.marca} {self.polegadas}\" | Ligada | Canal {self.canal} | Volume {self.volume}"
        return f"{self.marca} {self.polegadas}\" | Desligada"
