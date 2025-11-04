# Escribe tu código aquí

class Muestra:

    def __init__(self, tipo, peso, fragil):
        self.tipo = tipo
        self.peso = peso
        self.fragil = fragil

    def __str__(self):
        texto = "Muestra de tipo "+ self.tipo +" y peso "+ str(self.peso)+"g"
        return texto

    def riesgo(self):
        if ((self.tipo == "sangre" or self.tipo == "orina") and self.peso > 100 ) \
         or (self.fragil == True and self.tipo != "sangre" and self.tipo != "orina"):
         return "ALTO"
        else:
            return "BAJO"
        