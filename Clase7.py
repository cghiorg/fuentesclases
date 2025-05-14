# Paso 1: Crear una tupla con 3 estudiantes. Cada uno tiene nombre, edad y lista de materias.
estudiantes_tupla = (
    ("Ana", 20, ["Matemáticas", "Física"]),
    ("Luis", 22, ["Historia", "Literatura"]),
    ("Sofía", 19, ["Biología", "Química"])
)

# Paso 2: Convertimos la tupla a una lista para poder modificarla (agregar un nuevo estudiante).
estudiantes_lista = list(estudiantes_tupla)

# Agregamos un nuevo estudiante
nuevo_estudiante = ("Marcos", 21, ["Geografía", "Filosofía"])
estudiantes_lista.append(nuevo_estudiante)

# Paso 3: Transformamos la lista en un diccionario.
# Clave: nombre del estudiante, Valor: (edad, lista de materias)
estudiantes_dict = {}
for estudiante in estudiantes_lista:
    nombre, edad, materias = estudiante
    estudiantes_dict[nombre] = {
        "edad": edad,
        "materias": materias
    }

# Paso 4: Imprimir los datos de cada estudiante de forma legible.
print("📚 Lista de estudiantes:")
for nombre, datos in estudiantes_dict.items():
    print(f"\n👤 Nombre: {nombre}")
    print(f"🎂 Edad: {datos['edad']}")
    print("📘 Materias:")
    for materia in datos['materias']:
        print(f" - {materia}")
