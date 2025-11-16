def obtener_promedios(curso):
    # resultado = [["Ricardo",3],["Ingrid", 6.5]]
    resultado = []

    for estudiante in curso.estudiantes:
        promedio = sum(estudiante.notas)/len(estudiante.notas)
        resultado.append([estudiante.nombre, round(promedio,1)])
    
    return resultado


class Estudiante:

    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut
        self.notas = []
    
    def agregar_nota(self, nota):
        self.notas.append(nota)
    
    def promedio_mas_de_4(self):
        promedio = sum(self.notas) / len(self.notas)
        if promedio >= 4:
            return True
        return False
    
class Curso:

    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def estudiantes_aprobados(self):
        resultado = []
        for estudiante in self.estudiantes:
            if estudiante.promedio_mas_de_4():
                resultado.append(estudiante.nombre)
        
        return resultado

e1 = Estudiante("Ricardo","28122222")
e2 = Estudiante("Ingrid","2799999")
e1.agregar_nota(5)
e1.agregar_nota(4)
e1.agregar_nota(1)
e2.agregar_nota(6)
e2.agregar_nota(7)
e2.agregar_nota(7)
curso = Curso("IIC1103")
curso.agregar_estudiante(e1)
curso.agregar_estudiante(e2)
lista_restulado = curso.estudiantes_aprobados()
print(lista_restulado)
# crear una funcion que reciba un curso que cree una lista con el nombre del estudiante y su promedio

lista_nombres = obtener_promedios(curso)
print(lista_nombres)