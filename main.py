import json
from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral
from menu import menu_principal

# from estructuras.arbol_binario import ArbolBST ----> modificado (se debe usar AVL y general)

def cargar_categorias():
    """Genera la jerarquía de la NBA para el árbol general."""
    arbol_cat = ArbolGeneral()
    raiz = arbol_cat.insertar_raiz("NBA")

    este = arbol_cat.agregar_hijo(raiz, "Conferencia Este")
    oeste = arbol_cat.agregar_hijo(raiz, "Conferencia Oeste")

    arbol_cat.agregar_hijo(este, "Atlantico")
    arbol_cat.agregar_hijo(este, "Central")
    arbol_cat.agregar_hijo(este, "Sudeste")

    arbol_cat.agregar_hijo(oeste, "Noroeste")
    arbol_cat.agregar_hijo(oeste, "Pacifico")
    arbol_cat.agregar_hijo(oeste, "Sudoeste")
    return arbol_cat

def main():
    # 1. Cargar datos del JSON en el arbol AVL
    with open("datos/equipos.json", "r", encoding="utf-8") as archivo:
        lista_de_elementos = json.load(archivo)

    # arbol = ArbolBST() ----> (no se trabaja con BST)
    arbol_equipos = AVL()
    for elemento in lista_de_elementos:
        arbol_equipos.insertar(elemento, clave=lambda e: e['nombre'].lower())  # se agrega arbol_equipos (antes era arbol)

    # 2. Iniciar el arbol de categorias
    arbol_categorias = cargar_categorias()

    # 3. Lanzar el menú pasándole ambas estructuras
    menu_principal(arbol_equipos, arbol_categorias)   

"""def main():
    menu_principal(arbol)""" # ----> modificado

if __name__ == "__main__":
    main()
