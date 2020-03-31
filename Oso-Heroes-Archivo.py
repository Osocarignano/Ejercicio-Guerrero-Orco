class Orco:
    vida= 0.0
    ataque = 0
    defensa = 0
    resistenciaMagica = 0

    def __init__(self, vida = 1, ataque = 1, defensa = 1 ):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.resistenciaMagica = 3

    def atacar(self, enemigo:Heroe):
        if self.vida > 0:
            enemigo.vida -= (self.ataque - enemigo.defensa)
            danio = (self.ataque - enemigo.defensa)
            print ("{} ha recibido {} de daño".format(enemigo.__class__.__name__, danio))

            if enemigo.vida < 1:
                print ("{} ha muerto".format(enemigo.__class__.__name__))
                enemigo.vida = 0
        else:
            print ("{} esta muerto, no puede pelear".format(self.__class__.__name__))

class Heroe:
    vida = 0
    ataque = 0
    defensa = 0

    def atacar(self, enemigo:Orco):
        pass

class Arquero (Heroe):
    cantFlechas = 0

    def __init__(self, vida = 1, ataque = 1, defensa = 1 ):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.cantFlechas = 2

    def atacar(self, enemigo:Orco):
        if self.vida > 0:
            if self.cantFlechas > 0:
                if self.ataque <= enemigo.defensa:
                    enemigo.vida -= 1
                    danio = 1
                else:
                    enemigo.vida -= (self.ataque - enemigo.defensa)
                    danio = (self.ataque - enemigo.defensa)

                self.cantFlechas -= 1
                print ("{} ha recibido {} de daño de {}".format(enemigo.__class__.__name__, danio, self.__class__.__name__))
            else:
                print("No hay más flechas!!")

            if enemigo.vida < 1:
                print ("{} ha muerto".format(enemigo.__class__.__name__))
                enemigo.vida = 0
        else:
            print ("{} esta muerto, no puede pelear".format(self.__class__.__name__))

class Mago (Heroe):
    def __init__(self, vida = 1, ataque = 1, defensa = 1 ):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self, enemigo:Orco):
        if self.vida > 0:
            if self.ataque <= enemigo.resistenciaMagica:
                enemigo.vida -= 1
                danio = 1
            else:
                enemigo.vida -= (self.ataque - enemigo.resistenciaMagica)
                danio = (self.ataque - enemigo.resistenciaMagica)

            print ("{} ha recibido {} de daño de {}".format(enemigo.__class__.__name__, danio, self.__class__.__name__))

            if enemigo.vida < 1:
                print ("{} ha muerto".format(enemigo.__class__.__name__))
                enemigo.vida = 0
        else:
            print ("{} esta muerto, no puede pelear".format(self.__class__.__name__))

class Paladin (Heroe):
    desgaste = 50

    def __init__(self, vida = 1, ataque = 1, defensa = 1 ):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self, enemigo:Orco):
        if self.vida > 0:
            if (self.ataque + (0.1 * self.desgaste)) <= enemigo.defensa:
                enemigo.vida -= 1
                danio = 1
            else:
                enemigo.vida -= (self.ataque + (0.1 * self.desgaste)) - enemigo.defensa
                danio = self.ataque + (0.1 * self.desgaste) - enemigo.defensa

            if self.desgaste > 0:
                self.desgaste -= 1

            print ("{} ha recibido {} de daño de {}".format(enemigo.__class__.__name__, danio, self.__class__.__name__))

            if enemigo.vida < 1:
                print ("{} ha muerto".format(enemigo.__class__.__name__))
                enemigo.vida = 0
        else:
            print ("{} esta muerto, no puede pelear".format(self.__class__.__name__))

def main():
    with open("texto1.txt") as archivo:
        lista = list(archivo.readlines())
        while lista[0].lower() != "orco_escapa" and len(lista) > 1: ##ver por que no funciona
            linea = lista.pop(0).replace("\n","_")
            if len(linea) > 1:
                if linea[0:3].lower() == "ata":
                    linea = linea.split("_")
                    atacante = linea[1].lower()
                    if atacante == "orco":
                        enemigo = linea[3].lower()
                        if enemigo == "paladin":
                            orco.atacar(enemigo=paladin)
                        elif enemigo == "mago":
                            orco.atacar(enemigo=mago)
                        elif enemigo == "arquero":
                            orco.atacar(enemigo=arquero)
                    elif atacante == "mago":
                        mago.atacar(enemigo=orco)
                    elif atacante == "paladin":
                        paladin.atacar(enemigo=orco)
                    elif atacante == "arquero":
                        arquero.atacar(enemigo=orco)
                elif linea[0:3].lower() != "com" and linea[0] != " " and len(ascii(linea[0])) <= 3:
                    len(ascii(linea[0]))
                    linea = linea.replace("(", ",")
                    linea = linea.replace(")", ",")
                    linea = linea.split(",")
                    heroe = linea[0]
                    vida = int(linea[1].replace("vida=", ""))
                    ataque = int(linea[2].replace("ataque=", ""))
                    defensa = int(linea[3].replace("defensa=", ""))
                    if heroe.lower() == "orco":
                        orco = Orco(vida=vida, ataque=ataque, defensa=defensa)
                    elif heroe.lower() == "paladin":
                        paladin = Paladin(vida=vida, ataque=ataque, defensa=defensa)
                    if heroe.lower() == "mago":
                        mago = Mago(vida=vida, ataque=ataque, defensa=defensa)
                    elif heroe.lower() == "arquero":
                        arquero = Arquero(vida=vida, ataque=ataque, defensa=defensa)

        print("Batalla Terminada\n")
        print("Orco - Vida restante {}\n".format(orco.vida))
        print("Paladin - Vida restante {}\n".format(paladin.vida))
        print("Mago - Vida restante {}\n".format(mago.vida))
        print("Arquero - Vida restante {}\n".format(arquero.vida))







