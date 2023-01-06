# CREANDO CONDICIONES

# EJEMPLO 1
Saldo = 500 # Recomendado: Insertar valores desde terminal
Deuda = 2000

if Saldo == Deuda:
    print("La deuda ha sido pagada con exito")
elif Saldo < Deuda:
# Pueden existir tantos elif como sea necesario
    print("Saldo insuficiente, pago no realizado")
elif Saldo > Deuda:
    resto = Deuda - Saldo
    print(f"Ha pagado su deuda y le sobran {resto} pesos")
else:
    print("Error 001: No se ha procesado el pago")


# EJEMPLO 2
Edad = 10

if Edad == 0:
    print("¡Bienvenido al mundo!")
elif Edad == 18:
    print("Eres mayor de edad ahora")
elif Edad > 60:
    print("Ya eres algo viejo")
elif Edad < 0:
    print("No es valida esta edad, vuelva a intentarlo")
else:
    print("Sigue asi")


# EJEMPLO 3
Admin_Name = "Jose"
Admin_Key = 12345

if Admin_Name == "Jose":
    print("Acceso en espera...")
    if Admin_Key == 12345:
        print("Contraseña valida")
        print("ACCESO AUTORIZADO")
    else:
        print("ACCESO DENEGADO")
        exit()
else:
    print("Usuario sin privilegios...")
    print("ACCESO AUTORIZADO")