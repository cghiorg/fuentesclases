class Animal:
    def hablar(self):
        print("Este animal hace un sonido.")

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")
        
perro = Perro()
gato = Gato()

perro.hablar()
gato.hablar()


class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
    def moverse(self):
        print(f"El vehículo de marca {self.marca} se está moviendo.")
        
class Auto(Vehiculo):
    def moverse(self):
        print(f"El auto {self.marca} está conduciendo por la ruta.")

class Bicicleta(Vehiculo):
    def moverse(self):
        print(f"La bicicleta {self.marca} está pedaleando por la ciclovía.")
        
v = Vehiculo("Genérica")
a = Auto("Toyota")
b = Bicicleta("Oxford")

v.moverse()
a.moverse()
b.moverse()


