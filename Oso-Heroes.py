class Orco:
    vida= float,
    defensa = int,
    resitenciaMagica = int,

    def __init__(self, vida = 1, defensa = 1, resitenciaMagica = 1 ):
        self.vida = vida
        self.defensa = defensa
        self.resitenciaMagica = resitenciaMagica
        print ('{} - Vida {} - Defensa {} - Resist. Mágica {}'.format(self.__class__.__name__, str(self.vida),
                                                                     str(self.defensa), str(self.resitenciaMagica)))

class Heroe:
    ataque = int,

    def atacar(self, Orco):
        pass

class Arquero (Heroe):
    cantFlechas = int,

    def __init__(self, ataque = 1, cantFlechas = 1):
        self.ataque = ataque
        self.cantFlechas = cantFlechas
        print ("{} - Ataque {} - Cant. Flechas {}".format(self.__class__.__name__, str(self.ataque), str(self.cantFlechas)))

    def atacar(self, Orco):
        if self.cantFlechas > 0:
            if self.ataque <= Orco.defensa:
                Orco.vida -= 1
                danio = 1
            else:
                Orco.vida -= (self.ataque - Orco.defensa)
                danio = (self.ataque - Orco.defensa)
        else:
            return ("No hay más flechas!!")

        self.cantFlechas -= 1
        return "{} ha recibido {} de daño".format(Orco.__class__.__name__, danio)


class Mago (Heroe):
    def __init__(self, ataque = 1):
        self.ataque = ataque
        print ("{} - Ataque {}".format(self.__class__.__name__, str(self.ataque)))

    def atacar(self, Orco):
        if self.ataque <= Orco.resitenciaMagica:
            Orco.vida -= 1
            danio = 1
        else:
            Orco.vida -= (self.ataque - Orco.resitenciaMagica)
            danio = (self.ataque - Orco.resitenciaMagica)

        return "{} ha recibido {} de daño".format(Orco.__class__.__name__, danio)

class Paladin (Heroe):
    desgasteEspada = int,

    def __init__(self, ataque = 1):
        self.ataque = ataque
        self.desgaste = 50
        print ("{} - Ataque {} - Desgaste Espada {}".format(self.__class__.__name__, str(self.ataque), str(self.desgaste)))

    def atacar(self, Orco):
        if self.ataque + (0.1 * self.desgaste) <= Orco.defensa:
            Orco.vida -= 1
            danio = 1
        else:
            Orco.vida -= self.ataque + (0.1 * self.desgaste) - Orco.defensa
            danio = self.ataque + (0.1 * self.desgaste) - Orco.defensa
        if self.desgaste > 0:
            self.desgaste -= 1

        return "{} ha recibido {} de daño".format(Orco.__class__.__name__, danio)

