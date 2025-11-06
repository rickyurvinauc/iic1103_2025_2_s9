
# crear archivo de ejemplo con with
f = open("demo.txt","w")
f.write("uno\n")
f.write("dos\n")
f.writelines(["tres\n", "cuatro\n"])
f.close()

# leer todo
contenido = open("demo.txt", "r").readlines()
print("readlines() ->")
print(contenido)


# anadir lineas
f = open("demo.txt", "a")
f.write("cinco\n")
f.writelines(["seis\n", "siete\n"])
f.close()

# recorrer linea a linea
print("for linea in open(...):")
for linea in open("demo.txt", "r"):
    print("  ", linea.strip())