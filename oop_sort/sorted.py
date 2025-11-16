numeros = [5, 2, 9, 1, 7]
ordenados = sorted(numeros)
print(ordenados)  # [1, 2, 5, 7, 9]

palabras = ["manzana", "kiwi", "banana", "cereza"]
ordenadas = sorted(palabras)
print(ordenadas)  # ['banana', 'cereza', 'kiwi', 'manzana']

numeros = [5, 2, 9, 1, 7]
ordenados = sorted(numeros, reverse=True)
print(ordenados)  # [9, 7, 5, 2, 1]


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
    Pelicula("El Padrino", 1972, "Drama", "Historia de la mafia", "Francis Ford Coppola"),
    Pelicula("Inception", 2010, "Ciencia ficción", "Sueños compartidos", "Christopher Nolan"),
    Pelicula("Parasite", 2019, "Thriller", "Clases sociales", "Bong Joon-ho"),
    Pelicula("Titanic", 1997, "Romance", "Historia trágica", "James Cameron")
]

def criterio_por_anio(pelicula):
    return pelicula.anio

ordenadas_por_anio = sorted(peliculas, key=criterio_por_anio)
for pelicula in ordenadas_por_anio:
    print(pelicula)


def criterio_por_nombre(pelicula):
    return pelicula.nombre

ordenadas_por_nombre = sorted(peliculas, key=criterio_por_nombre)
for pelicula in ordenadas_por_nombre:
    print(pelicula)
