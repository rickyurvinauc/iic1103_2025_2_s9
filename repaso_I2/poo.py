class Estudiante:
    def __init__(self, nombre, carrera, notas):
        # notas es una lista de numeros
        self.nombre = nombre
        self.carrera = carrera
        self.notas = notas

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        total = 0
        i = 0
        while i < len(self.notas):
            total = total + float(self.notas[i])
            i = i + 1
        return total / float(len(self.notas))

    def estado(self):
        p = self.promedio()
        if p >= 4.0:
            return "aprobado"
        else:
            return "reprobado"

    def __str__(self):
        return self.nombre + " - " + self.carrera + " - prom " + str(round(self.promedio(), 2)) + " - " + self.estado()


e1 = Estudiante("Ana", "Informatica", [5.0, 4.3, 3.9, 6.0])
e2 = Estudiante("Luis", "Industrial", [3.5, 3.8, 3.9])

print("objeto e1:", e1)
print("objeto e2:", e2)
print("e1.promedio():", round(e1.promedio(), 2))
print("e2.estado():", e2.estado())