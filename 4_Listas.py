# MANEJO DE LISTAS

Alumnos = ["Juan", "Gerardo", "Luis", "Pedro", "Carlos"]
# El primer elemento de una lista esta en la posicion 0

# Imprimir la lista completa
print(Alumnos)

# Imprimir una posicion de la lista
print(Alumnos[0])

# Ordenar la lista alfabeticamente
Alumnos.sort()
print(Alumnos)

# Usando las listas en mensajes
mensaje = f"{Alumnos[4]} reprobo el semestre"
print(mensaje)

# Remplazar valores de una lista
Alumnos[3] = "Karla" # Se remplaza a Luis porque ordenamos la lista antes

# Agregar valores a una lista
Alumnos.append("Marcelo")
print(Alumnos)

# Eliminar valores de una lista
del Alumnos[4]
print(Alumnos)

# Eliminar el ultimo elemento de una lista
Alumnos.pop()
print(Alumnos)

# Eliminar valores mediante el nombre
Alumnos.remove("Juan")
print(Alumnos)

# Unir dos listas
Maestros = ["Raul", "Enrique", "Lucero", "Alondra"]
Grupo = Alumnos + Maestros
print(Grupo)