from estructuras.arbol_binario import ArbolBST

class Equipo:
    def __init__(self, nombre, conferencia, division, partidos_ganados, partidos_perdidos, eficiencia_ofensiva, eficiencia_defensiva, estrella_de_tres_puntos, estrella_de_bloqueos, finales_alcanzadas, anillos):
        self.nombre = nombre
        self.conferencia = conferencia
        self.division = division
        self.partidos_ganados = partidos_ganados
        self.partidos_perdidos = partidos_perdidos
        self.eficiencia_ofensiva = eficiencia_ofensiva
        self.eficiencia_defensiva = eficiencia_defensiva
        self.estrella_de_tres_puntos = estrella_de_tres_puntos
        self.estrella_de_bloqueos = estrella_de_bloqueos
        self.finales_alcanzadas = finales_alcanzadas
        self.anillos = anillos

def __repr__(self):
    return f"{self.nombre} (Conferencia: {self.conferencia}, Division: {self.division}, Partidos_ganados: {self.partidos_ganados}, Partidos_perdidos: {self.partidos_perdidos}, Eficiencia_ofensiva: {self.eficiencia_ofensiva}, Eficiencia_defensiva: {self.eficiencia_defensiva}, Estrella_de_tres_puntos: {self.estrella_de_tres_puntos}, Estrella_de_bloqueos: {self.estrella_de_bloqueos}, Finales_alcanzadas: {self.finales_alcanzadas}, Anillos: {self.anillos})"

def main():
    arbol = ArbolBST()

# Lo construimos SIN orden, para que el árbol ordene solo
    datos = [
        Equipo("Boston Celtics", "Este", "Atlantico", 62, 20, 120.8, 112.7, 2, 1, 23, 18),
        Equipo("Golden State Warriors", "Oeste", "Pacifico", 46, 36, 117.2, 115.1, 1, 0, 12, 7),
        Equipo("Miami Heat", "Este", "Sureste", 46, 36, 114.0, 113.8, 1, 1, 7, 3),
        Equipo("Philadelphia 76ers", "Este", "Atlantico", 47, 35, 116.8, 114.5, 1, 1, 9, 3),
        Equipo("San Antonio Spurs", "Oeste", "Soroeste", 41, 41, 119.6, 111.3, 0, 1, 6, 5),
]

# Insertamos ordenando por el atributo .nombre en minúsculas
    for d in datos:
        arbol.insertar(d, clave=lambda e: e.nombre.lower())

    print("Altura del árbol:", arbol.altura())

    print("\n--- inorder (ordenado alfabéticamente) ---")
    for e in arbol.inorder():
        print(" ", e.nombre)

    print("\n--- preorder ---")
    for e in arbol.preorder():
        print(" ", e.nombre)

    print("\n--- postorder ---")
    for e in arbol.postorder():
        print(" ", e.nombre)

    print("\n--- búsquedas ---")
# Probamos buscar un equipo que existe (en minusculas)
    encontrado = arbol.buscar("miami heat", clave=lambda e: e.nombre.lower())
    print("Buscar 'miami heat':", encontrado)

# Probamos buscar un equipo que NO exite
    no_encontrado = arbol.buscar("zzz", clave=lambda e: e.nombre.lower())
    print("Buscar 'zzz':", no_encontrado)

if __name__ == "__main__":
    main()
