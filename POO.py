class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola, soy {self.nombre}")

        
persona1 = Persona("Ana", 25)
persona2 = Persona("Carlos", 21)
print(persona1.nombre)
print(persona2.edad)
persona2 = Persona("Carlos",33)
print(persona2.edad)
print(persona1.edad)
persona1.edad = 26

persona1.saludar()



