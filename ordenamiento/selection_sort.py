# Explicacion paso a paso del selection sort
lista_desordenada = [7, 12, 9, 11, 3]

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            numero_seleccionado = lista[min_index]
            numero_comparar = lista[j]
            if numero_comparar < numero_seleccionado:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    
    return lista

lista_ordenada = selection_sort(lista_desordenada)
print(lista_ordenada)