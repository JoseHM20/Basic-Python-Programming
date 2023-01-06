# CREANDO CONJUNTOS

# Los conjuntos permiten la no repeticion de elementos

Edades = set()
# Si el conjunto tendra elementos definidos podemos saltar esto
Edades = {5, 10, 9, 8, 11, 15, 17, 20, 5, 10, 9} # Conjunto desordenado
"""El agregar valores repetidos no provoca error, pero solo apareceran los primeros detectados"""

# Agregar elementos al conjunto
Edades.add(1) # Sin posicion especifica
print(Edades)

# Eliminar elemento del conjunto 
Edades.discard(11)
print(Edades)

# Eliminar todos los elementos de un conjunto
Edades.clear()
print(Edades)
