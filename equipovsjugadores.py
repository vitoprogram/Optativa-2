
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
equipo = Equipo("Lakers")

jugador1 = Jugador(16, "Pau Gasol")
jugador2 = Jugador(24, "Kobe Bryant")

jugador1.asignar_equipo(equipo)
jugador2.asignar_equipo(equipo)

print(f"Equipo: {equipo.nombre}")
for j in equipo.jugadores:
    print(f"{j.dorsal}. {j.nombre}")
