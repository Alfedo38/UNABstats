from estructuras.cola_prioridad import MaxHeapNBA
from estructuras.grafo_nba import GrafoNBA

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