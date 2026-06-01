#----MENÚ PRINCIPAL----
print("1.Ver inventario")
print("2.Registrar venta")
print("3.Salir")
a=input("Bienvenid@ por favor elija una de las opciones: ").strip().lower()
while True:
    if a=="1":
        print("1.-Rosas")
        print("2.-Tulipanes")
        print("3.-Margaritas")
        print("4.-Lirios")
        print("5.-Girasoles")
        print("6.-Orquídeas")
        opcion=input("Por favor elija el tipo de flor:").strip().lower()
        if opcion=="1":
             print("Ramo pequeño: 10")
             print("Ramo mediano: 25")
             print("Ramo grande: 50")
             print("Ramo extragrande: 100")
             break
        elif opcion=="2":
             print("Ramo pequeño: 10")
             print("Ramo mediano: 25")
             print("Ramo grande: 50")
             print("Ramo extragrande: 100")
             break
        elif opcion=="3":
            print("Ramo pequeño: 5")
            print("Ramo mediano: 15")
            print("Ramo grande: 30")
            print("Ramo extragrande: 60")
            break
        elif opcion=="4":
             print("Ramo pequeño: 20")
             print("Ramo mediano: 35")
             print("Ramo grande: 60")
             print("Ramo extragrande: 120")
             break
        elif opcion=="5":
             print("Ramo pequeño: 20")
             print("Ramo mediano: 35")
             print("Ramo grande: 60")
             print("Ramo extragrande: 120")
             break
        elif opcion=="6":
             print("Ramo pequeño: 10")
             print("Ramo mediano: 25")
             print("Ramo grande: 50")
             print("Ramo extragrande: 100")
             break
        else:
                print("Opción incorrecta")
                break
    elif a=="2":
        flor=input("Ingrese el tipo de flor que desea:").strip().lower()
        precio=input("Ingrese el tamaño del ramo:").strip().lower()
        break
    elif a=="3":
         print("Saliendo del sistema")
         break
    else :
         print("Opción inválida")
         break