lista5 = [['Alvarez','Jimena'],['Barrios','Juan'],['Alvarez','Francisco'],['Barrios','Alberto'],['Alvarez','Patricia']]

def criterio3(item):
    return item[1],item[0], item[0]+item[1]

print(lista5)
lista5_ordenada = sorted(lista5,key=criterio3)
for elem in lista5_ordenada:
    print(elem)