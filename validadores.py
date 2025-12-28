from catalogo import catalogo

#valida que el id del producto existe
def validador_id(id):
    for producto in catalogo:
        if producto.get("id") == id:
            return True
    
    print("ERROR - Ingrese el ID de un producto que exista en el catálogo")  
    return False              

  