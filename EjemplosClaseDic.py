# Diccionario vacío
dic_vacio = {}

# Diccionario con elementos
alumno = {
    "nombre": "Ana",
    "edad": 25,
    "carrera": "Ingeniería"
}

# Diccionario anidado
frutas = {
    "manzana": {"peso": 150, "color": "rojo"},
    "plátano": {"peso": 120, "color": "amarillo"}
}

print(alumno["nombre"])

print(alumno.get("edad"))

alumno["edad"] = 26

print(alumno.get("edad"))

alumno["sexo"] = "Femenino"

print(alumno.get("sexo"))

print (alumno.keys())

print (alumno.values())

print (alumno.items())

print(alumno.pop("edad"))

print (alumno.items())

if "nombre" in alumno:
    print("La clave 'nombre' existe")
    
    
