# TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA

## 🧪 Práctica Evaluativa – Recuperatorio Parcial I

### Asignatura: Programación I

### Tema: Estructuras Repetitivas con Listas

---

## 🧩 Desafío

Una empresa necesita gestionar su stock de productos de forma sencilla. Para ello, se desea desarrollar un programa que permita:

1. Ingresar una lista con los nombres de los productos disponibles.
2. Ingresar una lista con las cantidades correspondientes a cada producto.
3. Mostrar un listado con el stock disponible.
4. Permitir al usuario consultar el stock de un producto específico.
5. Informar cuáles productos tienen stock agotado (cantidad igual a cero).

---

## ⚙️ Requisitos Técnicos

- Utilizar exclusivamente estructuras repetitivas (`for`, `while`), estructuras condicionales (`if`, `elif`, `else`) y listas.
- No se permite el uso de diccionarios ni estructuras avanzadas.

### Sugerencias

- Utilizar dos listas paralelas: una para los nombres de productos y otra para las cantidades.
- Para consultar el stock de un producto, buscar su índice en la lista de nombres y utilizar ese índice en la lista de cantidades.
- Si un producto está agotado (es decir, no tiene stock), debe mantenerse en ambas listas, asignando el valor 0 en su posición correspondiente dentro de la lista de cantidades.

---

## 🛒 Menú del Programa

### 🛒 Menú de Opciones:

1. Agregar producto
2. Ver productos agotados
3. Actualizar stock
4. Ver todos los productos
5. Salir

---

## Cómo Ejecutar el Programa

1. Asegúrate de tener Python instalado en tu sistema.
2. Descarga el archivo `RecuperatorioParcial1.py`.
3. Abre una terminal y navega hasta el directorio donde se encuentra el archivo.
4. Ejecuta el programa con el siguiente comando:

   ```bash
   python RecuperatorioParcial1.py

5. Sigue las instrucciones en pantalla para gestionar el stock de productos.