import csv
from estructuras.cola_prioridad import MaxHeapNBA


def ver_top_rebotes():

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

        
            jugadores[id_jugador]["partidos"].append({
                "fecha": fila["Fecha"],
                "rebotes": float(fila["Rebotes"])
            })

    
    heap = MaxHeapNBA()

    for jugador in jugadores.values():

        
        if len(jugador["partidos"]) < 5:
            continue

        partidos_ordenados = sorted(
            jugador["partidos"],
            key=lambda partido: partido["fecha"],
            reverse=True
        )

        ultimos_5 = partidos_ordenados[:5]

   
        total_rebotes = sum(
            partido["rebotes"] for partido in ultimos_5
        )

        promedio = total_rebotes / 5

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

    print("\nTOP 5 — PROMEDIO DE REBOTES EN SUS ÚLTIMOS 5 PARTIDOS")

    for puesto, jugador in enumerate(top_5, 1):
        print(
            f"{puesto}. {jugador['nombre']} — "
            f"{jugador['promedio']:.2f} rebotes por partido (L5)"
        )

    input("\nPresioná [Enter] para volver...")