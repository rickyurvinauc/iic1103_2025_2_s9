##AQUI PUEDES ESCRIBIR TU CODIGO
def criterio(item):
    return (-item[1], item[0])

def ordenar_ocupacion(aud):
    lista = []
    indice = 0
    for indice_c in range(len(aud[0])):
        contador_x = 0
        for indice_f in range(len(aud)):
            if aud[indice_f][indice_c] == "X":
                contador_x += 1
        lista.append([indice, contador_x])
        indice+=1
    lista.sort(key=criterio)
    return lista       