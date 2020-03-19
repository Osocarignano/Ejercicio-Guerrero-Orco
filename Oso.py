
class Guerrero:
    vida = int,
    vidainicial = int,
    ataque = int,
    defensa = int,
    curacion = int

    def __init__(self, vida=1, vidainicial=1, ataque=1, defensa=1,curacion=1):
        self.vida = vida
        self.vidainicial = vidainicial
        self.ataque = ataque
        self.defensa = defensa
        self.curacion = curacion

        print("Guerrero - Vida {}/{} - Ataque {} - Defensa {} - Curación {}".format(str(self.vida), str(self.vidainicial),
            str(self.ataque), str(self.defensa), str(self.curacion)))

    def atacar(self, Orco):
        if self.ataque - Orco.defensa < 1:
            Orco.vida += -1
            print ("{} // recibio 1 de daño".format(Orco.__class__.__name__))
        else:
            Orco.vida += -(self.ataque - Orco.defensa)
            print ("{} // recibio {} de daño".format(Orco.__class__.__name__, (self.ataque - Orco.defensa)))

        if Orco.vida < 1:
            return "{} esta mueeeeerto... muerto muerto muerto".format(Orco.__class__.__name__)

    def curar (self):
        if self.vida + self.curacion > self.vidainicial:
            daniocurado = self.vidainicial - self.vida
            self.vida = self.vidainicial
        else:
            daniocurado = self.curacion
            self.vida += self.curacion
        return "Vida recuperada {}".format(str(daniocurado))

class Orco:
    vida = int,
    ataque = int,
    defensa = int

    def __init__ (self, vida=1, ataque=1, defensa=1):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        print("Orco - Vida {} - Ataque {} - Defensa {}".format(str(self.vida), str(self.ataque), str(self.defensa)))

    def atacar (self, Guerrero):
        if self.ataque - Guerrero.defensa < 1:
            Guerrero.vida += -1
            print("{} // recibio 1 de daño".format(Guerrero.__class__.__name__))
        else:
            Guerrero.vida += -(self.ataque - Guerrero.defensa)
            print("{} // recibio {} de daño".format(Guerrero.__class__.__name__, (self.ataque - Guerrero.defensa)))

        if Guerrero.vida < 1:
            return "{} esta mueeeeerto... muerto muerto muerto".format(Guerrero.__class__.__name__)





