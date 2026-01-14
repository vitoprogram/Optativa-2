class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []

    def añadir_jugador(self, jugador):
        self.jugadores.append(jugador)


class Jugador:
    def __init__(self, dorsal, nombre):
        self.dorsal = dorsal
        self.nombre = nombre
        self.equipo = None

    def asignar_equipo(self, equipo):
        self.equipo = equipo
        equipo.añadir_jugador(self)


# Programa principal
equipo1 = Equipo("Barcelona")

jugador1 = Jugador(10, "Messi")
jugador2 = Jugador(8, "Iniesta")

jugador1.asignar_equipo(equipo1)
jugador2.asignar_equipo(equipo1)

print(equipo1.nombre)
for jugador in equipo1.jugadores:
    print(f"{jugador.dorsal}. {jugador.nombre}")
