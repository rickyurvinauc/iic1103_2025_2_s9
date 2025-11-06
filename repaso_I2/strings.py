
texto = "  Python en Datos  "

# Indexacion y slicing
print("Primer caracter:", texto[2])            # espacio -> indice 2
print("Subcadena:", texto[2:8])                # "Python"
print("Ultimo caracter:", texto[-1])           # espacio

# Metodos comunes
limpio = texto.strip()
print("strip():", limpio)               # "Python en Datos"

mayus = limpio.upper()
minus = limpio.lower()
print("upper():", mayus)
print("lower():", minus)

print("find('Datos'):", limpio.find("Datos"))  # posicion
print("count('o'):", limpio.count("o"))        # conteo

partes = limpio.split(" ")
print("split(' '):", partes)                   # lista de palabras

unido = "-".join(partes)
print("join('-'):", unido)