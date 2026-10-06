from estructuras.avl import AVL, comparar_bst_vs_avl

class Equipo:
    def __init__(self, nombre, conferencia="Este"):
        self.nombre = nombre
        self.conferencia = conferencia

    def __repr__(self):
        return f"{self.nombre} ({self.conferencia})"

def main():
    print("=== 1. CASOS DE DESBALANCE: DATOS PERFECTAMENTE ORDENADOS ===")
    
    # 10 equipos de la NBA ordenados alfabéticamente (el peor escenario para el BST)
    datos_nba = [
        Equipo("Atlanta Hawks", "Este"),
        Equipo("Boston Celtics", "Este"),
        Equipo("Chicago Bulls", "Este"),
        Equipo("Dallas Mavericks", "Oeste"),
        Equipo("Denver Nuggets", "Oeste"),
        Equipo("Golden State Warriors", "Oeste"),
        Equipo("Indiana Pacers", "Este"),
        Equipo("Los Angeles Lakers", "Oeste"),
        Equipo("Miami Heat", "Este"),
        Equipo("New York Knicks", "Este")
    ]

    # Instanciamos el AVL e insertamos
    avl = AVL()
    for eq in datos_nba:
        avl.insertar(eq, clave=lambda x: x.nombre.lower())

    print(f"Altura final del AVL: {avl.altura()}")
    print(f"Cantidad total de nodos: {len(avl)}")
    print()

    print("--- Recorrido Inorder (Ordenado Alfabéticamente) ---")
    for eq in avl.inorder():
        print(f"  {eq}")
    print()

    print("--- Recorrido Preorder (Muestra la estructura balanceada) ---")
    for eq in avl.preorder():
        print(f"  {eq.nombre}")
    print()

    print("=== 2. PRUEBAS DE BÚSQUEDA EN EL AVL ===")
    print("Buscar 'Miami Heat':", avl.buscar("miami heat", clave=lambda x: x.nombre.lower()))
    print("Buscar 'ZZZ':", avl.buscar("zzz", clave=lambda x: x.nombre.lower()))
    print()

    print("=== 3. COMPARACIÓN REAL: BST vs AVL ===")
    # Llamamos a la función de la cátedra para obtener métricas reales de altura y tiempos
    metricas = comparar_bst_vs_avl(datos_nba, clave=lambda x: x.nombre.lower())
    
    if "error" in metricas:
        print("Error en comparación:", metricas["error"])
    else:
        print(f"Altura resultante en BST común: {metricas['altura_bst']}")
        print(f"Altura resultante en Árbol AVL : {metricas['altura_avl']}")
        print(f"Tiempo de búsqueda en BST (1000 iteraciones): {metricas['tiempo_bst_ms']:.4f} ms")
        print(f"Tiempo de búsqueda en AVL (1000 iteraciones): {metricas['tiempo_avl_ms']:.4f} ms")

if __name__ == "__main__":
    main()
    