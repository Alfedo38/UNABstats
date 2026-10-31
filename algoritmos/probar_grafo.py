from estructuras.grafo_nba import GrafoNBA

def main():
    print("=== TP7: RED DE CONEXIONES Y RIVALIDADES DE LA NBA ===")
    
    red_nba = GrafoNBA()
    
    # Creamos las conexiones clásicas (Aristas con peso = Partidos Jugados)
    red_nba.agregar_rivalidad("Boston Celtics", "Los Angeles Lakers", 12)
    red_nba.agregar_rivalidad("Boston Celtics", "Miami Heat", 8)
    red_nba.agregar_rivalidad("Golden State Warriors", "Los Angeles Lakers", 10)
    red_nba.agregar_rivalidad("San Antonio Spurs", "Los Angeles Lakers", 6)
    
    print("\n--- MAPA DE LA RED DEL DOMINIO ---")
    red_nba.mostrar_red()

if __name__ == "__main__":
    main()