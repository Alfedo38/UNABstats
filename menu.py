from jugadores import buscar_jugador
from estructuras.cola_prioridad import MaxHeapNBA
from estructuras.grafo_nba import GrafoNBA

def buscar_equipo(arbol_equipos): # ---> se modifica arbol a arbol_equipos
    nombre_a_buscar = input("Ingrese el nombre del equipo a buscar: ").lower()
    resultado = arbol_equipos.buscar(nombre_a_buscar, clave=lambda e: e['nombre'].lower())
    if resultado:
        print("\n--- Equipo Encontrado ---")
        print(f"Datos: {resultado}")
    else:
        print("\nNo se encontro ningun equipo con ese nombre.")

def mostrar_top_equipos_heap(arbol_equipos=None): # ---> para que la función pueda usar el árbol y buscar el rating, necesitamos pasarle el árbol como parámetro desde donde se la llama
    print("\n==================================================")
    print("      TOP 5 RECOMENDACIONES DE EQUIPOS (HEAP)     ")
    print("==================================================")
    
    # 1. Definimos la misma clase que tenemos en el archivo de prueba
    class EquipoNBA:
        def __init__(self, nombre, rating):
            self.nombre = nombre
            self.rating = rating
        def __repr__(self):
            return f"{self.nombre} (Rating: {self.rating})"

    # 2. La lista de datos duros tal cual se armó en la prueba
    equipos = [
        EquipoNBA("Boston Celtics", 8.1),
        EquipoNBA("Miami Heat", 0.2),
        EquipoNBA("Golden State Warriors", 2.1),
        EquipoNBA("Los Angeles Lakers", -0.7),
        EquipoNBA("San Antonio Spurs", 8.3),
        EquipoNBA("Chicago Bulls", -1.8),
        EquipoNBA("New York Knicks", 9.3),
        EquipoNBA("Detroit Pistons", 8.8),
        EquipoNBA("Philadelphia 76ers", 2.3),
        EquipoNBA("Milwaukee Bucks", 1.8)
    ]
    
    # 3. Inicializamos el MaxHeapNBA e insertamos especificando la prioridad
    heap = MaxHeapNBA()
    for eq in equipos:
        heap.insertar(eq, prioridad=eq.rating)

    # 4. Obtenemos el top 5 y lo imprimimos usando el formato de la prueba
    # Usamos la función que tenga asignada la estructura (obtener_top_n u obtain_top_n)
    if hasattr(heap, 'obtain_top_n'):
        top_5 = heap.obtain_top_n(5)
    else:
        top_5 = heap.obtener_top_n(5)

    for i, eq in enumerate(top_5, 1):
        print(f"{i}. {eq}")

    
    print("--------------------------------------------------")
    input("\nPresioná [Enter] para volver...")

def mostrar_red_rivalidades_grafo():
    print("\n==================================================")
    print("        RED DE CONEXIONES Y RIVALIDADES NBA       ")
    print("==================================================")
    grafo = GrafoNBA()
    grafo.agregar_rivalidad("Boston Celtics", "Los Angeles Lakers", 12)
    grafo.agregar_rivalidad("Boston Celtics", "Miami Heat", 8)
    grafo.agregar_rivalidad("Golden State Warriors", "Los Angeles Lakers", 10)
    grafo.agregar_rivalidad("San Antonio Spurs", "Los Angeles Lakers", 6)
    
    grafo.mostrar_red()
    print("--------------------------------------------------")
    input("\nPresioná [Enter] para volver...")

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

            # esta linea congela la pantalla hasta que se presione Enter
            input("\nPresioná [Enter] para volver al menú principal...")

        elif opcion == "8":
            mostrar_top_equipos_heap(arbol_equipos) # ---> acá también pasamos el árbol como en la funcion mostrar_top_equipos_heap()

        elif opcion == "9":
            mostrar_red_rivalidades_grafo()


        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida.")
            # Agregamos esto para ver que pasa si no reconoce el 7:
            input("Presioná [Enter] para continuar...")