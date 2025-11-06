class Planta:

    def __init__(self, nombre, resistencia):
        self.nombre = nombre
        self.resistencia = resistencia
        self.agua = 0

    def __str__(self):
        return f"{self.nombre} - {self.agua}/{self.resistencia}"

    def regar(self, agua):
        # Calculamos el total de agua que habria despues de regar:
        total = agua + self.agua

        # Si el total es menor o igual a la resistencia, la planta acepta todo el agua.
        if total <= self.resistencia:
            # Actualizamos el estado de agua con el total calculado.
            self.agua = total
        else:
            # Si el total excede la resistencia, limitamos el agua al maximo permitido.
            # Evitamos que self.agua supere self.resistencia.
            self.agua = self.resistencia
