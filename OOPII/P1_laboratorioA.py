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