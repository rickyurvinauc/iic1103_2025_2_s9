class Candidato:
    def __init__(self, nombre, votos, edad):
        self.nombre = nombre
        self.votos = votos
        self.edad = edad

    def __str__(self):
        return self.nombre + " - votos: " + str(self.votos) + " - edad: " + str(self.edad)

c1 = Candidato("Dora", 1200, 25)
c2 = Candidato("Bob", 950, 30)
c3 = Candidato("Homero", 1500, 45)
c4 = Candidato("Lisa", 1500, 20)

candidatos = [c1, c2, c3, c4]

def criterio_votos(candidato):
    return candidato.votos

candidatos.sort(key=criterio_votos, reverse=True)

for c in candidatos:
    print(c)
# Homero - votos: 1500 - edad: 45
# Lisa - votos: 1500 - edad: 20
# Dora - votos: 1200 - edad: 25
# Bob - votos: 950 - edad: 30
candidatos = [c1, c2, c3, c4]
def criterio_votos_edad(candidato):
    return candidato.votos, -candidato.edad

resultados = sorted(candidatos, key=criterio_votos_edad, reverse=True)
print("-"*10)
for c in resultados:
    print(c)
# Lisa - votos: 1500 - edad: 20
# Homero - votos: 1500 - edad: 45
# Dora - votos: 1200 - edad: 25
# Bob - votos: 950 - edad: 30