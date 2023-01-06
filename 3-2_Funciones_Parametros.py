# Creando funciones con parametros

# Sintaxis: def NombreFuncion(parametro1,..,parametroN):
# def: palabra de definir
# NombreFuncion: Nombre a asignar a la funcion

# Realicemos una suma
def SUMA(a, b): # A y B representan parametros que se inyectaran
    
    # sumar valores
    resultado = a + b

    print(resultado) # Forma basica de impresion

    print(f"El resultado de la suma es {resultado}") # Forma mas formal
    # "F" nos dice que hay una variable dentro de la cadena
    # "{}" almacena la variable a imprimir

    print("El resultado de la suma es",resultado) # Otra forma de imprimir
    # La "," representa un epsacio y debe estar fuera de la cadena seguido de la variable
SUMA(5, 10) # Enviamos dos valores a la funcion


def MULTIPLICACION(a, b = 10): # En este caso B tiene un valor por defecto
        
    # sumar valores
    resultado = a * b

    print(f"El resultado de la multiplicaciob es {resultado}")

MULTIPLICACION(10) # Error: Faltan argumentos
# La forma de evitar estos errores es dandole valores por defecto a la funcion

