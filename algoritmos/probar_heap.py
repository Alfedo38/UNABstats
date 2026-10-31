from estructuras.cola_prioridad import MaxHeapNBA

class EquipoNBA:
    def __init__(self, nombre, rating):
        self.nombre = nombre
        self.rating = rating  # Función de prioridad

    def __repr__(self):
        return f"{self.nombre} (Rating: {self.rating})"

def main():
    print("=== TP6: RANKING DINÁMICO CON COLA DE PRIORIDAD (HEAP) ===")
    
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
    
    heap = MaxHeapNBA()
    for eq in equipos:
        heap.insertar(eq, prioridad=eq.rating)
        
    print("\n--- TOP 5 RECOMENDACIONES DE EQUIPOS ---")
    top_5 = heap.obtain_top_n(5) if hasattr(heap, 'obtain_top_n') else heap.obtener_top_n(5)
    for i, eq in enumerate(top_5, 1):
        print(f"{i}. {eq}")

if __name__ == "__main__":
    main()