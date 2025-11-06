def primera_cancion(lista):
    # Construimos el rango de indices validos segun el tamano de la lista.
    indices = range(len(lista))
    # Creamos una lista vacia para almacenar los indices que ya aparecen
    # en las canciones (indices reproducidos).
    indices_reproduccion = []

    # Recorremos cada cancion en 'lista' y recogemos su indice de reproduccion.
    # Asi obtenemos un registro de todos los indices que ya estan presentes.
    for cancion in lista:
        indices_reproduccion.append(cancion[2])

    # Ahora comprobamos, en orden, cual es el primer indice esperado
    # que NO esta en 'indices_reproduccion'. Cuando lo encontremos,
    # devolvemos el titulo de la cancion en esa posicion.
    for i in indices:
        if i not in indices_reproduccion:
            return lista[i][0]