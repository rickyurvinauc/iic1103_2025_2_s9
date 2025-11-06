class Caja:
    def __init__(self, peso_max, muestras=[]):
        self.peso_max = peso_max
        self.muestras = muestras

    def agregar_muestra(self, muestra):
        if len(self.muestras) == 0 and self.peso_max <= muestra.peso:
            self.muestras.append(muestra)
            return True
        peso_actual = 0
        for mues in self.muestras:
            peso_actual += mues.peso
        peso_total = peso_actual + muestra.peso
        tipo_pri = self.muestras[0].riesgo()
        if peso_total <= self.peso_max and tipo_pri == muestra.riesgo():
            self.muestras.append(muestra)
            return True
        return False

    def contar_fragiles(self):
        conteo = 0
        for muestra in self.muestras:
            if muestra.fragil == True:
                conteo += 1
        return conteo