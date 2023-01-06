# CREANDO LA FUNCION INIT EN CLASES

# Crear clase
class Animal:
    # Otorgar valores iniciales
    """
    Nombvre = "Puppy"
    Años = 2
    Yipo = "Perro
    """

    """
    Si nos damos cuenta, debemos de otorgar valores iniciales
    de manera ibligatoria. Es por ello que usaremos la funcion 
    __init__() para poder mandar valores a la clase.
    """

    def __init__(self, nombre_animal, años_animal, tipo_animal): # Self es un valor vacio obligatorio
        # Le asignamos parametros a la funcion
        # Es importante agregar self antes de la variable
        self.Nombre = nombre_animal
        self.Años = años_animal
        self.Tipo = tipo_animal

        print(f"Mi mascota se llama {self.Nombre}, tiene {self.Años} y es un {self.Tipo}")

x = Animal("Puppy", 2, "Perro")
print(x)