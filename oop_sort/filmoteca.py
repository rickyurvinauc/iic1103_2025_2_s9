class Director:

    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad


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
            "La película: "
            + self.nombre
            + " del año: "
            + str(self.anio)
            + " tiene un puntaje promedio de: "
            + str(self.promedio)
        )

    def agregar_puntuacion(self, puntaje):
        self.puntos.append(puntaje)
        self.calcular_promedio()

    def calcular_promedio(self):
        if self.puntos:
            suma = sum(self.puntos)
            self.promedio = round(suma / len(self.puntos), 1)
        else:
            self.promedio = 0

    def es_mejor_que(self, otra_pelicula):
        return self.promedio > otra_pelicula.promedio


class Filmoteca:
    def __init__(self):
        self.peliculas = []

    def __str__(self):
        return "Filmoteca con " + str(len(self.peliculas)) + " películas."

    def agregar_pelicula(
        self, nombre, anio, categoria, descripccion, nombre_director, nacionalidad
    ):

        director = Director(nombre_director, nacionalidad)
        pelicula = Pelicula(nombre, anio, categoria, descripccion, director)
        self.peliculas.append(pelicula)

    def director_mas_frecuente(self):
        directores = []
        for pelicula in self.peliculas:
            directores.append(pelicula.director.nombre)
        directores_unicos = []
        for director in directores:
            if director not in directores_unicos:
                directores_unicos.append(director)
        contador = []
        for director in directores_unicos:
            contador.append(directores.count(director))
        maximo = max(contador)
        indice = contador.index(maximo)
        return [directores_unicos[indice], maximo]


# uso de clase filmoteca

filmoteca = Filmoteca()
filmoteca.agregar_pelicula(
    "Inception",
    2010,
    "Ciencia ficcion",
    "Un ladron roba secretos a traves de los suenos.",
    "Christopher Nolan",
    "Britanico",
)
filmoteca.agregar_pelicula(
    "Interstellar",
    2014,
    "Ciencia ficcion",
    "Viaje a traves de un agujero de gusano.",
    "Christopher Nolan",
    "Britanico",
)
filmoteca.agregar_pelicula(
    "Dunkirk",
    2017,
    "Guerra",
    "Evacuacion durante la Segunda Guerra Mundial.",
    "Christopher Nolan",
    "Britanico",
)
filmoteca.agregar_pelicula(
    "Jurassic Park",
    1993,
    "Aventura",
    "Cientificos recrean dinosaurios en una isla remota.",
    "Steven Spielberg",
    "Estadounidense",
)

# print(filmoteca)
print(filmoteca.director_mas_frecuente())

# uso de clase pelicula
director_1 = Director("Christopher Nolan", "Britanico")
director_2 = Director("Steven Spielberg", "Estadounidense")

pelicula_1 = Pelicula(
    "Inception",
    2010,
    "Ciencia ficcion",
    "Un ladron roba secretos a traves de los suenos.",
    director_1,
)
pelicula_2 = Pelicula(
    "Jurassic Park",
    1993,
    "Aventura",
    "Un parque de diversiones con dinosaurios.",
    director_2,
)
pelicula_3 = Pelicula(
    "The Dark Knight", 2008, "Accion", "Batman lucha contra el Joker.", director_1
)

lista_peliculas = [pelicula_1, pelicula_2, pelicula_3]

for pelicula in lista_peliculas:
    print(pelicula)

pelicula_1.agregar_puntuacion(8)
pelicula_1.agregar_puntuacion(9)
pelicula_1.agregar_puntuacion(10)

pelicula_2.agregar_puntuacion(7)
pelicula_2.agregar_puntuacion(8)
pelicula_2.agregar_puntuacion(9)

pelicula_3.agregar_puntuacion(9)
pelicula_3.agregar_puntuacion(9)
pelicula_3.agregar_puntuacion(10)


# calculamos el promedio de los puntajes de las peliculas
suma = 0
for pelicula in lista_peliculas:
    suma += pelicula.promedio

promedio_total = suma / len(lista_peliculas)
print("El promedio total de las peliculas es: ", round(promedio_total, 0))
