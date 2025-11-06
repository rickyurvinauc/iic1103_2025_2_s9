a = [3, 1, 4]
print("lista inicial:", a)

a.append(1)
print("append(1):", a)

a.insert(1, 9)
print("insert(1,9):", a) # inserta en la posicion 1, el numero 9

a.remove(4)
print("remove(4):", a)

x = a.pop()  # saca el ultimo
print("pop(): valor =", x, " ->", a)

copia = a.copy()
copia.sort()
print("copy() y sort():", copia, " (original:", a, ")")

copia.reverse()
print("reverse():", copia)

print("len(a):", len(a))
print("concatenacion:", a + [7, 8])
print("repeticion:", [0] * 5)
print("pertenencia 9 in a:", 9 in a)

# slicing
b = [0, 1, 2, 3, 4, 5]
print("slicing b[2:5]:", b[2:5])