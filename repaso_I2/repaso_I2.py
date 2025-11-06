#strings

texto = "Programar"
print(texto[0])      # P
print(texto[-1])     # r
print(texto[2:5])    # ogr

#listas

numeros = [10, 20, 30]
numeros.append(40)
print(numeros[1])  # 20


#listas de listas
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(matriz[0][1])  # 2

for fila in matriz:
    for valor in fila:
        print(valor)

notas = [
     [600, 600, 600], # Estudiante 1
     [600, 500, 600], # Estudiante 2
     [600, 600, 350], # Estudiante 3
     [600, 200, 450] # Estudiante 4
]

print(len(notas)) # cantidad de filas
print(len(notas[0])) # cantidad de columnas
# archivos

archivo = open("datos.txt", "w")
archivo.write("Hola mundo\n")
archivo.close()