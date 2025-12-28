"""

1) Propósito
Desarrollar una aplicación de consola en Python que modele el comportamiento básico de un
ecommerce:
• Mostrar un catálogo de productos.
• Permitir agregar productos a un carrito.
• Calcular el total a pagar.
Usando únicamente contenidos del Módulo 3: tipos de datos, condicionales, ciclos, estructuras de
datos y funciones.

2) Alcance del ejercicio (MVP)
2.1. Catálogo de productos
• Definir en el código un catálogo inicial con mínimo 5 productos.
• Cada producto debe tener:
o id (entero y único),
o nombre,
o categoría (ejemplo: "ropa", "tecnología", "hogar"),
o precio (número > 0).

Sugerencia: usar una lista de diccionarios o un diccionario donde la llave sea el id.


2.2. Menú principal
Al ejecutar el programa, se debe ver un menú similar:
Bienvenido/a a tu Ecommerce
1) Ver catálogo de productos
2) Buscar producto por nombre o categoría
3) Agregar producto al carrito
4) Ver carrito y total
5) Vaciar carrito
0) Salir
El menú debe repetirse hasta que el usuario elija la opción 0) Salir.

2.3. Carrito de compras
El carrito será una estructura en memoria (por ejemplo, una lista) donde se almacenan los productos
seleccionados.
Funcionalidad mínima:
• Agregar producto al carrito (opción 3)
o Pedir el id del producto.
o Pedir la cantidad (entero > 0).
o Validar que el id exista. Si no existe, mostrar mensaje de error.
o Guardar en el carrito el producto y la cantidad.
• Ver carrito y total (opción 4)
o Listar los ítems del carrito:
 id, nombre, cantidad, precio unitario, subtotal.
o Mostrar el total a pagar: suma de todos los subtotales.
• Vaciar carrito (opción 5)
o Dejar el carrito vacío y mostrar un mensaje de confirmación.
2.4. Búsqueda de productos (opción 2)
• Permitir buscar productos por nombre o por categoría.
• Mostrar todos los productos que coincidan con el texto ingresado (ej.: si escribe “ropa”, mostrar
todas las prendas).

3) Requisitos técnicos
El código debe:
• Estar escrito en Python 3 y ejecutarse desde consola:
python ecommerce_m3.py
• Usar tipos de datos básicos:
o int, float, str, bool.
• Usar estructuras de datos:
o Al menos una estructura compuesta para el catálogo (lista o diccionario).
o Al menos una estructura compuesta para el carrito (lista o diccionario).
• Usar condicionales (if, elif, else) para:
o Validar opciones del menú.
o Validar que la cantidad sea > 0.
o Mostrar mensajes distintos según si el carrito está vacío o no.
• Usar ciclos:
o Un ciclo while para el menú principal.
o Ciclos for o while para recorrer catálogo y carrito al mostrarlos.
• Usar funciones:
o Mínimo 3 funciones claramente separadas, por ejemplo:
 mostrar_menu()
 listar_productos(catalogo)
 buscar_productos(catalogo)
 agregar_al_carrito(catalogo, carrito)
 mostrar_carrito_y_total(carrito)
o Al menos una función debe recibir parámetros y retornar un valor.
• Usar nombres en snake_case, identación correcta y algunos comentarios breves.

4) Entregables
• Archivo Python: ecommerce_m3.py.
• (Opcional si se pide en el curso) un README.txt o README.md con:
o Breve descripción del programa.
o Cómo ejecutarlo.

"""
import mensajes
import catalogo
import carrito





while True:

    mensajes.menu()
    print('\nElija una opción')
    opcion = input(">>> ")

    if opcion == '1':
        #Ver catálogo de productos
        catalogo.ver_catalogo()

    elif opcion == '2':
        #Buscar productos por nombre o categoría
        busqueda = input("Ingrese una referencia para su busqueda: ")
        catalogo.busqueda_producto(busqueda)     

    elif opcion =='3':
        #primero muestra la lista de productos disponibles
        catalogo.ver_catalogo()
        #Agregar productos al carrito
        carrito.agregar_productos()

    elif opcion =='4':
        #Ver carrito y total
        carrito.ver_carrito()

    elif opcion =='5':
        #Vaciar carrito
        carrito.vaciar_carrito()

    elif opcion =='0':
        break

    else:
        print('\nIngresa una opción')