class Figura:
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado * self.lado

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.14 * self.radio * self.radio

def mostrar_area(figura):
    print(f"Área: {figura.area()}")

f1 = Cuadrado(4)
f2 = Circulo(3)

mostrar_area(f1)   # Área: 16
mostrar_area(f2)   # Área: 28.26
    
    