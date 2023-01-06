# CREANDO CLASES

# Zona de importacionn de librerias
import time

# Definicion: Una clase es una forma de almacenar ciertos datos y funcionalidades.

clientes = {}

class Cliente_BBVA:
    while 1 == 1:

        def Agregar_Cliente(Nombre_Cliente, Datos_Cliente): # Importar variables
            clientes[Nombre_Cliente] = Datos_Cliente # Agregar clave  y valor al diccionario
            time.sleep(2)
            print("Cliente agregado con exito...")
            print(clientes)
        
        def Eliminar_Cliente(Nombre_Cliente): # Importar variables
            if clientes.get(Nombre_Cliente): # Comprobar existencia del cliente
                del(clientes[Nombre_Cliente]) # Eliminar clave y valor al diccionario
                time.sleep(2)
                print("Cliente eliminado con exito...")
                print(clientes)
            else:
                time.sleep(2)
                print(f"{Nombre_Cliente} no ha sido detectado")
        
        print("[1] Agregar cliente \n[2] Eliminar cliente \n[3] Ver base de datos \n[4] Salir de la aplicacion")
        Accion = int(input("Eliga una opcion: "))

        if Accion == 1:
            Cliente = input("Escribe el nombre de el cliente: ")
            Datos = input("Escriba la edad y pais del cliente: ")
            Añadir = Agregar_Cliente(Cliente, Datos)
        elif Accion == 2:
            Cliente = input("Escribe el nombre de el cliente: ")
            Eliminar = Eliminar_Cliente(Cliente)
            print(Eliminar)
        elif Accion == 3:
            print("Cargando base de datos...")
            print(clientes)
        elif Accion == 4:
            print("Saliendo de la aplicacion...")
            exit()
        
        print()

Cliente_BBVA()
