from jugadores import buscar_jugador

def menu_principal ():
    while True:
        print("""
========================================
            UNABSTATS 
========================================

1. Buscar jugador
2. Explorar Equipos
3. Ver Top 5 Puntos
4. Ver Top 5 Asistencias
5. Ver top 5 Rebotes
6. Obtener recomendaciones
0. Salir

----------------------------------------""")
     
     
        opcion = input("Seleccioná una opción: ")

        if opcion == "1":

            nombre = input("Ingrese el nombre del jugador: ")

            buscar_jugador(nombre)

        elif opcion == "2":
            buscar_equipo()

        elif opcion == "3":
            ver_top_puntos()

        elif opcion == "4":
            ver_top_asistencias()

        elif opcion == "5":
            ver_top_rebotes()
        
        elif opcion == "6":
            obtener_recomendaciones()

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida.")