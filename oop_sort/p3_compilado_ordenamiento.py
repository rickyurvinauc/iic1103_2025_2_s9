
# Escribe tu código aquí
# ['14/02', '19:30', 120, 'Cena romantica', 2, 14, 1930]
def criterio(item):
    return item[4], item[5], item[6]


def ordenar_cronologicamente(actividades):
    for actividad in actividades:
        mes = int(actividad[0][len(actividad[0]) - 2:])
        dia = int(actividad[0][0:2])
        hora = int(actividad[1][:2] + actividad[1][len(actividad[1]) - 2:])
        actividad.append(mes)
        actividad.append(dia)
        actividad.append(hora)

    actividades.sort(key=criterio)
    lista = []
    for act in actividades:
        lista.append(act[:len(act) - 3])

    return lista


