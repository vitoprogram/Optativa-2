

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}")


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_usuario(self):
        print(f"Usuario: {self.nombre}")


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            libro.mostrar_info()


# Programa principal
biblioteca = Biblioteca()

libro1 = Libro("1984", "George Orwell")
libro2 = Libro("Don Quijote", "Miguel de Cervantes")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.mostrar_libros()
