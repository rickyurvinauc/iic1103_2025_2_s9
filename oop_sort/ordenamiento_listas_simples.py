numeros = [5, 2, 9, 1, 7]
numeros.sort()
print(numeros)
# [1, 2, 5, 7, 9]

palabras = ["manzana", "kiwi", "banana", "cereza"]
palabras.sort()
print(palabras)
# ['banana', 'cereza', 'kiwi', 'manzana']

# Ejemplo 3: Ordenar en orden descendente
numeros = [5, 2, 9, 1, 7]
numeros.sort(reverse=True)
print(numeros)  # [9, 7, 5, 2, 1]

# Ordenamiento personalizado con key sin  uso de funciones lamba
# Ejejmplo 4: Ordenar palabras por longitud
palabras = ["manzana", "kiwi", "banana", "cereza"]
palabras.sort(key=len, reverse=True)
print(palabras)  # ['kiwi', 'banana', 'cereza', 'manzana']

# Ejemplo 5: Ordenar numeros por su valor absoluto
numeros = [5, -2, 9, -1, 7]
numeros.sort(key=abs)
print(numeros)  # [-1, -2, 5, 7, 9]

# Ejemplo 6 Ordenar palabras ignorando mayusculas y minusculas
palabras = ["manzana", "Kiwi", "banana", "Cereza"]
palabras.sort(key=str.lower)
print(palabras)  # ['banana', 'Cereza', 'Kiwi', 'manzana']

# Ordenamiento personalizado con key usando funciones propias def criterio(item)

lista1 = [
    "arbol",
    "de",
    "delfin",
    "años",
    "ñandu",
    "ñuñoa",
    "mañana",
    "casa",
    "barco",
    "zapato",
    "televisor",
    "paraguas",
    "lluvia",
    "ardilla",
    "elefante",
    "caracol",
    "ave",
    "gato",
    "foca",
]
lista2 = [
    "casa",
    "arbol",
    "ELEFANTE",
    "feria",
    "automovil",
    "libro",
    "DelFiN",
    "dinoSAURIO",
]


# criterio de invierte el orden de las palabras
lista1 = [
    "arbol", #0
    "de", #3
    "delfin",
    "años",
    "ñandu",
    "ñuñoa",
    "mañana",
    "casa",
    "barco",
    "zapato",
    "televisor",
    "paraguas",
    "lluvia",
    "ardilla",
    "elefante",
    "caracol",
    "ave",
    "gato",
    "foca",
]
def criterio1(item):
    return item[::-1]

print(lista1)
lista1_ordenada = sorted(lista1, key=criterio1)
print(lista1_ordenada)

# El criterio devuelve la posicion de la primera letra de cada palabra en el alfabeto personalizado abc
def criterio1b(item):
    abc = "abcdefghijklmnñopqrstuvwxyz"
    return abc.index(item[0])


#  La lista se ordenará alfabéticamente ignorando mayúsculas y minúsculas
def criterio2(item):
    return item.lower()


print(lista1)
lista1_ordenada = sorted(lista1, key=criterio1)
print(lista1_ordenada)

print(lista1)
lista1_ordenada = sorted(lista1, key=criterio1b)
print(lista1_ordenada)

print(lista2)
lista2_ordenada = sorted(lista2, key=criterio2)
print(lista2_ordenada)
