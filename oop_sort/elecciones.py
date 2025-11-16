candidatos = ["Dora", "Bob", "Homero", "Lisa"]

print(candidatos)
# ['Dora', 'Bob', 'Homero', 'Lisa']

# Ordenar alfabeticamente modificando la lista original
candidatos.sort()
print("Orden con sort:", candidatos)
# Orden con sort: ['Bob', 'Dora', 'Homero', 'Lisa']

# Usar sorted para crear una nueva lista
candidatos = ["Dora", "Bob", "Homero", "Lisa"]
ordenados = sorted(candidatos)
print("Original:", candidatos)
# Original: ['Dora', 'Bob', 'Homero', 'Lisa']
print("Con sorted:", ordenados)
# Con sorted: ['Bob', 'Dora', 'Homero', 'Lisa']

resultados = [
    ["Dora", 1200],
    ["Bob", 950],
    ["Homero", 1500],
    ["Lisa", 1500]
] # votos comuna San Joaquin

# Criterio: ordenar por la cantidad de votos (indice 1)

def criterio_votos(item):
    # item es una sublista: [nombre, votos]
    # Devolvemos solo los votos
    return item[1]

resultados_ordenados = sorted(resultados, key=criterio_votos, reverse=True)

for fila in resultados_ordenados:
    print(fila)

# ['Homero', 1500]
# ['Lisa', 1500]
# ['Dora', 1200]
# ['Bob', 950]

# [nombre, votos, edad]
resultados = [
    ["Dora", 1200, 25],
    ["Bob", 950, 30],
    ["Homero", 1500, 45],
    ["Lisa", 1500, 20]
]

def criterio_votos_edad(item):
    return item[1], item[2]

resultados.sort(key=criterio_votos_edad, reverse=True)
print("-"*10)
for candidato in resultados:
    print(candidato)

# ['Homero', 1500, 45]
# ['Lisa', 1500, 20]
# ['Dora', 1200, 25]
# ['Bob', 950, 30]


# [nombre, votos, edad]
resultados = [
    ["Dora", 1200, 25],
    ["Bob", 1500, 30],
    ["Homero", 1500, 45],
    ["Lisa", 1500, 20]
]

def criterio_votos_mayoredad(item):
    return item[1], -item[2]

resultados.sort(key=criterio_votos_mayoredad, reverse=True)
print("-"*10)
for candidato in resultados:
    print(candidato)

# ['Lisa', 1500, 20]
# ['Bob', 1500, 30]
# ['Homero', 1500, 45]
# ['Dora', 1200, 25]