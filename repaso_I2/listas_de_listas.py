def suma_col(tabla, j):
    total = 0
    i = 0
    while i < len(tabla):
        total = total + tabla[i][j]
        i = i + 1
    return total


mat = [
    ["ana", 3, 80],
    ["carlos", 1, 95],
    ["beatriz", 2, 88]
]
print("matriz inicial:", mat)
print("acceso mat[0][0]:", mat[0][0])   # "ana"
print("acceso mat[2][2]:", mat[2][2])   # 88

# recorrer
print("recorrer por filas y columnas:")
i = 0
while i < len(mat):
    j = 0
    fila_texto = ""
    while j < len(mat[i]):
        if j == 0:
            fila_texto = str(mat[i][j])
        else:
            fila_texto = fila_texto + " | " + str(mat[i][j])
        j = j + 1
    print("  ", fila_texto)
    i = i + 1


# agregacion por columna numerica (col 2 = puntaje)
total_puntaje = suma_col(mat, 2)
print("suma de col 2:", total_puntaje)