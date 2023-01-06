# CREANDO CONDICIONES CON OPERAODRES OR, AND

# EJEMPLO 1
# 1: Encendido / Conectado
# 0: Apagado / Desconectado
Sistema = 1
Usuario = 1

if Sistema == 1 and Usuario == 1:
    print("ACCESO AUTORIZADO")
elif Sistema == 0 and Usuario == 1:
    print("Sistema en mantenimiento")
elif Sistema == 1 and Usuario == 0:
    print("Sin suarios en linea")
elif Sistema == 0 and Usuario == 0:
    print("Sin servicio")
else:
    print("Conexiones desconocidas")
