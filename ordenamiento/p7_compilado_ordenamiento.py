def criterio(item):
    return item[1]
archivo = open('catalan.txt','r')
contenido = archivo.readlines()
lista = []
lista_palabras = []
for linea in contenido:
    linea = linea.strip()
    if linea not in lista:
        lista.append(linea)
    lista_palabras.append(linea)

inidce_l = 0
for palabra in lista:
    contador = 0
    for pal in lista_palabras:
        if pal == palabra:
            contador += 1
    lista[inidce_l] = [palabra, contador]
    inidce_l += 1

lista.sort(key=criterio, reverse = True)

for item in lista:
    if item[1]>1:
        print(item[0]+" "+str(item[1]))

archivo.close()