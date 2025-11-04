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
        if sum(self.notas) / len(self.notas) > 4:
            return True
        return False
    
    def cambiar_nombre(self, nombre):
        self.nombre = nombre

    def misma_carrea(self, estudiante2):
        if self.carrera == estudiante2.carrera:
            return True
        return False

vivi = Estudiante(1,"Vivi","Ing. Civil")
ricardo = Estudiante(2, "Ricardo","Dc. DCC")

print(vivi) # Hola soy Vivi y mi promedio de notas es 4.5

nombre = "Ricardo"
print(type(vivi))
