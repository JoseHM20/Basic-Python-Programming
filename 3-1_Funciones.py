# Creando funciones

# Sintaxis: def NombreFuncion():
# def: palabra de definir
# NombreFuncion: Nombre a asignar a la funcion

def Nombre_Cliente():
    print("Juan Rafael Moreira") # Se debe respetar el espacio (identacion)

print("Esto esta afuera de la funcion")

# Notar que si se ejecuta aso solo se imprimira el print que esta fuera de la funcion
# Para que la funcion funcione deberemos de mandarla llamar

Nombre_Cliente() # Se imprimen resultados


def SUMA():
    # Almacenar valores enteros en variables
    a = 5
    b = 10

    resultado = a + b # Almacenar resultado en otra variable
    print(resultado) # Imprimir resultado
SUMA()

def RESTA():
    # Almacenar valores enteros en variables
    a = 50
    b = 10

    resultado = a - b # Almacenar resultado en otra variable
    print(resultado) # Imprimir resultado
RESTA()