"""
Docstring para catalogo
Este es el archivo que contiene el catálogo que usaremos y las funciones del mismo
Ver Catálogo y busqueda de producto
"""

catalogo = [
    {'id': 1, 'Nombre': 'Pisco Mistral', 'Categoría': 'Pisco', 'Precio': 4500},
    {'id': 2, 'Nombre': 'Ron Havana', 'Categoría': 'Ron', 'Precio': 8500},
    {'id': 3, 'Nombre': 'Pisco Mistral Nobel', 'Categoría': 'Pisco', 'Precio': 12000},
    {'id': 4, 'Nombre': 'Gin Hendricks', 'Categoría': 'Gin', 'Precio': 24000},
    {'id': 5, 'Nombre': 'Cerveza Corona', 'Categoría': 'Cerveza', 'Precio': 2500},
    {'id': 6, 'Nombre': 'Gin Beefeather', 'Categoría': 'Gin', 'Precio': 12000},
]


def ver_catalogo():
    #funcion para mostrar el catalogo de productos por consola
    print("\nEstos son los productos disponibles")
    print("----------------------------------------")

    for producto in catalogo:
        print(f"ID: {producto["id"]} - Nombre: {producto["Nombre"]} - Categoría: {producto['Categoría']} - Precio: ${producto["Precio"]}")


def busqueda_producto(referencia):
    #funcion para buscar un producto segun la coincidencia de nombre o categoria
    encontrado = False
    
    print("\nProductos encontrados")
    print("----------------------------------------")
    for producto in catalogo:
        if referencia.lower() in producto['Nombre'].lower() or referencia.lower() in producto['Categoría'].lower():
            print(f"ID: {producto['id']} \n" 
                  f"Nombre: {producto['Nombre']} \n" 
                  f"Categoría: {producto['Categoría']} \n"
                  f"Precio: {producto['Precio']} \n")
            encontrado = True
            
    if not encontrado:
        print('Este producto no está en el catálogo o no está disponible \n')  


