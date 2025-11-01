class Muestra:
    def __init__(self, tipo, peso, fragil):
        self.tipo = tipo
        self.peso = peso
        self.fragil = fragil

    def riesgo(self):
        if self.tipo in ["sangre", "orina"] and self.peso > 100:
            return "ALTO"
        elif self.fragil and self.tipo not in ["sangre", "orina"]:
            return "ALTO"
        else:
            return "BAJO"

    def __str__(self):
        return f"Muestra de tipo {self.tipo} y peso {self.peso}g"


class Caja:
    def __init__(self, peso_max):
        self.peso_max = peso_max
        self.muestras = []

    def agregar_muestra(self, nueva):
        total_actual = 0
        for m in self.muestras:
            total_actual += m.peso

        if total_actual + nueva.peso <= self.peso_max:
            if self.muestras != []:
                if self.muestras[0].riesgo() == nueva.riesgo():
                    self.muestras.append(nueva)
                    return True
                else:
                    return False
            else:
                self.muestras.append(nueva)
                return True
        else:
            return False

    def contar_fragiles(self):
        n = 0
        for m in self.muestras:
            if m.fragil:
                n += 1
        return n