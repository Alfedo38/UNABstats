class GrafoNBA:
    def __init__(self):
        # Representación mediante Lista de Adyacencia
        self.adyacencia = {}

    def agregar_equipo(self, equipo):
        if equipo not in self.adyacencia:
            self.adyacencia[equipo] = []

    def agregar_rivalidad(self, eq1, eq2, partidos_jugados=1):
        self.agregar_equipo(eq1)
        self.agregar_equipo(eq2)
        # Es un grafo no dirigido (rivalidad mutua)
        if eq2 not in [rival for rival, _ in self.adyacencia[eq1]]:
            self.adyacencia[eq1].append((eq2, partidos_jugados))
        if eq1 not in [rival for rival, _ in self.adyacencia[eq2]]:
            self.adyacencia[eq2].append((eq1, partidos_jugados))

    def mostrar_red(self):
        for equipo, rivales in self.adyacencia.items():
            lista_rivales = ", ".join([f"{riv} ({pj} PJ)" for riv, pj in rivales])
            print(f"🏀 {equipo} está conectado con: [{lista_rivales}]")