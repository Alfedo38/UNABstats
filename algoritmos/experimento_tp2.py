import time
import random
from estructuras.arbol_binario import ArbolBST

# Definición de la clase del dominio (NBA)
class Equipo:
    def __init__(self, nombre, conferencia="Este"):
        self.nombre = nombre
        self.conferencia = conferencia

# --- ESTRATEGIA 1: Búsqueda Secuencial ---
def busqueda_secuencial(lista, target):
    """Recorre la lista elemento por elemento. Complejidad O(N)."""
    for e in lista:
        if e.nombre.lower() == target.lower():
            return e
    return None

# --- ESTRATEGIA 2: Búsqueda en Árbol BST ---
def registrar_en_arbol(lista):
    """Construye el árbol mezclando los elementos para evitar recursion infinita."""
    arbol = ArbolBST()

    # Creamos una copia de la lista y la mezclamos al azar
    lista_mezclada = lista.copy()
    random.shuffle(lista_mezclada)

    for e in lista_mezclada:
        #insertamos pasando el equipo y su clave en minusculas. Pasamos el lambda ejecutable que espera el archivo arbol_binario.py
        arbol.insertar(e, clave=lambda x : x.nombre.lower())
    return arbol

def main():
    # Tamaños de entrada solicitados (1.000, 10.000, 100.000)
    tamanos = [1000, 10000, 100000]
    
    print(f"{'N elementos':<15} | {'Búsqueda secuencial (ms)':<25} | {'Búsqueda en árbol (ms)':<25}")
    print("-" * 72)
    
    for N in tamanos:
        # Generamos N equipos simulados (ej: Equipo_00001, Equipo_00002...)
        equipos = [Equipo(f"Equipo_{str(i).zfill(6)}") for i in range(N)]
        
        # Buscamos un elemento que NO existe para simular el peor escenario posible (Worst Case)
        target = "Equipo_Inexistente"
        
        # --- Medición Estrategia 1: Secuencial ---
        inicio = time.time()
        busqueda_secuencial(equipos, target)
        t_secuencial = (time.time() - inicio) * 1000 # Convertimos a milisegundos
        
        # --- Medición Estrategia 2: Árbol BST ---
        # Primero armamos el árbol (la estructura debe estar creada)
        arbol = registrar_en_arbol(equipos)
        
        # Medimos ESTRICTAMENTE el tiempo que tarda la operación crítica de buscar
        inicio = time.time()
        arbol.buscar(target.lower(), clave=lambda x: x.nombre.lower())
        t_arbol = (time.time() - inicio) * 1000
        
        # Imprimimos la fila con formato prolijo
        print(f"{N:<15,} | {t_secuencial:<25.4f} | {t_arbol:<25.4f}")

if __name__ == "__main__":
    main()
