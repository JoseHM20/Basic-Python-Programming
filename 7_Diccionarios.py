# CREANDO DICCIONARIOS

# sintaxis: NombreDiccionario = {"Clave1" : "Valor1", "Clave2" : "Valor2"}

colores = {1: "Azul", 2: "Verde", 3: "Amarillo"}
print(colores)

# Mostrar cantidad total de elementos en el diccionario
print(len(colores))

# Buscar en el diccionario
print(colores.get(1, "No se a descubierto este color"))
print(colores.get(5, "No se a descubierto este color"))

# Mostrar solo las claves de el diccionario
print(colores.keys())

# Mostrar solo los valores de el diccionario
print(colores.values())

# Añadir elementos al diccionario
colores[4] = "Rojo" # Sin posicion especifica
print(colores)

# Eliminar elementos de un diccionario
del(colores[1])
print(colores)

# Eliminar todos los elementos de un diccionario
limpiar = colores.clear
print(limpiar)

poblcacion = {"Juan":{"edad": 35, "Estatura":1.75}, "Mariana":{"edad": 18, "Estatura":1.65}}
print(poblcacion)