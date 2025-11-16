# Ordenando listas de listas

# Este criterio suma el primer y segundo elemento de cada sublista.
lista3 = [[4,4],[0,1],[1,2],[1,6],[0,3],[9,0],[3,4],[2,5]]

def criterio1(item):
    return item[0]+item[1]

print(lista3)
lista3_ordenada = sorted(lista3,key=criterio1,reverse=True)
print(lista3_ordenada)

# Convierte cada elemento en una cadena antes de ordenarlo.
lista4 = ['arbol',43,39,'casa',34598,'delfin',4,1,'barco',90,'cerca',5]

def criterio2(item):
    return str(item)

print(lista4)
lista4_ordenada = sorted(lista4,key=criterio2)
print(lista4_ordenada)

# Este criterio ordena primero por el segundo elemento de cada sublista, 
# y en caso de empate, por el primer elemento. Varios criterios a la vez
lista5 = [['Alvarez','Jimena'],['Barrios','Juan'],['Alvarez','Francisco'],['Barrios','Alberto'],['Alvarez','Patricia']]

def criterio3(item):
    return item[1],item[0], item[0]+item[1]

print(lista5)
lista5_ordenada = sorted(lista5,key=criterio3)
for elem in lista5_ordenada:
    print(elem)
    

# mas ejemplos de ordenamiento de listas de listas
numeros = [[3, 5, 1], [10, 2], [4, 4, 4], [7]]
numeros.sort(key=sum)
print(numeros)  # [[7], [3, 5, 1], [10, 2], [4, 4, 4]]

frases = [["Hola"], ["Hola", "mundo"], ["Python", "es", "genial"]]
frases.sort(key=len)
print(frases)  # [['Hola'], ['Hola', 'mundo'], ['Python', 'es', 'genial']]

numeros = [[3, 5, 1], [10, 2], [4, 4, 4], [7]]
numeros.sort(key=max)
print(numeros)  # [[7], [3, 5, 1], [4, 4, 4], [10, 2]]
