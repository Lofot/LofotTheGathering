class Tecnica:
    def __init__(self, Nombre, danyoF, danyoM, probCrit, probAcierto, costeEnergia):
        self.Nombre=Nombre
        self.danyoFisico=danyoF
        self.danyoMagico=danyoM
        self.probCritico=probCrit
        self.probAcierto=probAcierto
        self.costeEnergia=costeEnergia

    def getNombre(self):
            return self.Nombre
    def getDanyoFisico(self):
            return int(self.danyoFisico)
    def getDanyoMagico(self):
            return int(self.danyoMagico)
    def getProbCritico(self):
            return self.probCritico
    def getProbAcierto(self):
            return self.probAcierto
    def getCosteEnergia(self):
            return self.costeEnergia