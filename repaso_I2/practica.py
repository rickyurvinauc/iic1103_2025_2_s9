
# Escribe tu código aquí
import astrometro as ast

class Planeta:
    def __init__ (self, nombre, masa, radio, temperatura, distancia_estrella, metodo_deteccion):
        self.nombre= nombre
        self.masa= float(masa)
        self.radio= float(radio)
        self.temperatura= float(temperatura)
        self.distancia_estrella= float(distancia_estrella)
        self.metodo_deteccion= metodo_deteccion
    def __str__(self):
        return f"PLANETA {self.nombre}\nMasa: {self.masa} MT - Radio: {self.radio} RT - Temp: {self.temperatura} K - Dist: {self.distancia_estrella} UA - Deteccion: {self.metodo_deteccion}"
    def calcular_densidad(self):
        volumen= (4/3)*3.14*(self.radio)**3
        return round(self.masa/volumen, 2)
    def tipo_planeta(self):
        densidad= self.calcular_densidad()
        if densidad < 0.3:
            return "Gigante Liviano"
        elif densidad < 3:
            return "Tierra Rocosa"
        elif densidad >= 3:
            return "Mundo Compacto"
    def esta_en_zona_habitable(self):
        if self.temperatura >= 243 and self.temperatura <= 313 and self.distancia_estrella>=0.75 and self.distancia_estrella<= 1.25:
            return True
        else:
            return False

class CatalogoEstelar:
    def __init__(self, nombre_catalogo):
        self.nombre_catalogo= nombre_catalogo
        self.planetas= []
    def agregar_planeta(self, planeta):
        self.planetas.append(planeta)
        print(f"{planeta.nombre} correctamente agregado al catalogo {self.nombre_catalogo}")
    def cargar_catalogo(self):
        archivo= open("planetas.csv", "r")
        for planeta in archivo:
            linea= planeta.strip().split(",")
            if len(linea)== 6:
                solo_float= True
                for l in linea:
                    if "N/A" in l:
                        solo_float= False
            if solo_float:
                instancia_planeta= Planeta(linea[0],linea[1],linea[2],linea[3], linea[4], linea[5])
                if float(instancia_planeta.masa)>0 and float(instancia_planeta.radio)>0 and float(instancia_planeta.temperatura)>0 and float(instancia_planeta.distancia_estrella)>0:
                    self.agregar_planeta(instancia_planeta)
    def mostrar_planetas(self):
        if len(self.planetas)== 0:
            print(f"{self.nombre_catalogo} no contiene planetas")
        else:
            for planeta in self.planetas:
                print(planeta)
    def buscar_planeta(self, nombre_planeta):
        no_encontro= True
        for planeta in self.planetas:
            if planeta.nombre== nombre_planeta:
                no_encontro= False
                return planeta
            if no_encontro:
                return -1
    def buscar_planetas_habitables(self):
        lista= []
        for planeta in self.planetas:
            if planeta.esta_en_zona_habitable():
                lista.append(planeta)
                return lista
    def promedio_temperaturas(self):
        if len(self.planetas) == 0:
            return 0
        else:
            suma=0
            for planeta in self.planetas:
                suma+= float(planeta.temperatura)
                return round(suma/len(self.planetas),2)
    def conteo_tipo_planetas(self):
        cantidad_Gigantes_Livianos=0
        cantidad_Tierra_Rocosa=0
        cantidad_Mundo_Compacto=0
        for planeta in self.planetas:
            tipo= planeta.tipo_planeta()
            if tipo == "Gigante Liviano":
                cantidad_Gigantes_Livianos+=1
            elif tipo == "Tierra Rocosa":
                cantidad_Tierra_Rocosa+=1
            else:
                cantidad_Mundo_Compacto+=1
            print(f"Conteo de planetas en el catalogo {self.nombre_catalogo}\n- Gigante Liviano: {cantidad_Gigantes_Livianos}\n- Tierra Rocosa: {cantidad_Tierra_Rocosa}\n- Mundo Compacto: {cantidad_Mundo_Compacto}")
    
    # def existe_conexion(self, planeta1, planeta2, visitados=[]):
    #     visitados.append(planeta1)
    #     distancia = ast.distancia(planeta1, planeta2)
    #     if distancia < 5:
    #         return True
    #     for planeta in self.planetas:
    #         distancia = ast.distancia(planeta1, planeta)
    #         if distancia < 5:
    #             if planeta == planeta2:
    #                 return True
    #         if distancia< 5 and planeta not in visitados:
    #             return self.existe_conexion(planeta,planeta2,visitados)
    #
    #     return False
    def existe_conexion(self, planeta_actual, planeta_objetivo, visitados):
        visitados.append(planeta_actual)

        for planeta_siguiente in self.planetas:
            if planeta_siguiente not in visitados:
                if ast.distancia(planeta_actual, planeta_siguiente) < 5:
                    if planeta_siguiente == planeta_objetivo:
                        return True
                    if self.existe_conexion(
                        planeta_siguiente, planeta_objetivo, visitados
                    ):
                        return True
        return False
        

print("Catalogo elegido: TRAPPIST-1")
print()

planeta_1 = Planeta("TRAPPIST-1e", 0.62, 1.2, 251.0, 0.028, "Transito")
planeta_2 = Planeta("TRAPPIST-1b", 0.85, 1.12, 400.0, 0.011, "Transito")
planeta_3 = Planeta("TRAPPIST-1c", 1.38, 1.1, 334.0, 0.0158, "Transito")
planeta_4 = Planeta("TRAPPIST-1d", 0.41, 0.78, 282.0, 0.022, "Transito")
planeta_5 = Planeta("TRAPPIST-1-751f", 5.5, 2.57, 425.0, 1.18, "Imagen Directa")
planeta_6 = Planeta("TRAPPIST-1-517e", 4.59, 1.82, 302.0, 0.41, "Velocidad Radial")
planeta_7 = Planeta("TRAPPIST-1-797d", 5.45, 2.27, 413.0, 1.0, "Velocidad Radial")
planeta_8 = Planeta("TRAPPIST-1-844b", 8.81, 1.14, 406.0, 1.17, "Velocidad Radial")
planeta_9 = Planeta("TRAPPIST-1-711e", 9.19, 1.28, 375.0, 0.56, "Transito")
planeta_10 = Planeta("TRAPPIST-1-722f", 6.9, 2.11, 213.0, 1.28, "Velocidad Radial")
C_TRAPPIST_1 = CatalogoEstelar("TRAPPIST-1")
C_TRAPPIST_1.agregar_planeta(planeta_7)
C_TRAPPIST_1.agregar_planeta(planeta_8)
C_TRAPPIST_1.agregar_planeta(planeta_2)
C_TRAPPIST_1.agregar_planeta(planeta_3)
C_TRAPPIST_1.agregar_planeta(planeta_5)
C_TRAPPIST_1.agregar_planeta(planeta_1)
C_TRAPPIST_1.agregar_planeta(planeta_4)
C_TRAPPIST_1.agregar_planeta(planeta_6)
C_TRAPPIST_1.agregar_planeta(planeta_9)
C_TRAPPIST_1.agregar_planeta(planeta_10)
print()

C_TRAPPIST_1.mostrar_planetas()
print()

p1 = planeta_10
p2 = planeta_4
print(f"Verificando si existe conexion entre {p1.nombre} y {p2.nombre}...")
conexion = C_TRAPPIST_1.existe_conexion(p1, p2, [])
print("¿Estan conectados?:", conexion)