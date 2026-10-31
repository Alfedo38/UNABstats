# Análisis TP6 + TP7 — Colas de Prioridad y Grafos

## 1. TP6 — Cola de Prioridad (Heaps)
### 1.1 ¿Por qué un Heap y no ordenar una lista común?
Para obtener el ranking de los mejores $N$ equipos, la estrategia tradicional de ordenar toda la lista mediante algoritmos de ordenación clásicos consume un tiempo de $O(N \log N)$. En cambio, el uso de una Cola de Prioridad basada en una **Heap Binaria** optimiza drásticamente el proceso a un tiempo de $O(N \log K)$, donde $K$ es el tamaño del Top buscado. Si el dataset crece masivamente a miles de registros, la Heap ahorra una inmensidad de ciclos de cómputo al no procesar datos que no entrarán en el ranking.

### 1.2 Complejidad Temporal
- **Inserción (Insert):** $O(\log n)$ por el proceso de flotado (`_flotar`).
- **Extracción del Máximo (Extract-Max):** $O(\log n)$ por el proceso de hundido (`_hundir`).

---

## 2. TP7 — Grafos (Red de Relaciones)
### 2.1 Representación del dominio
Mapeamos el ecosistema de la NBA como un **Grafo No Dirigido y Ponderado**. 
- **Vértices (Nodos):** Representan a las franquicias de la liga (Celtics, Lakers, Heat).
- **Aristas (Enlaces):** Representan las rivalidades históricas de partidos jugados.
- **Pesos:** El valor numérico asignado a la arista equivale a la cantidad de Partidos Jugados (PJ) en etapas críticas de playoffs.

### 2.2 Estructura elegida
Implementamos el grafo mediante una **Lista de Adyacencia** usando un diccionario de Python. Es la opción de ingeniería más eficiente para nuestro dominio ya que es un grafo "disperso" (un equipo no juega contra absolutamente todos los equipos históricos todo el tiempo), minimizando el consumo de memoria a $O(V + A)$.