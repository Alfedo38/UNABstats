# Resumen del Proyecto: UNABstats (Dominio NBA)

El sistema **UNABstats** fue desarrollado de manera progresiva utilizando distintas estructuras de datos para optimizar la gestión, la búsqueda, la jerarquización y el análisis entre equipos y jugadores de la NBA:

## 1. Búsqueda y Análisis (TP2 y TP3)
* **Implementación:** Comparamos tres estrategias de búsqueda por nombre de equipo:
  * Búsqueda Secuencial $O(n)$
  * Búsqueda Binaria $O(\log n)$
  * Árbol Binario de Búsqueda (BST) $O(\log n)$
* **Resultados:** En pruebas con 100.000 registros (`algoritmos/experimento_tp3.py`), la búsqueda secuencial tardó aproximadamente **15,75 ms**, mientras que el árbol BST lo hizo en aprox. **0,03 ms**, demostrando la eficiencia logarítmica.
* **Documentación:** `docs/07-analisis-tp3.md`

## 2. Balanceo Automático con Árbol AVL (TP4)
* **Implementación:** Reemplazamos el BST común por un **Árbol AVL** (`estructuras/avl.py`) en la opción de búsqueda de equipos del menú principal.
* **Resultados:** Durante la carga de datos con orden alfabético (en el peor de los casos para un BST), el árbol BST se desbalanceó alcanzando **altura 10**, en tanto que el AVL conservó la simetría con rotaciones automáticas registrando **altura 4** (`algoritmos/probar_avl.py`), garantizando un rendimiento $O(\log n)$.

## 3. Organización por jerarquías usando un Árbol General (TP5)
* **Implementación:** Modelamos la estructura de la liga de la NBA mediante un **Árbol N-ario** (`estructuras/arbol_general.py`) organizándola en tres niveles: `NBA` $\rightarrow$ `Conferencias` $\rightarrow$ `Divisiones`.



* **Integración:** Lo incorporamos al menú interactivo mediante un recorrido de amplitud (**BFS**) para visualizar la estructura por niveles.
* **Documentación:** `docs/08-analisis-tp4-tp5.md`

## 4. Ranking con Cola de Prioridad / Heap (TP6)
* **Implementación:** Utilizamos una estructura **Max-Heap Binaria** (`estructuras/cola_prioridad.py`) mediante un criterio de ordenamiento según el rating o índice de eficiencia por equipo.
* **Resultados:** Permite obtener el **Top-5 de equipos recomendados** en el menú con una complejidad de $O(n \log k)$, evitando el costo de ordenar toda la base de datos $O(n \log n)$ en cada consulta.

## 5. Red de rivalidades con Grafos (TP7)
* **Implementación:** Tuvimos en cuenta las rivalidades y partidos históricos jugados entre equipos para utilizar un **Grafo No Dirigido y Ponderado** mediante una Lista de Adyacencia (`estructuras/grafo_nba.py`), donde los nodos son los equipos y el peso de las aristas representa los partidos disputados entre rivales clásicos.
* **Documentación:** `docs/09-analisis-tp6-tp7.md`

## 6. Fase final: Armado de las opciones restantes del menú principal

### Top-5 Estadísticas de Jugadores
* **Implementación:** Para los Top-5 puntos, Top-5 rebotes y Top-5 asistencias se eligió la estructura **Max-Heap** que permite obtener los jugadores con mayor prioridad y eficiencia.
* **Funcionamiento:** Se leen los datos de `NBA.csv`, se agrupan los partidos de cada jugador según su ID, se ordenan los partidos por fecha y se seleccionan los últimos 5, calculando el promedio de puntos, rebotes y asistencias. Luego se inserta cada jugador en el Heap usando su promedio como prioridad y finalmente muestra los 5 jugadores con mayor promedio.

### Recomendaciones de Jugadores
* **Implementación:** Para la opción de recomendaciones también se eligió como estructura un **Max-Heap** debido a que necesitamos obtener los jugadores con los promedios más altos.
* **Funcionamiento:** Al igual que en las opciones anteriores se agrupan sus partidos y calculamos el promedio de los últimos 5 partidos según la estadística que se desee consultar. Luego se utiliza el promedio como prioridad para obtener las seis recomendaciones.
