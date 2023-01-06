# CREANDO ARCHIVOS DESDE PYTHON

"""
La creacion de archivos en Python se ha vuelto una 
practica muy utilizada para almacenar datos generador por un script.

La sintaxis a utilizar es: archivo = open(NOMBRE_ARCHIVO, Parametro)

Parametros:
w = escritura
r = lectura
"""

def Escribir():
    # Crear archivo
    archivo = open("16_Archivo_Prueba.txt", "w")

    # Escribir una secuencia del 1 al 20
    for i in range(0, 20):
        archivo.write("Se ha escrito " + str(i) + "\n")

    # Cerrar archivo
    archivo.close()

def Leer():
    # Si lo que queremos es que el archivo se cierre por si mismo

    with open("16_Archivo_Prueba.txt", "r") as archivo:
        # Notas importantes
        # 1. Si solo se quiere leer un archivo se puede omitir el parametro "r"
        # 2. "as archivo" es una forma de asignar una operacion a una variable

        # Leer archivo linea por linea
        for linea in archivo:
            print(linea.rstrip()) # "rstrip" elimina los saltos de linea

Escribir()
Leer()
