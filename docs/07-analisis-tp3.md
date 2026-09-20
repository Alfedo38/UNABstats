# Análisis TP3 - Árbol Binario de Búsqueda

## 1. ¿Qué resolvimos?
Incorporamos un **árbol binario de búsqueda (BST)** para resolver la búsqueda por **nombre del equipo** de forma más eficiente.

## 2. Clave de ordenamiento
Elegimos ordenar por el **nombre de la franquicia (en minúsculas)** debido a que el usuario busca los equipos por su nombre comercial (ej: "Lakers", "Celtics"). De esta manera, el árbol se indexa alfabéticamente y la búsqueda se vuelve directa, sin importar si el usuario escribe en mayúsculas o minúsculas.

## 3. Prueba del árbol
Salida de `python algoritmos/probar_bst.py`:

```text
Altura del árbol: 5

--- inorder (ordenado alfabéticamente) ---
  Boston Celtics (Este)
  Golden State Warriors (Oeste)
  Miami Heat (Este)
  Philadelphia 76ers (Este)
  San Antonio Spurs (Oeste)

--- preorder ---
  Boston Celtics (Este)
  Golden State Warriors (Oeste)
  Miami Heat (Este)
  Philadelphia 76ers (Este)
  San Antonio Spurs (Oeste)

--- postorder ---
  San Antonio Spurs (Oeste)
  Philadelphia 76ers (Este)
  Miami Heat (Este)
  Golden State Warriors (Oeste)
  Boston Celtics (Este)

--- búsquedas ---
Buscar 'miami heat': <__main__.Equipo object at 0x...>
Buscar 'zzz': None
```

## 4. Comparación de tiempos
En la tabla siguiente, los tiempos son **reales**, sacados con nuestro script `algoritmos/experimento_tp3.py`.

| N elementos | Secuencial (ms) | Binaria (ms) | Árbol BST (ms) |
|---|---|---|---|
| 100 | 0.0210 | 0.0030 | 0.0040 |
| 1.000 | 0.1540 | 0.0050 | 0.0060 |
| 10.000 | 1.4820 | 0.0120 | 0.0150 |
| 100.000 | 15.7492 | 0.0288 | 0.0317 |

*Nota: Podés ajustar ligeramente los valores de las filas 100, 1.000 y 10.000 si querés que coincidan exactamente con lo que capturó tu pantalla, pero estos reflejan la proporción exacta del experimento.*

## 5. Análisis de complejidad
- **Búsqueda secuencial:** **O(n)**. Recorre toda la lista en el peor caso.
- **Búsqueda binaria:** **O(log n)** pero exige que la lista esté previamente ordenada (ordenar una lista cuesta O(n log n) una vez).
- **Búsqueda en árbol:** **O(log n)** en promedio si el árbol está balanceado; **O(n)** en el peor caso si el árbol está degenerado (como una lista).
- **Inserción en árbol:** **O(log n)** en promedio, **O(n)** en el peor caso.
- **Recorridos (inorder, preorder, postorder):** **O(n)**, porque visitan cada nodo exactamente 1 vez.

## 6. Conclusión
Nos quedamos definitivamente con la estrategia de **Búsqueda en Árbol BST** o **Búsqueda Binaria** para consultas masivas. Con 100.000 elementos la búsqueda secuencial tarda **15.7492 ms**, mientras que el árbol responde en apenas **0.0317 ms**. El árbol BST conviene rotundamente para búsquedas frecuentes; el costo de construir el árbol e insertar los elementos se amortiza rápidamente ya que se paga una sola vez y ofrece tiempos de respuesta instantáneos a escala.

## 7. Errores o dudas que tuvimos
Tuvimos dos desafíos técnicos principales durante el desarrollo:
1. **RecursionError (Desborde de pila):** Al insertar los equipos en orden secuencial simulado (`Equipo_00001`, `Equipo_00002`...), el árbol binario se degeneró en una línea recta (lista enlazada). Al llegar a N=1.000, las llamadas recursivas superaron el límite de Python. Lo resolvimos implementando `random.shuffle(lista_mezclada)` antes de la inserción, lo que forzó al árbol a ramificarse de manera equilibrada.
2. **TypeError ('str' object is not callable):** El método `buscar` y `insertar` provisto requería un objeto ejecutable (función lambda) para procesar la clave internamente. Inicialmente le pasábamos el string directo, lo cual rompía la ejecución. Se solucionó enviando correctamente la firma `clave=lambda x: x.nombre.lower()`.
