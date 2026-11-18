import csv
from estructuras.cola_prioridad import MaxHeapNBA


def ver_top_asistencias():

    # Guardaremos los partidos de cada jugador.
    jugadores = {}

    with open("NBA.csv", "r", encoding="utf-8", newline="") as archivo:

        filas = csv.DictReader(archivo)

        for fila in filas:

            id_jugador = fila["Jugador_ID"]

            # Creamos al jugador solamente cuando aparece por primera vez.
            if id_jugador not in jugadores:
                jugadores[id_jugador] = {
                    "nombre": fila["Jugador"],
                    "partidos": []
                }

            # Agregamos cada partido con su fecha y sus rebotes.
            jugadores[id_jugador]["partidos"].append({
                "fecha": fila["Fecha"],
                "asistencias": float(fila["Asistencias"])
            })

    # Esta parte va FUERA del recorrido de filas.
    # Primero necesitamos haber reunido todos los partidos.
    heap = MaxHeapNBA()

    for jugador in jugadores.values():

        # Participan jugadores con al menos cinco partidos registrados.
        if len(jugador["partidos"]) < 5:
            continue

        # Ordenamos desde el partido más reciente al más antiguo.
        partidos_ordenados = sorted(
            jugador["partidos"],
            key=lambda partido: partido["fecha"],
            reverse=True
        )

        # Tomamos únicamente los primeros cinco.
        ultimos_5 = partidos_ordenados[:5]

        # Sumamos los rebotes de esos cinco partidos.
        total_asistencias = sum(
            partido["asistencias"] for partido in ultimos_5
        )

        # Calculamos el promedio L5.
        promedio = total_asistencias / 5

        # Guardamos el resultado y lo usamos como prioridad.
        heap.insertar(
            {
                "nombre": jugador["nombre"],
                "promedio": promedio
            },
            prioridad=promedio
        )

    top_5 = heap.obtener_top_n(5)

    if not top_5:
        print("No hay jugadores con cinco partidos registrados.")
        return

    print("\nTOP 5 — PROMEDIO DE ASISTENCIAS EN SUS ÚLTIMOS 5 PARTIDOS")

    for puesto, jugador in enumerate(top_5, 1):
        print(
            f"{puesto}. {jugador['nombre']} — "
            f"{jugador['promedio']:.2f} asistencias por partido (L5)"
        )

    input("\nPresioná [Enter] para volver...")