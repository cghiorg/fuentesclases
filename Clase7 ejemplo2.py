# Clase base Vehículo
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrar_info(self):
        print(f"🚗 Vehículo:")
        print(f"  Marca: {self.marca}")
        print(f"  Modelo: {self.modelo}")
        print(f"  Año: {self.anio}")

# Subclase Auto que hereda de Vehículo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)  # Llama al constructor de la clase padre
        self.puertas = puertas  # Nuevo atributo exclusivo de Auto

    # Sobrescribimos el método para incluir la cantidad de puertas
    def mostrar_info(self):
        super().mostrar_info()  # Muestra la info básica
        print(f"  Puertas: {self.puertas}")

# Crear instancia de Vehículo
vehiculo_generico = Vehiculo("Toyota", "Corolla", 2015)
vehiculo_generico.mostrar_info()

print("\n====================\n")

# Crear instancia de Auto
auto_deportivo = Auto("Ford", "Mustang", 2022, 2)
auto_deportivo.mostrar_info()
