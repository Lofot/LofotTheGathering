from src import Tecnica

class Personaje:
    def __init__(self, nombre, vida, armadura, resist_Magica, energia):
        self.Nombre=nombre
        self.vida=vida
        self.Armadura=armadura
        self.Resist_Magica=resist_Magica
        self.Energia=energia;
        self.Tecnicas = []

    def getNombre(self):
        return self.Nombre
    def getVida(self):
        return self.Vida
    def getTecnica(self):
        for x in self.Tecnicas:
            print(str(x.getNombre()))
    def getArmadura(self):
        return self.Armadura
    def getResist_Magica(self):
        return self.Resist_Magica
    def getEnergia(self):
        return self.Energia

    def setTecinas(self, Tecnica1, Tecnica2):
        self.Tecnicas.append(Tecnica1)
        self.Tecnicas.append(Tecnica2)
