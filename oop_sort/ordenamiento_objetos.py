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
        return (
            f"Pelicula({self.nombre}, {self.anio}, {self.categoria}, {self.promedio})"
        )

    def calcular_promedio(self):
        if self.puntos:
            suma = sum(self.puntos)
            self.promedio = round(suma / len(self.puntos), 1)
        else:
            self.promedio = 0


peliculas = [
    Pelicula("El Padrino", 1972, "Drama", "Mafia", "Francis Ford Coppola"),
    Pelicula("Inception", 2010, "Ciencia ficción", "Sueños", "Christopher Nolan"),
    Pelicula("Parasite", 1972, "Thriller", "Sociedad", "Bong Joon-ho"),
    Pelicula("Titanic", 1997, "Romance", "Tragedia", "James Cameron"),
]


# def criterio_por_anio(pelicula):
#     return pelicula.anio, pelicula.nombre


# peliculas.sort(key=criterio_por_anio)
# print("Ordenadas por año:")
# for pelicula in peliculas:
#     print(pelicula)


# def criterio_por_nombre(pelicula):
#     return pelicula.nombre


# peliculas.sort(key=criterio_por_nombre)
# print("Ordenadas por nombre:")
# for pelicula in peliculas:
#     print(pelicula)


def criterio_por_director(pelicula):
    return pelicula.director


peliculas.sort(key=criterio_por_director)
print("Ordenadas por director:")
for pelicula in peliculas:
    print(pelicula)


# def criterio_por_categoria(pelicula):
#     return pelicula.categoria


# peliculas.sort(key=criterio_por_categoria)
# print("Ordenadas por categoria:")
# for pelicula in peliculas:
#     print(pelicula)


# def criterio_por_longitud_descripcion(pelicula):
#     return len(pelicula.descripcion)


# peliculas.sort(key=criterio_por_longitud_descripcion)
# print("Ordenadas por longitud de descripcion:")
# for pelicula in peliculas:
#     print(pelicula)


# def criterio_por_promedio(pelicula):
#     return pelicula.promedio


# peliculas[0].puntos = [10, 9, 9]
# peliculas[1].puntos = [8, 8, 9]
# peliculas[2].puntos = [9, 10, 10]
# peliculas[3].puntos = [7, 8, 8]

# peliculas[0].calcular_promedio()
# peliculas[1].calcular_promedio()
# peliculas[2].calcular_promedio()
# peliculas[3].calcular_promedio()

# peliculas.sort(key=criterio_por_promedio, reverse=True)
# print("Ordenadas por promedio:")

# for pelicula in peliculas:
#     print(pelicula)
