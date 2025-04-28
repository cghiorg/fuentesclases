class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_info(self):
        print(f"'{self.titulo}' de {self.autor} ({self.anio})")

class LibroFisico(Libro):
    def __init__(self, titulo, autor, anio, ubicacion):
        super().__init__(titulo, autor, anio)
        self.ubicacion = ubicacion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Ubicación en estantería: {self.ubicacion}")

class Ebook(Libro):
    def __init__(self, titulo, autor, anio, formato):
        super().__init__(titulo, autor, anio)
        self.formato = formato

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Formato digital: {self.formato}")

fisico = LibroFisico("Cien años de soledad", "Gabriel García Márquez", 1967, "Estante 4B")
digital = Ebook("Rebelión en la granja", "George Orwell", 1945, "EPUB")

def mostrar_libro(libro):
    libro.mostrar_info()
    print("----------")
    
mostrar_libro(fisico)
mostrar_libro(digital)