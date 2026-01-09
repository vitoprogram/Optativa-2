class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre


class Jugador:
    def __init__(self, dorsal, nombre, equipo):
        self.dorsal = dorsal
        self.nombre = nombre
        self.equipo = equipo

    def mostrar(self):
        print(f"{self.dorsal}.{self.nombre} - {self.equipo.nombre}")


# Programa principal
equipo1 = Equipo("Lakers")
jugador1 = Jugador(16, "PauGasol", equipo1)
equipo2 = Equipo("FC Barcelona")
jugador2 = Jugador(10,"Messi", equipo2)

jugador1.mostrar()
jugador2.mostrar()