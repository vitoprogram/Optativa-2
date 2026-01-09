class Jugador:
    def __init__(self, dorsal, nombre):
        self.dorsal = dorsal
        self.nombre = nombre

    def mostrar(self):
        print(f"{self.dorsal}.{self.nombre}")


# Programa principal
jugador1 = Jugador(16, "PauGasol")
jugador2 = Jugador(10, "Messi")

jugador1.mostrar()
jugador2.mostrar()
