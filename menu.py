from jugadores import buscar_jugador
from top_rebotes import ver_top_rebotes
from top_asistencias import ver_top_asistencias
from top_puntos import ver_top_puntos
from estructuras.cola_prioridad import MaxHeapNBA
from estructuras.grafo_nba import GrafoNBA
from recomendaciones import obtener_recomendaciones
from top_equipos import mostrar_top_equipos_heap
from buscar_equipo import buscar_equipo
from rivalidades_grafo import mostrar_red_rivalidades_grafo


def menu_principal (arbol_equipos, arbol_categorias): 
    while True:
        print("""
========================================
            UNABSTATS 
========================================

1. Buscar jugador
2. Explorar Equipos (Buscar por AVL)
3. Ver Top 5 Puntos
4. Ver Top 5 Asistencias
5. Ver Top 5 Rebotes
6. Obtener recomendaciones
7. Explorar Categorías Jerárquicas (Árbol General)
8. Ver Top 5 Equipos (Heap)
9. Mostrar partidos jugados entre equipos (Grafo)
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
            input("\nPresioná [Enter] para volver al menú principal...")

        elif opcion == "8":
            mostrar_top_equipos_heap()

        elif opcion == "9":
            mostrar_red_rivalidades_grafo()


        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida.")
            # Agregamos esto para ver que pasa si no reconoce el 7:
            input("Presioná [Enter] para continuar...")