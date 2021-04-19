from src.Personaje import Personaje
from src.Tecnica import Tecnica
class Juego:

    def __init__(self, nombre):
        self.Nombre=nombre

    def carga(self):
        t1 = Tecnica("Gancho", 15, 0, 60, 85, 20)
        t2 = Tecnica("Rayo Solar", 0, 30, 20, 70, 35)
        p1 = Personaje("Moradin", 80, 30, 10, 100)
        p1.setTecinas(t1, t2)
        p1.getTecnica()

j1 = Juego("LofotTheGathering")
j1.carga()