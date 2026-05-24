#Proyecto Sistema de ventas de Floristería
#Bloqueo de seguridad inicial
print("Floristeria Aurora Floral")
contraseña=input("Cree una contraseña para ingresar al sistema: ").strip()
intentos=0
intentos_máximo=3
while intentos<intentos_máximo:
    clave=input("Ingrese la contraseña: ").strip()
    if clave==contraseña:
        print("Acceso concedido")
        print("Bienvenid@ al sistema de ventas de la floristería 'Aurora Floral'")
        break
    else:
        intentos +=1
        print("Contraseña incorrecta, intentelo de nuevo")
if intentos==intentos_máximo:
    print("Acceso bloqueado.Superó el límite de intentos")
