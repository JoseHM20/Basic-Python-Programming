# CREANDO TUPLAS

# Las tuplas no pueden ser modificadas

Num_Primos = (2, 3, 5, 5, 7, 11, 13, 17, 19)

# Num_Primos.append(23)
# del Num_Primos(3)

print(Num_Primos)

# Mostrar un unico elemento
print(Num_Primos[2])

# Verificar existencia de elementos
print(3 in Num_Primos)

# Arrojar la posicion del elemento
print(Num_Primos.index(17)) # Si hay mas de un valor igual toma el mas cercano

# Mostrar cuantas coincidencias hay de un elemnto
print(Num_Primos.count(5))

# Mostrar la cantidad de elementos totales de la tupla
print(len(Num_Primos))

# Transformar tuplas a listas
lista = list(Num_Primos)
print(lista)

#  Transformar listas a tuplas
tupla = tuple(lista)
print(tupla)