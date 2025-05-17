'''Desafío: Una empresa necesita gestionar su stock de productos de forma sencilla. Para ello,
se desea desarrollar un programa que permita:
1. Ingresar una lista con los nombres de los productos disponibles.
2. Ingresar una lista con las cantidades correspondientes a cada producto.
3. Mostrar un listado con el stock disponible.
4. Permitir al usuario consultar el stock de un producto específico.
5. Informar cuáles productos tienen stock agotado (cantidad igual a cero)'''

# Inicializar listas vacías para nombres y cantidades
nombres = []
cantidades = []

# Variable bandera para controlar el bucle
salir = True

# Bucle principal
while salir:
    print("\n 🛒 Menú de opciones:")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Agregar producto
        nombre = input("Ingrese el nombre del producto: ").lower()
        cantidad = int(input("Ingrese la cantidad en stock: "))
        nombres.append(nombre)
        cantidades.append(cantidad)
        print("Producto agregado con éxito.")

    elif opcion == "2":
        # Ver productos agotados
        print("Productos agotados:")
        productos_encontrados = False
        for i in range(len(nombres)):
            if cantidades[i] == 0:
                print(nombres[i])
                productos_encontrados = True
        if productos_encontrados == False:
            print("No hay productos agotados.")

    elif opcion == "3":
        # Actualizar stock
        producto = input("Ingrese el nombre del producto a actualizar: ").lower()
        if producto in nombres:
            index = nombres.index(producto)
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            cantidades[index] = nueva_cantidad
            print("Stock actualizado.")
        else:
            print("Producto no encontrado.")

    elif opcion == "4":
        # Ver todos los productos
        print("Listado de productos:")
        for i in range(len(nombres)):
            print(f"{nombres[i]}: {cantidades[i]}")

    elif opcion == "5":
        # Salir
        print("Gracias por usar el sistema.")
        salir = False

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


