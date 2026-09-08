### 🏀 Sistema de Recomendación de Básquetbol

Este proyecto es una aplicación de consola en Python diseñada para conectar a los usuarios con su equipo o jugador ideal en el mundo del básquetbol. 

### 🏗️ Arquitectura y Componentes (Clases del Dominio)

El proyecto está estructurado bajo el paradigma de **Programación Orientada a Objetos (POO)** y se divide en las siguientes clases principales: 

* **Equipo**: Representa a los clubes deportivos. Contiene atributos privados como el nombre, la conferencia, su estilo de juego principal (ofensivo o defensivo), etc.
* **Jugador**: Representa a los atletas. Contiene atributos privados como el nombre, la posición en la cancha (base, alero, pívot), la altura y sus promedios estadísticos.
* **Usuario**: Representa el perfil de la persona que interactúa con el sistema. Almacena sus respuestas, filtros seleccionados y el tipo de perfil deportivo que está buscando.

### 🔒 Encapsulamiento

Para proteger los datos y evitar modificaciones externas por error, todos los atributos de estas clases utilizan la convención de guion bajo (_atributo). El acceso para lectura desde otros módulos se realiza estrictamente a través de métodos **Getters** (@property). 

### 🤖 Sistema de Recomendación (Operación de Filtrado)

El núcleo lógico del proyecto es su motor de recomendaciones, el cual procesa la información de la siguiente manera: 

1. **Captura de Preferencias**: El sistema solicita al Usuario que defina qué características busca (por ejemplo: un estilo de juego rápido, una posición específica en la cancha o una conferencia en particular).
2. **Cruce de Datos (Algoritmo de Filtrado)**: El programa recorre las listas de objetos Equipo y Jugador previamente cargadas.
3. **Evaluación de Atributos**: Compara los atributos internos de cada equipo o jugador con los deseos del usuario.
4. **Despliegue de Resultados**: Descarta las opciones que no coinciden y muestra en la terminal únicamente las recomendaciones personalizadas que mejor se adaptan al perfil del usuario.