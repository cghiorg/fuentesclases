# Lista vacía
lista_vacia = []

# Lista con elementos
numeros = [1, 2, 3, 4, 5]
mixta = [10, "Hola", True, [1, 2]]  # Lista con diferentes tipos
print(mixta[1])
print(numeros[-1])

print(dir(numeros))

numeros.append(6)
print(numeros)
numeros.append(20)
print(numeros)
numeros.append(8)
print(numeros)
numeros.insert(2, 99)
print(numeros)
numeros.extend([7, 11])
numeros.remove(99)
ultimo = numeros.pop([7])
print(numeros)