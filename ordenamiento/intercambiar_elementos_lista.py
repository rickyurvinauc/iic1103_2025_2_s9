# # Intercambiar el primer elemento con el segundo

# lista = [1, 2, 3, 4, 5]
# lista[0], lista[1] = lista[1], lista[0]
# print(lista)  # [2, 1, 3, 4, 5]

# # Intercambiar el primer y el ultimo elemento
# lista[0], lista[-1] = lista[-1], lista[0]

# # Intercambiar el segundo y el penultimo elemento
# lista[1], lista[-2] = lista[-2], lista[1]

# print(lista)  # [5, 4, 3, 2, 1]

# lista_de_listas = [[1, 2], [3, 4], [5, 6], [7, 8]]
# # Intercambiar el primer elemento con el segundo
# lista_de_listas[0], lista_de_listas[1] = lista_de_listas[1], lista_de_listas[0]
# print(lista_de_listas)
# # [[3, 4], [1, 2], [5, 6], [7, 8]]

def swap(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

# Intercambiar el primer y el ultimo elemento
lista_de_listas = [[1, 2], [3, 4], [5, 6], [7, 8]]
swap(lista_de_listas, 0, -1)
print(lista_de_listas)
# [[7, 8], [3, 4], [5, 6], [1, 2]]
# [[7, 8], [1, 2], [5, 6], [3, 4]]