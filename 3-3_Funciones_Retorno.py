# Creando funciones que retornan valores

# Sintaxis: def NombreFuncion(parametro1,..,parametroN):
# def: palabra de definir
# NombreFuncion: Nombre a asignar a la funcion

def Alumnos(nombre):
    return nombre # Se encarga de almacenar el resultado final en una variable fuera de la funcion

Alumno = Alumnos("Juan")
# Se guardara juan como el valor de la variable alumno
print(Alumno)


# EJEMPLO 2
def SUMA(a, b):
    resultado = a + b # Se almacena el resultado en una variable
    return resultado # Se exporta el resultado

SUMADO = SUMA(10, 20)
print(SUMADO)