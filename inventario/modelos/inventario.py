
from datetime import datetime
from collections import Counter

        
class Inventario:
    def __init__(self):
        self.productos = []
        self.ventas = []
    
    def registrar_producto(self, producto):
        """
        Registrar un nuevo producto en el inventario.
        """
        self.productos.append(producto)

    def realizar_venta(self, venta):
        """
        Crea una nueva venta
        """
        self.ventas.append(venta)

    def buscar_producto(self, codigo):
        """
        Busca un producto a partir de su ID.
        """
        for p in self.productos:
            if p.codigo == codigo:
                return p
        
        return None

    def cambiar_estado_producto(self, producto):
        """
        Cambia el estado de un producto.
        """
        producto.disponible = not producto.disponible

    def ventas_rango_fecha(self, fecha_inicio, fecha_final):
        """
        Obtiene las ventas que se han realizado en un rango de fecha.
        """
        ventas_rango = []

        for v in self.ventas:
            if fecha_inicio <= v.fecha <= fecha_final:
                ventas_rango.append(v)
        
        return ventas_rango

    def top_5_mas_vendidos(self):
        """
        Obtiene el top 5 de los productos más vendidos.
        """
        conteo_ventas = {}

        for v in self.ventas:
            if v.codigo_producto in conteo_ventas:
                conteo_ventas[v.codigo_producto] += v.cantidad
            else:
                conteo_ventas[v.codigo_producto] = v.cantidad

        conteo_ventas = {k: v for k, v in sorted(conteo_ventas.items(), key=lambda item: item[1], reverse=True)}

        contador = Counter(conteo_ventas)

        return contador.most_common(5)

    def top_5_menos_vendidos(self):
        """
        Obtiene el top 5 de los productos menos vendidos.
        """
        conteo_ventas = {}

        for v in self.ventas:
            if v.codigo_producto in conteo_ventas:
                conteo_ventas[v.codigo_producto] += v.cantidad
            else:
                conteo_ventas[v.codigo_producto] = v.cantidad

        conteo_ventas = {k: v for k, v in sorted(conteo_ventas.items(), key=lambda item: item[1])}

        contador = Counter(conteo_ventas)

        return contador.most_common()[:-6:-1]

    def mostrar_datos_producto(self, producto):
        """
        Muestra los datos particulares de un producto.
        """
        print('ID: %i' % producto.codigo)
        print('Nombre: %s' % producto.nombre)
        print('Precio: $%.2f' % producto.precio)
        print('Cantidad: %i' % producto.cantidad)
        print('¿Disponible?: %s' % ('Sí' if producto.disponible else 'No'))

    def mostrar_datos_venta(self, venta):
        """
        Muestra los datos particulares de una venta.
        """
        print('ID Producto: %i' % venta.codigo_producto)
        print('Fecha: %s' % venta.fecha)
        print('Cantidad: %i' % venta.cantidad)
        print('Total sin IGV: $%.2f' % venta.total_sin_igv)
        print('Total: $%.2f' % (venta.total_sin_igv * 1.18))
        print()
        print('Datos del producto:')
        self.mostrar_datos_producto(self.buscar_producto(venta.codigo_producto))

    def mostrar_datos_venta_producto(self, datos_venta):
        producto = self.buscar_producto(datos_venta[0])
        self.mostrar_datos_producto(producto)
        print('Cantidad vendida: %i' % datos_venta[1])
        
class Producto:
    def __init__(self, codigo, nombre, precio, cantidad, disponible):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.disponible = disponible


class Venta:
    def __init__(self, codigo_producto, cantidad, total_sin_igv):
        self.codigo_producto = codigo_producto
        self.fecha = datetime.now()
        self.cantidad = cantidad
        self.total_sin_igv = total_sin_igv