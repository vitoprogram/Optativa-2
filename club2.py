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
nombre_equipo = input("Nombre del equipo: ")
equipo = Equipo(nombre_equipo)

cantidad = int(input("¿Cuántos jugadores quieres añadir? "))

for i in range(cantidad):
    print(f"\nJugador {i + 1}")
    dorsal = int(input("Dorsal: "))
    nombre = input("Nombre: ")

    jugador = Jugador(dorsal, nombre)
    jugador.asignar_equipo(equipo)

print("\nEquipo:", equipo.nombre)
for jugador in equipo.jugadores:
    print(f"{jugador.dorsal}. {jugador.nombre}")
