from src import Tecnica

class Personaje:
    def __init__(self, nombre, vida, armadura, resist_Magica):
        self.Nombre=nombre
        self.vida=vida
        self.Tecnicas=[]
        self.Armadura=armadura
        self.Resist_Magica=resist_Magica
        self.Energia;

    def getNombre(self):
        return self.Nombre
    def getVida(self):
        return self.Vida
    def getTecnica(self):
        return self.Tecnicas
    def getArmadura(self):
        return self.Armadura
    def getResist_Magica(self):
        return self.Resist_Magica
    def getEnergia(self):
        return self.Energia

    def setTecinas(self, Tecnica1, Tecnica2):
        self.Tecnicas.append(Tecnica1, Tecnica2)
