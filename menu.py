from jugadores import buscar_jugador

def buscar_equipo(arbol_equipos): # ---> se modifica arbol a arbol_equipos
    nombre_a_buscar = input("Ingrese el nombre del equipo a buscar: ").lower()
    resultado = arbol_equipos.buscar(nombre_a_buscar, clave=lambda e: e['nombre'].lower())
    if resultado:
        print("\n--- Equipo Encontrado ---")
        print(f"Datos: {resultado}")
    else:
        print("\nNo se encontro ningun equipo con ese nombre.")

def menu_principal (arbol_equipos, arbol_categorias): # ---> menu_pricipal recibe tanto el arbol_equipos como el arbol_categorias en lugar de arbol
    while True:
        print("""
========================================
            UNABSTATS 
========================================

1. Buscar jugador
2. Explorar Equipos (Buscar por AVL)
3. Ver Top 5 Puntos
4. Ver Top 5 Asistencias
5. Ver top 5 Rebotes
6. Obtener recomendaciones
7. Explorar Categorías Jerárquicas (Árbol General)
0. Salir

----------------------------------------""")
     
     
        opcion = input("Seleccioná una opción: ")

        if opcion == "1":

            nombre = input("Ingrese el nombre del jugador: ")

            buscar_jugador(nombre)

        elif opcion == "2":
            buscar_equipo(arbol_equipos) # ----> se modifica arbol por arbol_equipos

        elif opcion == "3":
            ver_top_puntos()

        elif opcion == "4":
            ver_top_asistencias()

        elif opcion == "5":
            ver_top_rebotes()
        
        elif opcion == "6":
            obtener_recomendaciones()

        elif opcion == "7":
            print("\n--- Categorías de la NBA (Recorrido en amplitud) ---")
            for cat in arbol_categorias.amplitud():
                print(f" -> {cat}")

            # esta linea congela la pantalla hasta que se presione Enter
            input("\nPresioná [Enter] para volver al menú principal...")


        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida.")
            # Agregamos esto para ver que pasa si no reconoce el 7:
            input("Presioná [Enter] para continuar...")
            
