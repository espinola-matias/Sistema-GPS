# 🗺️ Sistema GPS de Ciudad - Pathfinding con Python

Este proyecto es una simulación de un sistema de navegación GPS que opera sobre una matriz bidimensional (una ciudad). Utiliza el algoritmo **Breadth-First Search (BFS)** para encontrar la ruta más corta entre un punto de partida y un destino, esquivando edificios y obstáculos naturales.

## 🚀 Características Principales

* **Generación Procedural de Mapas:** La ciudad se genera dinámicamente basada en el tamaño ingresado por el usuario, creando patrones de edificios (🏨) y cuerpos de agua aleatorios (♒).
* **Algoritmo de Búsqueda (BFS):** Implementación de búsqueda en anchura utilizando colas (`deque`) para garantizar el camino más corto posible.
* **Validación de Datos:** Sistema robusto que corrige entradas de usuario (tamaño mínimo de ciudad, coordenadas fuera de rango).
* **Interactividad Dinámica:**
    * Selección de puntos de partida (✅) y llegada (❌).
    * Posibilidad de agregar obstáculos temporales (🧱) en tiempo real para recalcular la ruta.
* **Renderizado en Consola:** Visualización gráfica utilizando emojis para una experiencia de usuario clara.

## 🛠️ Tecnologías y Conceptos Aplicados

* **Lenguaje:** Python 3.x
* **Estructuras de Datos:**
    * Matrices (Listas de listas) para el grid.
    * `collections.deque` para la gestión eficiente de la cola en el algoritmo BFS.
    * Tuplas para el manejo de coordenadas `(x, y)`.
* **Manejo de Errores:** Uso de bloques `try-except` para asegurar la estabilidad del programa ante inputs inválidos.

## 📋 Pre-requisitos

Tener instalado Python 3.6 o superior.

## 🔧 Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/espinola-matias/Sistema-GPS.git](https://github.com/espinola-matias/Sistema-GPS.git)
    ```
2.  **Navegar al directorio:**
    ```bash
    cd Sistema-GPS
    ```
3.  **Ejecutar el programa:**
    ```bash
    python gps.py
    ```

## 🎮 Ejemplo de Funcionamiento

El sistema solicitará el tamaño de la ciudad y las coordenadas.

**Visualización del mapa:**
```text
🏨 ⬜ 🏨 ⬜ 🏨
⬜ ✅ ◾ 🧱 ⬜
🏨 ♒ 🏨 ❌ 🏨
⬜ ⬜ ◾ ◾ ⬜
🏨 ⬜ 🏨 ⬜ 🏨