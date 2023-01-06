# CLASES Y POLIMORFISMO

"""
El polimorfismo permite  auna clase hija tomar un metodo
y utilizarlo de forma diferente.
"""

class Alumno:
    def __init__(self, nombre, edad, registro):
        self.Nombre_Alumno = nombre
        self.Edad_Alumno = edad
        self.No_Registro = registro # Atributo encapsulado
    
    def MostrarInfor(self):
        print(f"El alumno se llama {self.Nombre_Alumno}, tiene {self.Edad_Alumno} años y su numero de registro es {self.No_Registro}")

class Alumno2(Alumno):
    def __init__(self, nombre, edad, registro, alias): # Agregar lo que se requiera
        super().__init__(nombre, edad, registro) # Importar clase padre (valores fijos)
        self.pronombre = alias # Polimorfismo de variables
    
    # Funciones del padre reescritas es polimorfismo tambien
    def MostrarInfor(self):
        print(f"El alumno se llama {self.Nombre_Alumno}, tiene {self.Edad_Alumno} años y su numero de registro es {self.No_Registro} y su alias es {self.pronombre}")

escuela = Alumno2("Jose Luis", 19, 1001, "Pepe")
escuela.MostrarInfor()