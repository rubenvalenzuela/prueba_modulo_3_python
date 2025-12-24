import validadores
from catalogo import catalogo




carrito = []

#funcion para agregar productos al carrito
def agregar_productos():

    eleccion_producto = int(input("\nIngrese el ID del producto que quiere agregar al carrito: "))
    cantidad_producto = input("\nIngrese la cantidad que quiere de este producto: ")

    if validadores.validador_id(eleccion_producto):
        
        cantidad_int = int(cantidad_producto)
        
        for producto in catalogo:
            if producto['id'] == eleccion_producto:
                subtotal = cantidad_int * producto['Precio']
                carrito.append({"id" : producto['id'],
                                "Nombre" : producto['Nombre'],
                                "Categoría": producto['Categoría'], 
                                "Precio" : producto['Precio'],
                                "Cantidad" : cantidad_int, 
                                "Subtotal" : int(subtotal)
                            })
                print('Producto agregado correctamente al carrito\n')

def ver_carrito():

    total = 0

    if carrito:
        for producto_carrito in carrito:
            print(
                f'ID: {producto_carrito['id']}\n'
                f'Nombre: {producto_carrito['Nombre']}\n'
                f'Cantidad: {producto_carrito['Cantidad']}\n'
                f'Subtotal: {producto_carrito['Subtotal']}\n'
                "-----------------------------------------------------------"
            )

            total += producto_carrito['Subtotal']
        print(f'El total del carrito es: {total}')
    else:
        print('El carrito está vacio \n')


def vaciar_carrito():
    carrito.clear()
    print('Se limpio el carrito \n')




