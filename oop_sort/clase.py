resultados = [
    ["Dora", 1200, 35],
    ["Bob", 950, 24],
    ["Homero", 1500, 60],
    ["Lisa", 1500, 60]
] # votos comuna San Joaquin

def criterio(item):
    # item ->  ["Dora", 1200, 35]
    return -item[1], item[2], item[0]

lista_resp = sorted(resultados, key=criterio, reverse=False)
print(lista_resp)

resultados.sort(key=criterio, reverse=False)
for cand in resultados:
    print(cand)