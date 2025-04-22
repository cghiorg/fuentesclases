class Animal:
    def hablar(self):
        return "Algún sonido"

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"

# Crear objetos
mi_perro = Perro()
mi_gato = Gato()

# Polimorfismo en acción con una lista de animales
animales = [Perro(), Gato(), Gato(), Perro()]

for animal in animales:
    print(animal.hablar())  # ➜ Guau, Miau, Miau, Guau (según el orden)
