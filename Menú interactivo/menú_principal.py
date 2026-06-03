nombre = ""
contraseña = ""
while True:
    print("1-. Iniciar sesión")
    print("2-. Registrarse")
    print("3-. Salir")
    opcion = input("Hola bienvenido a la Floristería Aurora Floral, por favor elija una opción: ").strip()
    if opcion == "1":
        usuario = input("Ingrese el nombre de usuario: ").strip().upper()
        clave = input("Ingrese la contraseña: ").strip().upper()
        if nombre == "" and contraseña == "":
            print("No existe ninguna cuenta registrada.")
            print("Primero debe registrarse.")
        else:
            intentos = 0
            intentos_maximo = 3
            while intentos < intentos_maximo:
                if usuario == nombre and clave == contraseña:
                    print("Acceso concedido")
                    print("Bienvenid@ al sistema de ventas de la floristería Aurora Floral")
                    inventario={
            "rosas": {
                 "stock": 200,
                 "precios": {"pequeño":10,"mediano": 25,"normal": 50, "grande": 100}
                    },
                    "tulipanes": {
                        "stock": 200,
                        "precios": {"pequeño": 10, "mediano": 25, "normal": 50, "grande": 100}
                    },
                    "margaritas": {
                        "stock": 400,
                        "precios": {"pequeño": 8, "mediano": 15, "normal": 30, "grande": 60}
                    },
                    "lirios": {
                        "stock": 250,
                        "precios": {"pequeño": 20, "mediano": 35, "normal": 60, "grande": 120}
                    },
                    "girasol": {
                        "stock": 80,
                        "precios": {"pequeño": 20, "mediano": 35, "normal": 60, "grande": 120}
                    },
                    "orquideas": {
                        "stock": 60,
                        "precios": {"pequeño": 10, "mediano": 25, "normal": 50, "grande": 100}
                    }
                }
                    while True:
                      print("---MENÚ PRINCIPAL---")
                      print("1. Ver inventario")
                      print("2. Registrar venta")
                      print("3. Actualizar inventario")
                      print("4. salir")
                      o=input("Por favor seleccione una opción: ").strip().lower()
                      if o=="1":
                          print("-Rosas")
                          print("-Tulipanes")
                          print("-Margaritas")
                          print("-Lirios")
                          print("-Girasoles")
                          print("-Orquídeas")
                          flor=input("Por favor elija el tipo de flor: ").strip().lower()
                          if flor in inventario :
                              print("Flor:",flor)
                              print("Stock:", inventario[flor]['stock'])
                              print("Precios de cada ramo:")
                              print("Pequeño:", inventario[flor]['precios']['pequeño'],"bs")
                              print("Mediano:", inventario[flor]['precios']['mediano'],"bs")
                              print("Normal:", inventario[flor]['precios']['normal'],"bs")
                              print("Grande:", inventario[flor]['precios']['grande'],"bs")
                          else:
                              print("Flor no encontrada") 
                      elif o == "2":
                          flor = input("Tipo de flor: ").strip().lower()
                          tamaño = input("Tamaño del ramo: ").strip().lower()
                          cantidad = int(input("Cantidad de ramos(Ingrese en números): "))
                          if flor in inventario:
                              if tamaño in inventario[flor]["precios"]:
                               total = inventario[flor]["precios"][tamaño] * cantidad
                               inventario[flor]["stock"] = (inventario[flor]["stock"] - cantidad)
                               print("Venta registrada")
                               print("Flor:", flor)
                               print("Tamaño:", tamaño)
                               print("Cantidad:", cantidad)
                               print("Total:", total, "Bs")
                               print("Stock restante:",inventario[flor]["stock"])
                               exit()
                          else:
                           print("Los datos ingresados son incorrectos o no estan en el sistema")
                      elif o == "3":
                          print("Actualizar el stock de la flor")
                          flor = input("Actualizar la flor: ").strip().lower()
                          flor = flor.replace(" ", "")
                          if flor in inventario:
                              cantidad = int(input("Cantidad a agregar: "))
                              inventario[flor]["stock"] = (inventario[flor]["stock"] + cantidad)
                              print("Inventario actualizado")
                              print("Nuevo stock:",inventario[flor]["stock"])
                          else:
                           print("Flor no encontrada")
                      elif o == "4":
                          print("Saliendo del sistema...")
                          exit()
                      else:
                         print("Opción inválida")
                else:
                    intentos += 1
                    if intentos == intentos_maximo:
                        print("Acceso bloqueado. Superó el límite de intentos.")
                        exit()
                    print("Usuario o contraseña incorrectos")
                    usuario = input("Ingrese el nombre de usuario: ").strip().upper()
                    clave = input("Ingrese la contraseña: ").strip().upper()
    elif opcion == "2":
        nombre = input("Cree un nombre de usuario: ").strip().upper()
        contraseña = input("Cree una contraseña: ").strip().upper()
        print("Registro exitoso.")
        print("Ahora puede iniciar sesión.")
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")
