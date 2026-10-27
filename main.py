import tablero

# Se crea el tablero
mi_tablero = tablero.Tablero(3)
# Se rellena el tablero
mi_tablero.fill_tablero()
print("Selecciona una opción:")
opcion = input("1. Mostrar tablero\n2. Salir\n")
while opcion != "2":
    if opcion == "1":
        mi_tablero.show_tablero()
    else:
        print("Opción no válida. Intenta de nuevo.")
    print("\nSelecciona una opción:")
    opcion = input("1. Mostrar tablero\n2. Salir\n")
