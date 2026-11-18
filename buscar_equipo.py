def buscar_equipo(arbol_equipos): # ---> se modifica arbol a arbol_equipos
    nombre_a_buscar = input("Ingrese el nombre del equipo a buscar: ").lower()
    resultado = arbol_equipos.buscar(nombre_a_buscar, clave=lambda e: e['nombre'].lower())
    if resultado:
        print("\n--- Equipo Encontrado ---")
        print(f"Datos: {resultado}")
    else:
        print("\nNo se encontro ningun equipo con ese nombre.")

        