# DESENCAPSULANDO DATOS DE CLASES

"""
Cuando el atributo es convertido a privado no quiere decir que no se 
pueda editar ni mostrar. Pero este proceso debe ser ejecutado desde 
dentro de la clase creada y con las funciones Getter y Setter.
"""

class Alumno:
    # Cambiar 2 de los atributos a privado
    def __init__(self, nombre, edad, registro):
        self.Nombre_Alumno = nombre
        self.__Edad_Alumno = edad # Atributo encapsulado
        self.__No_Registro = registro # Atributo encapsulado
    
    # MANDAR LLAMAR A UNA VARIABLE PRIVADA DESDE FUERA DE LA CLASE
    # ------------------------------------------------------------

    # Por cuestiones de orden se escribe la funcion con el nombre del atributo
    def Get_Edad_Alumno(self):
        print(self.__Edad_Alumno)
    
    def Get_No_Registro(self):
        print(self.__No_Registro)
    
    # EDITAR VALORES DE LA VARIABLE PRIVADA
    # -----------------------------------------------------------

    def Set_Edad_Alumno(self, edad):
        self.__Edad_Alumno = edad
        print(self.__Edad_Alumno)

    def Set_No_Registro(self, registro):
        self.__No_Registro = registro
        print(self.__No_Registro)
    

alumno1 = Alumno("Pepe", 18, 1000) # Se mantiene la instancia

# IMPRIMIR VARIABLES
#   publicas
print(alumno1.Nombre_Alumno)
#   privadas
alumno1.Get_Edad_Alumno()
alumno1.Get_No_Registro()

# EDITAR VARIABLES
alumno1.Set_Edad_Alumno(20)
alumno1.Set_No_Registro(1001)

