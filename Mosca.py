class Guerrero:
    vida = int
    ataque = int
    defensa = int
    curacion = int
    vida_inicial = int

    def __init__(self, vida=0, ataque=0, defensa=0, curacion=0, vida_inicial=0):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.curacion = curacion
        self.vida_inical = vida

        print("La vida del Guerrero es {} La vida maxima del Guerrero es {} El ataque del Guerrero es {} La defensa del Guerrero es {} curacion:{}".format(str(self.vida), str(self.vida_inical),
                                                                                                                                                           str(self.ataque), str(self.defensa), str(self.curacion)))

    def atacar(self, Orco):
        if Orco.defensa > self.ataque:
            Orco.vida = Orco.vida - 1
            print("La vida del orco es {} ".format(str(Orco.vida)))
        else:
            Orco.vida = Orco.vida - (self.ataque - Orco.defensa)
            print("La vida del orco es {} ".format(str(Orco.vida)))

        if Orco.vida <= 0:
            print("El Orco esta muerto")
            print("Gano el Guerrero")
        else:
            print("continua..?")

    def curar(self):
        self.vida += self.curacion
        return "Vida recuperada {}".format(str(self.vida))


class Orco:
    vida = int
    ataque = int
    defensa = int

    def __init__(self, vida=0, ataque=0, defensa=0):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

        print("La vida del Orco es {} El ataque del Orco es {} La defensa del Orco es {}".format(
            str(self.vida), str(self.ataque), str(self.defensa)))

    def atacar(self, Guerrero):
        if Guerrero.defensa > self.ataque:
            Guerrero.vida = Guerrero.vida - 1
            print("La vida del Guerrero es {} ".format(str(Guerrero.vida)))
        else:
            Guerrero.vida = Guerrero.vida - (self.ataque - Guerrero.defensa)
            print("La vida del Guerrero es {} ".format(str(Guerrero.vida)))

        if Guerrero.vida <= 0:
            print("El Guerro esta muerto")
            print("El Orco gano")
        else:
            print("continua..?")
