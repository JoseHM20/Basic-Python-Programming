# ENCAPSULANDO DATOS DE CLASES

"""
La encapsulacion de datos es simplemente la proteccion de un valor
en una variable. Es decir, no podra ser modificado despues en el codigo.

Esto se logra mediante el uso de la siguiente sintaxis:
self.__variable = 10
"""

class Variables:
    def __init__(self):
        self.variable_publica = "Soy la variable publica"
        self.__variable_privada = "Soy la variable privada" # Agregar guiones bajos

var = Variables()
print(var.variable_publica)
print(var.__variable_privada) # Lanzara un error

# ----------------------------------------------------------

class Alumno:
    def __init__(self, nombre, edad, registro):
        self.Nombre_Alumno = nombre
        self.Edad_Alumno = edad
        self.__No_Registro = registro # Atributo encapsulado

alumno1 = Alumno("Pepe", 18, 1000)
print(alumno1.Nombre_Alumno)
print(alumno1.Edad_Alumno)
print(alumno1.__No_Registro) # No se puede mostrar


