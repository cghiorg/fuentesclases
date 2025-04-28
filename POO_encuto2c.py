class Loro:
    def hablar(self):
        print("Soy un loro y digo: ¡Hola!")
class Robot:
    def hablar(self):
        print("Soy un robot y digo: Sistema activado.")
        
def hacer_hablar(entidad):
    entidad.hablar()
    
loro = Loro()       # Creamos un loro
robot = Robot()     # Creamos un robot

hacer_hablar(loro)
hacer_hablar(robot)

