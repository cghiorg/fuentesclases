class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre      # Atributo: nombre de la persona
        self.edad = edad          # Atributo: edad de la persona

    def saludar(self):            # Método: una acción que la persona puede hacer
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
        
p1 = Persona("Carlos", 40)
p1.saludar()

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def mostrar_saldo(self):
        print(f"Saldo actual: ${self.__saldo}")

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            
# Creamos una cuenta con $1000 de saldo inicial
mi_cuenta = CuentaBancaria(1000)

# Mostramos el saldo actual
mi_cuenta.mostrar_saldo()  # Salida: Saldo actual: $1000

# Depositamos $500
mi_cuenta.depositar(500)

# Mostramos el saldo actualizado
mi_cuenta.mostrar_saldo()  # Salida: Saldo actual: $1500