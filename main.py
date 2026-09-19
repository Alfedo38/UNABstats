import json
from estructuras.arbol_binario import ArbolBST

with open("datos/equipos.json", "r", encoding="utf-8) as archivo:
          lista_de_elementos = json.load(archivo)

arbol = arbolBST()
for elemento in lista_de_elementos:
    arbol.insertar(elemento, clave=lambda e: e['nombre'].lower())

from menu import menu_principal


def main():
    menu_principal(arbol)

if __name__ == "__main__":
    main()
