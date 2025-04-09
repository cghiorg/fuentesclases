numeros = [5, 2, 9, 1]
ordenada = sorted(numeros, reverse=True)
print(ordenada)  # [9, 5, 2, 1]

palabras = ["banana", "manzana", "kiwi"]
palabras.sort(key=str.lower, reverse=True)
print(palabras)

numeros = [1, 2, 3, 2, 2, 4, 5]
print(numeros.count(2))

frutas = ["manzana", "banana", "naranja", "peras"]
print(len(frutas))  # 3 (porque hay 3 elementos)

notas = [7, 8, 9, 7, 10, 7, 6, 7]
frecuencia = notas.count(7)
total = len(notas)
porcentaje = (frecuencia / total) * 100

print(f"El 7 aparece {frecuencia} veces, es el {porcentaje:.2f}% de la lista.")
