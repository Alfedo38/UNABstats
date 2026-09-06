import csv


def buscar_jugador(nombre):

    with open("NBA.csv", "r", encoding="utf-8") as archivo:

        jugadores = csv.DictReader(archivo)

        encontrados = []

        for jugador in jugadores:

            if nombre.lower() in jugador["Jugador"].lower():

                if jugador["Jugador"] not in encontrados:
                    encontrados.append(jugador["Jugador"])

        if len(encontrados) == 0:
            print("No se encontró ningún jugador.")
            return

        print("\nJugadores encontrados:")
        
        for jugador in encontrados:
            print("-", jugador)