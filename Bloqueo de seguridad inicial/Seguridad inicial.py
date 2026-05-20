#Proyecto Sistema de ventas de Floristería
#Paso nº1 : Bloqueo de seguridad inicial
contraseña_correcta="FloresGiovi"
usuario="Giovi16"
while True:
    nombre=input("Ingrese su nombre de ususario: ").strip()
    clave=input("Ingrese la contraseña: ").strip()
    if clave==contraseña_correcta and nombre==usuario:
        print("Acceso concedido")
        break
    else:
        print("Contraseña incorrecta, intentelo de nuevo")