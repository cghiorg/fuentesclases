numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numeros[2:6])
print(numeros[:4])
print(numeros[5:])
print(numeros[::2])
print(numeros[::-1])


letras = ["a", "b", "c", "a", "d", "a", "e"]

# Contar cuántas "a" hay en los primeros 5 elementos
primeros_5 = letras[:5]
cantidad_a = primeros_5.count("a")

print(f"En los primeros 5 elementos hay {cantidad_a} 'a'.")  

# Tupla vacía
tupla_vacia = ()

# Tupla con elementos
coordenadas = (10, 20)
mixta = (1, "a", [3, 4])

correcto = (5,)  # Es una tupla
incorrecto = (5)  # Es un entero, NO una tupla

