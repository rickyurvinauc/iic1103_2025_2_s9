# python
def esta_patron(circuito, patron):
    # Unimos todos los elementos de 'circuito' en una sola cadena.
    # Esto crea la representacion lineal del circuito.
    circuito_texto = "".join(circuito) * 2  # duplicar para simular circularidad
    # Comprobamos si 'patron' aparece como subcadena en la cadena duplicada.
    # Si aparece, significa que el patron existe.
    if patron in circuito_texto:
        return True
    # Si no aparece, devolvemos False.
    return False
