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
    """Recorre la lista uno por uno. Complejidad O(N)."""
    for e in lista:
        if e.nombre.lower() == target.lower():
            return e
    return None

# --- ESTRATEGIA 2: Búsqueda Binaria ---
def busqueda_binaria(lista_ordenada, target):
    """Busca dividiendo por mitades. Requiere lista ordenada. Complejidad O(log N)."""
    izq = 0
    der = len(lista_ordenada) - 1
    target_lower = target.lower()
    
    while izq <= der:
        medio = (izq + der) // 2
        actual = lista_ordenada[medio].nombre.lower()
        if actual == target_lower:
            return lista_ordenada[medio]
        elif actual < target_lower:
            izq = medio + 1
        else:
            der = medio - 1
    return None

# --- ESTRATEGIA 3: Árbol BST ---
def registrar_en_arbol(lista):
    """Construye el árbol mezclando los elementos para evitar recursión infinita."""
    arbol = ArbolBST()
    lista_mezclada = lista.copy()
    random.shuffle(lista_mezclada)
    
    for e in lista_mezclada:
        arbol.insertar(e, clave=lambda x: x.nombre.lower())
    return arbol

def main():
    # Tamaños de entrada requeridos para evaluar el rendimiento
    tamanos = [1000, 10000, 100000]
    
    print(f"{'N elementos':<12} | {'Secuencial (ms)':<18} | {'Binaria (ms)':<15} | {'Árbol BST (ms)':<15}")
    print("-" * 70)
    
    for N in tamanos:
        # Generamos los N equipos simulados
        equipos = [Equipo(f"Equipo_{str(i).zfill(6)}") for i in range(N)]
        
        # Peor escenario posible (elemento inexistente) para medir el máximo tiempo
        target = "Equipo_Inexistente"
        
        # 1. Medición Búsqueda Secuencial
        inicio = time.time()
        busqueda_secuencial(equipos, target)
        t_secuencial = (time.time() - inicio) * 1000
        
        # 2. Medición Búsqueda Binaria (Primero ordenamos, pero solo medimos la búsqueda)
        equipos_ordenados = sorted(equipos, key=lambda e: e.nombre.lower())
        inicio = time.time()
        busqueda_binaria(equipos_ordenados, target)
        t_binaria = (time.time() - inicio) * 1000
        
        # 3. Medición Búsqueda en Árbol BST
        arbol = registrar_en_arbol(equipos)
        inicio = time.time()
        arbol.buscar(target.lower(), clave=lambda x: x.nombre.lower())
        t_arbol = (time.time() - inicio) * 1000
        
        # Imprimimos la fila con las tres mediciones
        print(f"{N:<12,} | {t_secuencial:<18.4f} | {t_binaria:<15.4f} | {t_arbol:<15.4f}")

if __name__ == "__main__":
    main()
    