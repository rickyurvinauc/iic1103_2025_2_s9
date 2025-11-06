# Abrimos el archivo que contiene las parejas catalan-castellano en modo lectura
diccionario = open(`diccionario.txt`,"r")
# Leemos todas las lineas del archivo en una lista (cada linea incluye el salto de linea)
contenido_diccionario = diccionario.readlines()
# Cerramos el archivo para liberar recursos
diccionario.close()

# Preparamos la lista que contendra las parejas [catalan, castellano]
lista_diccionario = []

# Recorremos cada linea leida del archivo de diccionario
for item in contenido_diccionario:
    # Eliminamos espacios y saltos de linea alrededor y separamos por '-' en dos partes
    datos = item.strip().split("-")
    # Añadimos la pareja como una lista de dos elementos: [palabra_catalan, traduccion_castellano]
    lista_diccionario.append([datos[0],datos[1]])

# Abrimos el archivo con palabras en catalan en modo lectura
catalan = open(`catalan.txt`,"r")
# Creamos el archivo de salida en modo append para añadir traducciones
castellano = open(`castellano.txt`,"a")
# Leemos todas las lineas del archivo de palabras catalanas
contenido_catalan = catalan.readlines()
# Cerramos el archivo de entrada
catalan.close()

# Recorremos cada linea del archivo de catalan (cada posible palabra)
for item in contenido_catalan:
    # Normalizamos la palabra eliminando salto de linea
    palabra_catalan = item.strip()

    # Buscamos la traduccion comparando con cada entrada del diccionario en memoria
    for palabra_castellano in lista_diccionario:
        # Extraemos la forma en catalan de la entrada del diccionario
        palabra_catalan2 = palabra_castellano[0]
        # Extraemos la traduccion al castellano correspondiente
        traduccion = palabra_castellano[1]
        # Si encontramos coincidencia exacta escribimos la traduccion en el archivo de salida
        if palabra_catalan == palabra_catalan2:
            castellano.write(traduccion+"\n")
            # Una vez encontrada la traduccion, salimos del bucle interior para pasar a la siguiente palabra
            break

castellano.close()
