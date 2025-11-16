# Ejemplo 1: lista simple
lista = [1, 2, 3, 4, 5]
lista_ordenada = sorted(lista, reverse=True)
print(lista_ordenada)


# Ejemplo 2: lista simple con palabras
palabras = ["hola", "como", "estas", "bien"]
palabras_ordenadas = sorted(palabras, reverse=True)
print(palabras_ordenadas)

# Ejemplo 3: lista de listas
lista_de_listas = [[1, 2], [3, 4], [5, 6], [7, 8]]
lista_de_listas_ordenada = sorted(lista_de_listas, reverse=True)
print(lista_de_listas_ordenada)
# [[7, 8], [5, 6], [3, 4], [1, 2]]

# Ejemplo 4: lista de objetos de la clase Pelicula
class Pelicula:
    def __init__(self, nombre, anio, categoria, descripcion, director):
        self.nombre = nombre
        self.anio = anio
        self.categoria = categoria
        self.descripcion = descripcion
        self.director = director
        self.puntos = []
        self.promedio = 0

    def __str__(self):
        return f"Pelicula({self.nombre}, {self.anio}, {self.categoria}, {self.promedio})"
    
    def calcular_promedio(self):
        if self.puntos:
            suma = sum(self.puntos)
            self.promedio = round(suma / len(self.puntos), 1)
        else:
            self.promedio = 0

peliculas = [
    Pelicula("El Padrino", 1972, "Drama", "Mafia", "Francis Ford Coppola"),
    Pelicula("Inception", 2010, "Ciencia ficción", "Sueños", "Christopher Nolan"),
    Pelicula("Parasite", 2019, "Thriller", "Sociedad", "Bong Joon-ho"),
    Pelicula("Titanic", 1997, "Romance", "Tragedia", "James Cameron")
]

def criterio_por_anio(pelicula):
    return pelicula.anio

peliculas.sort(key=criterio_por_anio, reverse=True)

for pelicula in peliculas:
    print(pelicula)

# Pelicula(Parasite, 2019, Thriller, 0)
# Pelicula(Inception, 2010, Ciencia ficción, 0)
# Pelicula(Titanic, 1997, Romance, 0)
# Pelicula(El Padrino, 1972, Drama, 0)