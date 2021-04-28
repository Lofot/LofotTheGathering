from src.Personaje import Personaje
from src.Tecnica import Tecnica
from random import randint
class Juego:

    def __init__(self, nombre):
        self.nombre=nombre
        self.p1= Personaje;
        self.t1= Tecnica;
        self.t2= Tecnica;
        self.p2= Personaje;
        self.personajes=[]
        self.jugador1=Personaje;
        self.jugador2=Personaje;

    def carga(self):
        self.t1 = Tecnica("Gancho", 50, 0, 60, 85, 20)
        self.t2 = Tecnica("Rayo Solar", 0, 50, 20, 70, 35)
        self.p1 = Personaje("Moradin", 200, 30, 10, 100)
        self.p2= Personaje("Gandalf", 200, 30, 10, 100)
        self.p3 = Personaje("Tofol", 100000, 100000, 1000000, 1000000000)

        self.personajes.append(self.p1)
        self.personajes.append(self.p2)
        self.personajes.append(self.p3)
        self.p1.setTecinas(self.t1, self.t2)
        self.p2.setTecinas(self.t1, self.t2)
        self.p3.setTecinas(self.t1, self.t2)
        #self.p1.getTecnica()

    def juego(self):
        print("-------------------------------------------------\n _            __      _     _______ _\n"+
              "| |          / _|    | |   |__   __| |\n"+
"| |     ___ | |_ ___ | |_     | |  | |__   ___\n"+
"| |    / _ \|  _/ _ \| __|    | |  | '_ \ / _ \ \n"+
"| |___| (_) | || (_) | |_     | |  | | | |  __/ \n"+
"|______\___/|_| \___/ \__|    |_|  |_| |_|\___|\n" +
  " _____        _   _               _ \n"+
 "/  ____|     | | | |             (_)\n"+
"| |  __  __ _| |_| |__   ___ _ __ _ _ __   __ _ \n"+
"| | |_ |/ _` | __| '_ \ / _ \ '__| | '_ \ / _` |\n"+
"| |__| | (_| | |_| | | |  __/ |  | | | | | (_| |\n"+
"\_____|\__,_|\__|_| |_|\___| _|  |_|_| |_|\__, |\n"+
                                           "\t\t\t\t\t\t\t\t\t\t   __/ |\n"+
                                          "\t\t\t\t\t\t\t\t\t\t  |___/"+"\n-------------------------------------------------" )
        self.listadoPersonajes()
        self.seleccion()

    def seleccion(self):

        j=input("-------------------------------------------------\n"+ "Adalid, por favor, seleccione un personaje: ")
        if j=="1":

            self.p1.descPersonaje()
            eleccion=input("Estas seguro que deseas utilizar este campeon?\n1-- Si\n2-- No\nRespuesta: ")
            if eleccion=="1":
                self.jugador1=self.p1
                print( "El jugador ha seleccionado a: " + str(self.jugador1.getNombre()))
                print("-------------------------------------------------")

            elif eleccion=="2":
                print("-------------------------------------------------\nVolviendo a cargar los personajes...\n-------------------------------------------------")
                self.listadoPersonajes()
                self.seleccion()
        elif j=="2":

            self.p2.descPersonaje()
            eleccion = input("Estas seguro que deseas utilizar este campeon?\n1-- Si\n2-- No\nRespuesta: ")
            if eleccion == "1":
                print("El jugador ha seleccionado a: " + str(self.jugador1.getNombre()))
                print("-------------------------------------------------")
                self.jugador1=self.p2
            elif eleccion == "2":
                print(
                    "-------------------------------------------------\nVolviendo a cargar los personajes...\n-------------------------------------------------")
                self.listadoPersonajes()
                self.seleccion()

        elif j=="3":

            self.p3.descPersonaje()
            eleccion = input("Estas seguro que deseas utilizar este campeon?\n1-- Si\n2-- No\nRespuesta: ")
            if eleccion == "1":
                print("El jugador ha seleccionado a: " + str(self.jugador1.getNombre()))
                print("-------------------------------------------------")
                self.jugador1=self.p3
            elif eleccion == "2":
                print(
                    "-------------------------------------------------\nVolviendo a cargar los personajes...\n-------------------------------------------------")
                self.listadoPersonajes()
                self.seleccion()
        else :
            print ("Opcion incorrecta!")
            self.seleccion()

    def usarTecnica(self, jugador, enemigo):
        print("-------------------------------------------------")
        print("Tecnicas de: " + jugador.getNombre())
        jugador.getTecnica()

        tec=input("Seleccione una tecnica: ")
        if tec=="1":
            if (jugador.getTecnica1(0).getDanyoFisico()) > 0:
                enemigo.recibirDanyoFisico(int(jugador.getTecnica1(0).getDanyoFisico()))
            elif (jugador.getTecnica1(0).getDanyoMagico()) > 0:
                enemigo.recibirDanyoMagico(int(jugador.getTecnica1(0).getDanyoMagico()))
            print("Tecnica realizada correctamente, la vida de " + enemigo.getNombre() +  " es: " + str(enemigo.getVida()))

        elif tec=="2":
            if (jugador.getTecnica1(1).getDanyoFisico()) > 0:
                enemigo.recibirDanyoFisico(int(jugador.getTecnica1(1).getDanyoFisico()))
            elif (jugador.getTecnica1(1).getDanyoMagico()) > 0:
                enemigo.recibirDanyoMagico(int(jugador.getTecnica1(1).getDanyoMagico()))
            print("Tecnica realizada correctamente, la vida de " + enemigo.getNombre() +  " es: " + str(enemigo.getVida()))




    def lucha(self):
        print("Que empiecen la arena")
        self.eleccionBoss()
        rondas=0;
        while self.jugador1.getVida()>0 and self.jugador2.getVida()>0:
            rondas=rondas+1;
            print("-------------------------------------------------\nRonda: "+ str(rondas) + "\n-------------------------------------------------\n"+self.jugador1.getNombre() + " VS " + self.jugador2.getNombre())
            self.usarTecnica(self.jugador1, self.jugador2)

            if (self.jugador2.getVida()>0):
                self.bossAttacks()

    def eleccionBoss(self):
        r=randint(1,3)
        if r==1:
            self.jugador2=self.p1
        elif r==2:
            self.jugador2=self.p2
        elif r==3:
            self.jugador2=self.p3
    def bossAttacks(self):
        r=randint(1,2)
        print("-------------------------------------------------\nTurno de: "+self.jugador2.getNombre()+ " enemigo\n-------------------------------------------------")
        if r==1:
            if (self.jugador2.getTecnica1(0).getDanyoFisico()) > 0:
                self.jugador1.recibirDanyoFisico(int(self.jugador2.getTecnica1(0).getDanyoFisico()))
                print(self.jugador2.getNombre() +" va a usar "+ self.jugador2.getTecnica1(0).getNombre() )
            elif (self.jugador1.getTecnica1(0).getDanyoMagico()) > 0:
                self.jugador1.recibirDanyoMagico(int(self.jugador2.getTecnica1(0).getDanyoMagico()))
                print(self.jugador2.getNombre() + " va a usar " + self.jugador2.getTecnica1(0).getNombre())

            print("Tecnica realizada correctamente, la vida de " + self.jugador1.getNombre() +  " es: " + str(self.jugador1.getVida()))
        elif r==2:
            if (self.jugador2.getTecnica1(1).getDanyoFisico()) > 0:
                self.jugador1.recibirDanyoFisico(int(self.jugador2.getTecnica1(1).getDanyoFisico()))
                print(self.jugador2.getNombre() + " va a usar " + self.jugador2.getTecnica1(1).getNombre())
            elif (self.jugador1.getTecnica1(1).getDanyoMagico()) > 0:
                self.jugador1.recibirDanyoMagico(int(self.jugador2.getTecnica1(1).getDanyoMagico()))
                print(self.jugador2.getNombre() + " va a usar " + self.jugador2.getTecnica1(1).getNombre())

            print("Tecnica realizada correctamente, la vida de " + self.jugador1.getNombre() + " es: " + str(self.jugador1.getVida()))

    def listadoPersonajes(self):
        count=0
        print("Personajes:")
        print("-------------------------------------------------")
        for x in self.personajes:
            count = count + 1
            print(str(count) + " - " + str(x.getNombre()))
        print("-------------------------------------------------")

j1 = Juego("LofotTheGathering")
j1.carga()
j1.juego()
j1.lucha()