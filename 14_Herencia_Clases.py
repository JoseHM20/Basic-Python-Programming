# HEREDANDO UNA CLASE

"""
La herencia no es mas que tomar funcionalidades 
de una clase padre y asi poder realizar mas 
copias de la misma con las diferencias que nosotros deseemos
"""

class Alumno:
    def __init__(self, nombre, edad, registro):
        self.Nombre_Alumno = nombre
        self.Edad_Alumno = edad
        self.__No_Registro = registro # Atributo encapsulado
    
    def MostrarInfor(self):
        print(f"El alumno se llama {self.Nombre_Alumno}, tiene {self.Edad_Alumno} años y su numero de registro es {self.__No_Registro}")

class Alumno2(Alumno):
    def __init__(self, nombre, edad, registro):
        super().__init__(nombre, edad, registro)

escuela = Alumno2("Jose Luis", 19, 1001)
escuela.MostrarInfor()
