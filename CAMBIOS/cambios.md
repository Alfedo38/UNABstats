# 🛠️ Reporte de Cambios: Integración de Árbol de Búsqueda Binaria (BST)

Este documento detalla las modificaciones realizadas en la estructura del proyecto *UNAbStats* para reemplazar la búsqueda lineal por una estructura de datos optimizada basada en un Árbol Binario de Búsqueda (BST).

---

## 1. Cambios Realizados por Archivo

### 📄 main.py
* Se importó la clase ArbolBST desde el módulo estructuras.arbol_binario.
* Se implementó la lectura del archivo de datos externo datos/equipos.json empleando el módulo json con codificación utf-8 para prevenir errores de caracteres.
* Se modificó la llamada a la función menu_principal(arbol) para enviarle la estructura de datos ya cargada en memoria.

### 📄 menu.py
* Se adaptó la función del menú principal para que reciba el objeto arbol como parámetro.
* Se creó la función buscar_equipo(arbol). Se reemplazó el antiguo algoritmo de búsqueda lineal (bucle for sobre una lista) por el método altamente eficiente arbol.buscar().
* Se integró el método .lower() tanto al registrar los nombres en el árbol como al capturar la entrada del usuario (input), garantizando que las búsquedas funcionen sin importar el uso de mayúsculas o minúsculas.

---

## 2. Justificación Técnica del Análisis

### ¿Por qué elegimos ordenar el árbol por el atributo "nombre"?
Decidimos utilizar el campo *nombre* como la clave (key) del árbol binario debido a que *es el criterio natural y principal bajo el cual el usuario final interactúa con la aplicación* al momento de consultar estadísticas. El usuario busca un equipo ingresando textualmente su nombre (ej: "Boston Celtics"), por lo que indexar la estructura bajo este atributo optimiza de forma directa su experiencia de uso.

