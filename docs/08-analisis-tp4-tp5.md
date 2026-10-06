# Análisis TP4 + TP5 — AVL y Árbol General

## 1. ¿Qué resolvimos?
En esta etapa incorporamos dos estructuras de datos avanzadas para resolver problemas específicos dentro del sistema de la NBA:

| Estructura | Problema que resuelve | Dónde se usa |
| :--- | :--- | :--- |
| **Árbol AVL** | Garantiza que las búsquedas por nombre de equipo sean siempre rápidas \(O(\log n)\), incluso si los datos se ingresan en orden alfabético. | Opción 2: "Explorar Equipos (Buscar por AVL)" del menú. |
| **Árbol General** | Representa de forma natural la jerarquía organizativa y corporativa del dominio. | Opción 7: "Explorar Categorías Jerárquicas" del menú. |

---

## 2. TP4 — Árbol AVL

### 2.1 ¿Por qué AVL y no un BST común?
Un BST común se desbalancea por completo si los datos se insertan en orden alfabético ordenado (ej: de la A a la Z). Esto provoca que el árbol degenere en una línea recta (lista enlazada), elevando la complejidad de búsqueda a un ineficiente \(O(n)\). El AVL soluciona esto aplicando rotaciones automáticas que mantienen la altura balanceada en un óptimo \(O(\log n)\) sin importar el orden de inserción.

### 2.2 Rotaciones implementadas
- **Rotación simple derecha (Izquierda-Izquierda):** Factor de balance \(> 1\) y el nuevo dato va a la izquierda del hijo izquierdo.
- **Rotación simple izquierda (Derecha-Derecha):** Factor de balance \(< -1\) y el nuevo dato va a la derecha del hijo derecho.
- **Rotación doble izquierda-derecha (Izquierda-Derecha):** Factor de balance \(> 1\) pero el hijo izquierdo está pesado a la derecha.
- **Rotación doble derecha-izquierda (Derecha-Izquierda):** Factor de balance \(< -1\) pero el hijo derecho está pesado a la izquierda.

### 2.3 Comparación BST vs AVL (Datos Ordenados)
Ingresando 10 equipos de la NBA perfectamente ordenados alfabéticamente (*Atlanta Hawks, Boston Celtics, Chicago Bulls...*), obtuvimos las siguientes métricas reales en nuestro script `probar_avl.py`:

| Métrica | BST común | Árbol AVL |
| :--- | :---: | :---: |
| **Altura con datos ordenados** | 10 | 4 |
| **Complejidad peor caso búsqueda** | \(O(n)\) | \(O(\log n)\) |
| **Complejidad promedio inserción** | \(O(\log n)\) | \(O(\log n)\) |

**Justificación:** Insertar 10 elementos ordenados genera un BST con altura 10 (una cadena recta), mientras que el AVL balancea la estructura de forma inmediata reduciendo la altura máxima a solo 4 niveles. Esta diferencia se vuelve crítica y abismal al escalar a miles de registros.

---

## 3. TP5 — Árbol General (N-ario)

### 3.1 ¿Qué es un árbol general?
A diferencia de un árbol binario donde cada nodo tiene como máximo 2 hijos, un árbol general permite que cada nodo posea una cantidad ilimitada de hijos. Es la estructura ideal para representar clasificaciones taxonómicas o jerarquías naturales.

### 3.2 Jerarquía elegida del dominio (NBA)
Decidimos organizar el dominio de básquetbol según su estructura oficial de Conferencias y Divisiones:

```text
NBA (Raíz)
├── Conferencia Este
│   ├── Atlántico
│   ├── Central
│   └── Sudeste
└── Conferencia Oeste
    ├── Noroeste
    ├── Pacífico
    └── Sudoeste
```

**¿Por qué esta jerarquía?**
- Refleja la organización real de la liga comercial de la NBA.
- El AVL resuelve la búsqueda rápida de un equipo individual por clave, mientras que el Árbol General organiza la navegación estructural de las ligas.

### 3.3 Recorridos implementados
- **Amplitud (BFS):** Nivel por nivel, de arriba hacia abajo. Complejidad \(O(n)\). Se usa en el menú para listar las categorías de manera ordenada.
- **Profundidad Preorder (DFS):** Nodo,  hijos de izquierda a derecha. Complejidad \(O(n)\).
- **Profundidad Postorder (DFS):** Hijos, nodo. Complejidad \(O(n)\).

---

## 4. Análisis de complejidad temporal

| Operación | Árbol AVL | Árbol General |
| :--- | :---: | :---: |
| **Inserción** | \(O(\log n)\) | \(O(1)\) (insertando en un padre conocido) |
| **Búsqueda** | \(O(\log n)\) | \(O(n)\) (recorrido completo por niveles) |
| **Altura (Peor caso)** | \(O(\log n)\) | \(O(n)\) (si degenera en lista) |

- **¿Por qué el AVL es \(O(\log n)\)?** Porque mantiene su factor de balance estrictamente entre -1 y +1, obligando al árbol a ramificarse equitativamente.
- **¿Por qué el Árbol General es \(O(n)\) en búsqueda?** Porque no posee un criterio de ordenamiento interno (no es mayor a la derecha ni menor a la izquierda), por lo que para buscar un elemento es necesario realizar un recorrido completo visitando todos los nodos. Es perfectamente aceptable porque la cantidad de categorías es fija y reducida.

---

## 5. Errores o dudas que tuvimos
1. **ImportError / Archivo Faltante:** La función `comparar_bst_vs_avl` de la cátedra buscaba un archivo base llamado `arboles.py`, pero nuestro código del TP anterior se llamaba `arbol_binario.py`. Tuvimos que corregir la línea interna del import en `estructuras/avl.py` para sincronizar ambas entregas de forma exitosa.
2. **Efecto de Limpieza de Terminal:** Al integrar la opción 7, la pantalla se borraba instantáneamente debido a los comandos de limpieza de consola del menú. Lo solucionamos agregando un `input()` de congelamiento para pausar la terminal y permitir la lectura correcta del recorrido.