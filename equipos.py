class Equipo:
    def _init_(self, conferencia, division, partidos_perdidos, partidos_ganados, eficiencia_ofensiva, eficiencia_defensiva, estrella_de_tres_puntos, estrella_de_bloqueos, acceso_a_las_finales, anillos):
        self._conferencia = conferencia
        self._division = division
        self._partidos_perdidos = partidos_perdidos
        self._partidos_ganados = partidos_ganados
        self._eficiencia_ofensiva = eficiencia_ofensiva
        self._eficiencia_defensiva = eficiencia_defensiva
        self._estrella_de_tres_puntos = estrella_de_tres_puntos
        self._estrella_de_bloqueos = estrella_de_bloqueos
        self._acceso_a_las_finales = acceso_a_las_finales
        self._anillos = anillos

    @property
    def conferencia(self):
        return self._conferencia

    @property
    def division(self):
        return self._division

    @property
    def partidos_ganados(self):
        return self._partidos_ganados

    @property
    def partidos_perdidos(self):
        return self._partidos_perdidos

    @property
    def eficiencia_ofensiva(self):
        return self._eficiencia_ofensiva

    @property
    def eficiencia_defensiva(self):
        return self._eficiencia_defensiva

    @property
    def estrella_de_tres_puntos(self):
        return self._estrella_de_tres_puntos

    @property
    def estrella_de_bloqueos(self):
        return self._estrella_de_bloqueos

    @property
    def acceso_a_las_finales(self):
        return self._acceso_a_las_finales

    @property
    def anillos(self):
        return self._anillos

    def _repr_(self):
        return f"{self._conferencia} {self._division} {self._partidos_ganados} {self._partidos_perdidos} {self._eficiencia_ofensiva} {self._eficiencia_defensiva} {self._estrella_de_tres_puntos} {self._estrella_de_bloqueos} {self._acceso_a_las_finales} {self._anillos}"
    