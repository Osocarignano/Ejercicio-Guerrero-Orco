class Orco:
    vida = 0
    defensa = 0
    ataque = 0

    def atacar(self, enemy_obj):
        if (self.ataque - enemy_obj.defensa) <= 0:
            enemy_obj.vida -= 1
        else:
            enemy_obj.vida -= self.ataque - enemy_obj.defensa

        if enemy_obj.vida <= 0:
            return print("El Guerrero esta mueeeerto muerto muerto")
        else:
            return print("Vida del guerrero: {}".format(enemy_obj.vida))


class Guerrero:
    vida = 0
    vidaInicial = 0
    defensa = 0
    ataque = 0
    curacion = 0
    aux = 0

    def atacar(self, enemy_obj):
        if (self.ataque - enemy_obj.defensa) <= 0:
            enemy_obj.vida -= 1
        else:
            enemy_obj.vida -= self.ataque - enemy_obj.defensa

        if enemy_obj.vida <= 0:
            return print("El orco esta mueeeerto muerto muerto")
        else:
            return print("Vida del Orco: {}".format(enemy_obj.vida))

    def curar(self):
        if self.vida <= 0:
            return print("El Guerrero esta muerto te dije, no se cura nada, NADA")
        else:
            if self.vidaInicial == self.vida:
                return print("Curados 0 puntos de vida al Guerrero, esta a full")

            self.vida += self.curacion

            if self.vida > self.vidaInicial:
                self.aux = self.curacion - (self.vida - self.vidaInicial)
                self.vida = self.vidaInicial
                return print("Curados {} puntos de vida al Guerrero, vida al maximo".format(self.aux))
            else:
                return print("Curados {} puntos de vida al Guerrero y su vida es ahora {}".format(self.curacion, self.vida))


print("Ingrese valores del guerrero")
Guerrero001 = Guerrero()

Guerrero001.vida = int(input("Vida Gurrero: "))
Guerrero001.vidaInicial = int(input("Vida Maxima Gurrero: "))
Guerrero001.ataque = int(input("Ataque Gurrero: "))
Guerrero001.defensa = int(input("Defensa Gurrero: "))
Guerrero001.curacion = int(input("Curacion Gurrero: "))

print("\n")

print("Ingrese valores del Orco")
Orco001 = Orco()

Orco001.vida = int(input("Vida Orco: "))
Orco001.ataque = int(input("Ataque Orco: "))
Orco001.defensa = int(input("Defensa Orco: "))


print("\n")
Guerrero001.atacar(Orco001)
print("\n")
Orco001.atacar(Guerrero001)
print("\n")
Guerrero001.curar()
