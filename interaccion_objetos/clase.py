class Estudiante:

    def __init__(self, identificador ,nombre, carrera):
        self.identificador = nombre
        self.nombre = nombre
        self.carrera = carrera
        self.notas = [] # [5,4,6]

    def __str__(self):
        promedio = 0
        if len(self.notas) > 0:
            promedio = sum(self.notas) /len(self.notas)
        texto = "Hola soy: "+self.nombre+ " y mi promedio de notas es: "+ str(promedio)
        return texto

    def agregar_nota(self,nota):
        self.notas.append(nota) # modificado un atributo del objeto

    def notas_mayor_que_4(self):
        if sum(self.notas) / len(self.notas) >= 4:
            return True
        return False
    

class Curso:

    def __init__(self, nombre, semestre, profesor):
        self.nombre = nombre
        self.semestre = semestre
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def imprimi_aprobados_reprobados(self):
        aprobados = 0
        reprobados = 0
        for est in self.estudiantes:
            if est.notas_mayor_que_4():
                aprobados += 1
            else:
                reprobados += 1
        print(f"La cantidad de aprobados son: {aprobados} y reprobado son: {reprobados}")

    def carreras_curso(self): # una lista con las carreras
        lista_respuesta = []

        for est in self.estudiantes:
            if est.carrera not in lista_respuesta:
                lista_respuesta.append(est.carrera)
        
        return lista_respuesta

e1 = Estudiante(1, "Ricardo Urvina","Ing. Civil")
e2 = Estudiante(2, "Ingrid Medina","Ing. Construccion")
e3 = Estudiante(2, "Liliana Cordova","Ing. Civil")
e1.agregar_nota(7)
e1.agregar_nota(2)
e1.agregar_nota(4)

e2.agregar_nota(3)
e2.agregar_nota(2)
e2.agregar_nota(4)

e3.agregar_nota(5)
e3.agregar_nota(4)
e3.agregar_nota(3)

curso = Curso("IIC1103","2025-2","Tamara")

curso.agregar_estudiante(e1)
curso.agregar_estudiante(e2)
curso.agregar_estudiante(e3)

curso.imprimi_aprobados_reprobados()
print(curso.carreras_curso())