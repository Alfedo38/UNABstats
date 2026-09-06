import csv
from datetime import datetime


def buscar_equipo():

    # Leer los equipos del CSV
    with open("NBA.csv", "r", encoding="utf-8") as archivo:

        equipos = csv.DictReader(archivo)

        lista_equipos = []

        for equipo in equipos:

            if equipo["Equipo"] not in lista_equipos:
                lista_equipos.append(equipo["Equipo"])

    # Mostrar menú de equipos
    print("\n========================================")
    print("          SELECCIONAR EQUIPO")
    print("========================================")

    for i, equipo in enumerate(lista_equipos, 1):
        print(f"{i}. {equipo}")

    print("0. Volver")

    opcion = int(input("\nSeleccioná un equipo: "))

    if opcion == 0:
        return

    if opcion < 1 or opcion > len(lista_equipos):
        print("Opción inválida.")
        return

    # Obtener el equipo seleccionado
    equipo_seleccionado = lista_equipos[opcion - 1]

    print("\n========================================")
    print(f"          {equipo_seleccionado}")
    print("========================================")

    # Buscar jugadores del equipo
    with open("NBA.csv", "r", encoding="utf-8") as archivo:

        jugadores = csv.DictReader(archivo)

        lista_jugadores = []

        for jugador in jugadores:

            if jugador["Equipo"] == equipo_seleccionado:

                if jugador["Jugador"] not in lista_jugadores:
                    lista_jugadores.append(jugador["Jugador"])

    # Mostrar jugadores
    for i, jugador in enumerate(lista_jugadores, 1):
        print(f"{i}. {jugador}")

    print("0. Volver")

    opcion_jugador = int(input("\nSeleccioná un jugador: "))

    if opcion_jugador == 0:
        return

    if opcion_jugador < 1 or opcion_jugador > len(lista_jugadores):
        print("Opción inválida.")
        return

    # Obtener jugador seleccionado
    jugador_seleccionado = lista_jugadores[opcion_jugador - 1]

    print("\n========================================")
    print(f"          {jugador_seleccionado}")
    print("========================================")

    # Buscar todos los partidos del jugador
    with open("NBA.csv", "r", encoding="utf-8") as archivo:

        partidos = csv.DictReader(archivo)

        partidos_jugador = []

        for partido in partidos:

            if partido["Jugador"] == jugador_seleccionado:
                partidos_jugador.append(partido)

    # Ordenar por fecha: del más reciente al más antiguo
    partidos_jugador.sort(
        key=lambda partido: datetime.strptime(
            partido["Fecha"],
            "%Y-%m-%d"
        ),
        reverse=True
    )

    # Tomar los 5 más recientes
    ultimos_5 = partidos_jugador[:5]

    print("\nÚltimos 5 partidos:\n")

    for partido in ultimos_5:

        print(
            f"Fecha: {partido['Fecha']} | "
            f"Puntos: {partido['Puntos']} | "
            f"Asistencias: {partido['Asistencias']} | "
            f"Rebotes: {partido['Rebotes']}"
        )