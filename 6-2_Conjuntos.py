# CREANDO CONJUNTOS ARITMETICOS

# Edades de dos grupos
grupo_1 = {5, 10, 15, 20, 25}
grupo_2 = {3, 6, 9, 12, 15}

# Comparar conjuntos
grupo_3 = grupo_1 | grupo_2
print(grupo_3)

# intercepcion entre dos conjuntos
grupo_4 = grupo_1 & grupo_2
print(grupo_4)

# Diferencia entre dos conjuntos
a = {1, 2, 3}
b = {1, 4, 5}

c = a - b # Elementos de a que no estan en b
print(c)

# Diferenciar valores que no estan en a y b al mismo tiempo
d = a ^ b # Elementos de a que no estan en b
print(d)

# Validar que a es un subconjunto de e
conjunto = {1, 2, 3, 4, 5, 6}
print(a.issubset(conjunto))

# Evitar que se modifique un conjunto
inmutable = frozenset(conjunto)