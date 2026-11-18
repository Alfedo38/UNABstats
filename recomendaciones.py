import csv
from estructuras.cola_prioridad import MaxHeapNBA


def obtener_recomendaciones():

    # Cada opción relaciona un texto con una columna del CSV.
    opciones = {
        "1": ("Puntos", "Puntos"),
        "2": ("Rebotes", "Rebotes"),
        "3": ("Asistencias", "Asistencias"),
        "4": ("Triples convertidos", "3PA"),
        "5": ("Tiros de campo intentados", "TCI"),
        "6": ("Triples intentados", "3PI")
    }

    print("\n¿EN QUÉ ESTADÍSTICA BUSCÁS UN JUGADOR?")

    # Mostramos las opciones usando sus descripciones.
    for numero, datos in opciones.items():
        print(f"{numero}. {datos[0]}")

    print("0. Volver")

    opcion = input("\nSeleccioná una opción: ").strip()

    if opcion == "0":
        return

    if opcion not in opciones:
        print("Opción inválida.")
        return

    # Recuperamos el texto y la columna de la opción elegida.
    titulo, columna = opciones[opcion]

    # Cantidad de partidos para calcular el promedio.
    cantidad_partidos = 5

    jugadores = {}

    with open("NBA.csv", "r", encoding="utf-8", newline="") as archivo:

        filas = csv.DictReader(archivo)

        for fila in filas:

            id_jugador = fila["Jugador_ID"]

            if id_jugador not in jugadores:
                jugadores[id_jugador] = {
                    "nombre": fila["Jugador"],
                    "partidos": []
                }

            # Leemos la columna elegida, no una estadística fija.
            jugadores[id_jugador]["partidos"].append({
                "fecha": fila["Fecha"],
                "valor": float(fila[columna])
            })

    heap = MaxHeapNBA()

    for jugador in jugadores.values():

        # Exigimos una muestra completa de cinco partidos.
        if len(jugador["partidos"]) < cantidad_partidos:
            continue

        # Ordenamos por fecha: primero los más recientes.
        partidos_ordenados = sorted(
            jugador["partidos"],
            key=lambda partido: partido["fecha"],
            reverse=True
        )

        ultimos = partidos_ordenados[:cantidad_partidos]

        total = sum(partido["valor"] for partido in ultimos)

        promedio = total / cantidad_partidos

        # El promedio determina la prioridad del jugador.
        heap.insertar(
            {
                "nombre": jugador["nombre"],
                "promedio": promedio
            },
            prioridad=promedio
        )

    recomendaciones = heap.obtener_top_n(5)

    print(f"\nRECOMENDACIONES POR {titulo.upper()} — L5")

    if not recomendaciones:
        print("No hay jugadores con suficientes partidos.")

    for puesto, jugador in enumerate(recomendaciones, 1):
        print(
            f"{puesto}. {jugador['nombre']} — "
            f"{jugador['promedio']:.2f} por partido"
        )

    input("\nPresioná [Enter] para volver...")