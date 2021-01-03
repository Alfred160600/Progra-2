from datetime import datetime
from collections import Counter

def registrar_producto(productos, producto):
    """
    Registrar un nuevo producto en el inventario.
    """
    productos.append(producto)

def realizar_venta(ventas, venta):
    """
    Crea una nueva venta
    """
    venta['fecha'] = datetime.now()
    ventas.append(venta)

def buscar_producto(productos, id_producto):
    """
    Busca un producto a partir de su ID.
    """
    for p in productos:
        if p['id_producto'] == id_producto:
            return p
    
    return None

def cambiar_estado_producto(producto):
    """
    Cambia el estado de un producto.
    """
    producto['disponible'] = not producto['disponible']

def ventas_rango_fecha(ventas, fecha_inicio, fecha_final):
    """
    Obtiene las ventas que se han realizado en un rango de fecha.
    """
    ventas_rango = []

    for v in ventas:
        if fecha_inicio <= v['fecha'] <= fecha_final:
            ventas_rango.append(v)
    
    return ventas_rango

def top_5_mas_vendidos(ventas):
    """
    Obtiene el top 5 de los productos más vendidos.
    """
    conteo_ventas = {}

    for v in ventas:
        if v['id_producto'] in conteo_ventas:
            conteo_ventas[v['id_producto']] += v['cantidad']
        else:
            conteo_ventas[v['id_producto']] = v['cantidad']

    conteo_ventas = {k: v for k, v in sorted(conteo_ventas.items(), key=lambda item: item[1], reverse=True)}

    contador = Counter(conteo_ventas)

    return contador.most_common(5)

def top_5_menos_vendidos(ventas):
    """
    Obtiene el top 5 de los productos menos vendidos.
    """
    conteo_ventas = {}

    for v in ventas:
        if v['id_producto'] in conteo_ventas:
            conteo_ventas[v['id_producto']] += v['cantidad']
        else:
            conteo_ventas[v['id_producto']] = v['cantidad']

    conteo_ventas = {k: v for k, v in sorted(conteo_ventas.items(), key=lambda item: item[1])}

    contador = Counter(conteo_ventas)

    return contador.most_common()[:-6:-1]

def mostrar_datos_producto(producto):
    """
    Muestra los datos particulares de un producto.
    """
    print('Nombre: %s' % producto['nombre'])
    print('ID: %i' % producto['id_producto'])
    print('Precio: $%.2f' % producto['precio'])
    print('Cantidad: %i' % producto['cantidad'])
    print('¿Disponible?: %s' % ('Sí' if producto['disponible'] else 'No'))

def mostrar_datos_venta(productos, venta):
    """
    Muestra los datos particulares de una venta.
    """
    print('ID Producto: %i' % venta['id_producto'])
    print('Fecha: %s' % venta['fecha'])
    print('Cantidad: %i' % venta['cantidad'])
    print('Total sin IGV: $%.2f' % venta['total_sin_igv'])
    print('Total:: $%.2f' % (venta['total_sin_igv'] * 1.18))
    print()
    print('Datos del producto:')
    mostrar_datos_producto(buscar_producto(productos, venta['id_producto']))

def mostrar_datos_venta_producto(productos, datos_venta):
    producto = buscar_producto(productos, datos_venta[0])
    mostrar_datos_producto(producto)
    print('Cantidad vendida: %i' % datos_venta[1])
