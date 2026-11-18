from estructuras.cola_prioridad import MaxHeapNBA
from estructuras.grafo_nba import GrafoNBA

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