# CREANDO CICLOS WHILE

# Este es un ciclo que se ejecutara hasta que se cumpla una condicion

# EJEMPLO 1
# Jugando con contadores
count = 0
while count < 5:
    print("Aumentando en uno el contador")
    count = count + 1
    print(count)
print("Termino el ciclo")

# EJEMPLO 2
# Dinero en el bolsillo

dinero = int(input("Ingresa el saldo actual: "))
while dinero < 0:
    print("Cantidad invalida, volver a intentar")
    dinero = int(input("Ingresa el saldo actual: "))
print("Dinero comprobado")
