from estructuras.arbol_general import ArbolGeneral

def main():
    print("=== TP5: PRUEBA DEL ÁRBOL GENERAL (Jerarquía NBA) ===")
    
    # 1. Instanciamos el árbol e insertamos la raíz principal
    arbol = ArbolGeneral()
    raiz = arbol.insertar_raiz("NBA")
    
    # 2. Agregamos las Conferencias (Nivel 1)
    este = arbol.agregar_hijo(raiz, "Conferencia Este")
    oeste = arbol.agregar_hijo(raiz, "Conferencia Oeste")
    
    # 3. Agregamos las Divisiones de la Conferencia Este (Nivel 2)
    arbol.agregar_hijo(este, "Atlántico")
    arbol.agregar_hijo(este, "Central")
    arbol.agregar_hijo(este, "Sudeste")
    
    # 4. Agregamos las Divisiones de la Conferencia Oeste (Nivel 2)
    arbol.agregar_hijo(oeste, "Noroeste")
    arbol.agregar_hijo(oeste, "Pacífico")
    arbol.agregar_hijo(oeste, "Sudoeste")
    
    # --- Impresión de Métricas de la Estructura ---
    print(f"Raíz del árbol: {arbol.raiz.dato}")
    print(f"Altura del árbol jerárquico: {arbol.altura()}")
    print(f"Cantidad total de nodos (Categorías): {arbol.cantidad_nodos()}")
    print()
    
    # --- Pruebas de Recorridos Exigidos por la Cátedra ---
    print("--- Recorrido en Amplitud (BFS - Nivel por Nivel) ---")
    print(arbol.amplitud())
    print()
    
    print("--- Recorrido en Profundidad Preorder (DFS) ---")
    print(arbol.profundidad_preorder())
    print()
    
    print("--- Recorrido en Profundidad Postorder (DFS) ---")
    print(arbol.profundidad_postorder())
    print()
    
    # --- Pruebas de Búsqueda jerárquica ---
    print("--- Pruebas de Búsqueda de Categorías ---")
    nodo_central = arbol.buscar("Central")
    print(f"Buscar división 'Central': {nodo_central}")
    
    nodo_inexistente = arbol.buscar("División Inexistente")
    print(f"Buscar categoría falsa: {nodo_inexistente}")
    print()
    
    # --- Visualización por niveles ---
    print("--- Estructura Organizativa por Niveles ---")
    for i, nivel in enumerate(arbol.obtener_niveles()):
        print(f"  Nivel {i}: {nivel}")

if __name__ == "__main__":
    main()
    