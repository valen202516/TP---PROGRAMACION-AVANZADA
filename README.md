# Simulador de Eco-Logística Urbana (Delivery Express)

## Trabajo Práctico Integrador - Programación Avanzada 2026

Este proyecto es una aplicación de consola desarrollada en Python que simula la gestión y asignación eficiente de pedidos pendientes a una flota de vehículos ecológicos repartidores (Drones, Bicicletas, etc.). El sistema calcula costos, tiempos de entrega y gestiona recursos basándose en principios sólidos de Diseño Orientado a Objetos.

---

## 👥 Integrantes
Integrante 1: Valentin Prina Cerai - [Legajo/Email]
Integrante 2: Tomas - [Legajo/Email]
---

## 🎯 Objetivos del Proyecto
*   **Abstracción y Herencia:** Creamos una clase base `Vehiculo` (abstracta, como corresponde) de la cual nacen `Dron` y `Bicicleta`. Cada uno hereda la base pero define sus propias limitaciones físicas de peso y velocidad].
*   **Polimorfismo:** El `GestorLogistica` tiene una lista genérica de vehículos. Cuando recorre la lista para calcular los costos con `calcular_costo()`, no le importa qué bicho es en tiempo de ejecución; cada objeto responde a su manera.
*   **Relación entre objetos:** Usamos agregación/composición en el `GestorLogistica` para administrar las colecciones de datos sin que las clases dependan rígidamente entre sí.
---

## 🧠 Conceptos de POO Aplicados
El sistema modela el dominio del problema utilizando los pilares fundamentales de la programación orientada a objetos

Abstracción y Encapsulamiento: La clase abstracta `Vehiculo` define el molde genérico del transporte, ocultando los detalles internos de su velocidad y lógica interna de carga.
Herencia: Clases concretas como `Dron` y `Bicicleta` heredan la estructura base de `Vehiculo` para reutilizar atributos comunes.
Polimorfismo: El método `calcular_costo()` se redefine de manera particular en cada vehículo. El gestor procesa una lista heterogénea de transportes llamando al mismo método sin importar el tipo de objeto en tiempo de ejecución.
Relaciones entre Objetos: Se implementa una relación de **Agregación/Composición** en la clase `GestorLogistica`, la cual administra colecciones independientes de vehículos y pedidos.

---

## 🛠️ Patrón de Diseño Incorporado
Para no terminar tener un codigo con muchos de `if/else` a la hora de cobrar los envíos, incluimos el patrón **Strategy** 
Definimos la interfaz `IEstrategiaTarifa` y creamos tres lógicas distintas: `TarifaEstandar`, `TarifaUrgente` (con recargo) y `TarifaEco` (con descuento). El pedido cambia de tarifa en el aire sin romper nada de su estructura original.

---

## 📦 Elementos Opcionales Incluidos
Para aportar mayor valor técnico a la solución, se incorporaron los siguientes módulos:
Persistencia de datos: Los pedidos y el estado de la simulación se guardan y cargan automáticamente en formato **JSON**
Excepciones Personalizadas: Se definen errores propios (como `CapacidadExcedidaException`) para controlar de forma limpia las asignaciones inválidas.

---
```bash
   git clone [https://github.com/tu-usuario/eco-logistica-tpi.git](https://github.com/tu-usuario/eco-logistica-tpi.git)
   cd eco-logistica-tpi
