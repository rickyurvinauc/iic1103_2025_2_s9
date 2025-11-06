def contar_valeotro(chocolates):
    # Caso base: si hay 2 o menos envoltorios no se puede canjear ninguno.
    if chocolates <=2:
        return 0

    # Calculamos cuantos sobrantes quedan despues de canjear por grupos de 3:
    # chocolates//3*3 es la mayor multiplicacion de 3 <= chocolates.
    # chocolates - (chocolates//3*3) son los envoltorios que no se usan en este paso.
    sobrantes = chocolates - (chocolates//3*3)

    # chocolates//3 son los chocolates nuevos obtenidos en este paso.
    # Para los siguientes pasos, los envoltorios disponibles seran:
    #   - los nuevos chocolates (cada uno deja un envoltorio)
    #   - mas los sobrantes que no se usaron ahora.
    # Llamamos recursivamente con esa suma y añadimos los obtenidos en este paso.
    return chocolates//3 + contar_valeotro(chocolates//3 + sobrantes)
