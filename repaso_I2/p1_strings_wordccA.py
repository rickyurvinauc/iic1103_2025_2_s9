def parentesis(texto, indice):
    texto_cortado = texto[:indice]  # cortamos el texto hasta la posicion indicada (no incluido)
    indice_p = 0  # variable que guardara la posicion encontrada; inicia en 0 por defecto
    # Recorremos cada indice del texto_cortado para poder obtener la posicion numerica
    for indice_t in range(len(texto_cortado)):
        letra = texto_cortado[indice_t]  # obtenemos el caracter en la posicion actual
        # Si el caracter es un parentesis abierto, actualizamos indice_p
        # De esta forma vamos registrando la ultima posicion donde aparece '('
        if letra == "(":
            indice_p = indice_t
    # Al salir del bucle, indice_p contiene la ultima posicion de '(' ,
    # o 0 si no se encontro ninguno.
    return indice_p
