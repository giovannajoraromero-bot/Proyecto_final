#Proyecto Sistema de ventas de Floristería
#Bloqueo de seguridad inicial
print("1-.Iniciar sesion")
print("2-.Registrarse")
print("3-.Salir")
opcion=input("Hola bienvenido a la Floristería Aurora Floral, por favor elija una opción: ")
while True:
    if opcion=="1":
        user=input("Por favor ingrese su nombre de ususario: ")
        c=input("Ingrese su contraseña: ")
        print("Bienvenid@ al sistema")
        break
    elif opcion=="2":
        nombre=input("Cree el nombre de usuario: ").strip()
        contraseña=input("Cree la contraseña: ").strip()
        intentos=0
        intentos_máximo=3
        while intentos<intentos_máximo:
            usuario=input("Ingrese el nombre de usuario: ").strip()
            clave=input("Ingrese la contraseña: ").strip()
            if clave==contraseña and usuario==nombre:
                print("Acceso concedido")
                print("Bienvenid@ al sistema de ventas de la floristería 'Aurora Floral'")
                exit()
            else:
                intentos +=1
                print("Contraseña o usuario incorrecto, intentelo de nuevo")
            if intentos==intentos_máximo:
                print("Acceso bloqueado.Superó el límite de intentos")
                exit()
    elif opcion=="3":
        print("Saliendo del sistema")
        break
    else:
        print("Opción inválida")
        break
