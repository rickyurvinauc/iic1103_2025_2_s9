class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera
        self.notas = []

    def __str__(self):
        if len(self.notas) == 0:
            return f"{self.nombre} estudia {self.carrera} y no tiene notas"
        prom = sum(self.notas) / len(self.notas)
        if prom >= 4:
            estado = "aprobado"
        else:
            estado = "reprobado"
        return f"{self.nombre} estudia {self.carrera} y está {estado}"

    def notas_igual_mayor_4(self):
        return sum(self.notas) / len(self.notas) >= 4

    def misma_carrera(self, otro):
        return self.carrera == otro.carrera

    def agregar_nota(self, n):
        self.notas.append(n)

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, est):
        self.estudiantes.append(est)

    def carreras_curso(self):
        L = []
        for est in self.estudiantes:
            if est.carrera not in L:
                L.append(est.carrera)
        return L

    def estudiantes_por_carrera(self):
        L = []
        for carrera in self.carreras_curso():
            total = 0
            for est in self.estudiantes:
                if est.carrera == carrera:
                    total += 1
            L.append([carrera, total])
        return L

    def aprobados_y_reprobados(self):
        aprob = 0
        reprob = 0
        for est in self.estudiantes:
            if est.promedio_sobre_4():
                aprob += 1
            else:
                reprob += 1
        print(f"el total de aprobados es {aprob}, el de reprobados es {reprob}")

e1 = Estudiante("Camila", "Psicología")
e2 = Estudiante("Luis", "Ingeniería")
print(e1)
print(e2)


e3 = Estudiante("Roberto", [2.5, 6.0, 3.0])
e3.agregar_nota(4.5)
e3.agregar_nota(5.0)
print(e3.notas)
print(e3.notas_igual_mayor_4())

e4 = Estudiante("Roberto", "Ingeniería")
e5 = Estudiante("María", "Ingeniería")
print(e4.misma_carrera(e5))

e6 = Estudiante("Diego","Sociologia")
e6.notas = [4]
e6.agregar_nota(5)
print(e6.notas)

c = Curso("IIC1103")
c.agregar_estudiante(Estudiante("Roberto", "Psicología"))
c.agregar_estudiante(Estudiante("María", "Biología"))
c.agregar_estudiante(e6)
print(c.carreras_curso())

c = Curso("BBDD")
c.agregar_estudiante(Estudiante("A", "Ing"))
c.agregar_estudiante(Estudiante("B", "Bio"))
c.agregar_estudiante(Estudiante("C", "Ing"))
print(c.estudiantes_por_carrera())
