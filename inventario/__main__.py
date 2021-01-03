from modelos.inventario import Inventario, Venta, Producto
import os
import datetime
import pickle


def imp_opciones():
    """
    Imprime el menú de las operaciones disponibles.
    """

    print("=======================================================")
    print("=============== BOTICA LA INMACULADDA =================")
    print("=======================================================")   
    print("==  1- Agregar producto nuevo                        ==")
    print("==  2- Despachar un producto                         ==")
    print("==  3- Buscar un producto por su código              ==")
    print("==  4- Cambiar disponibilidad de un producto         ==")
    print("==  5- Productos vendidos en un rango de fechas      ==")
    print("==  6- Ver los 5 productos más vendidos              ==")
    print("==  7- Ver los 5  productos menos vendidos           ==")
    print("==  0- Salir                                         ==")
    print("=======================================================")
    print("=======================================================")



def capturar_cadena(mensaje):
    """
    Captura una cadena de caracteres y valida la entrada de datos.

    """
    while True:
        cadena = input(f'{mensaje}: ').strip()

        if len(cadena):
            return cadena
        else:
            print('MENSAJE: Debe digitar una cadena de caracteres con texto.')
        
        print()

def num_real(mensaje):
    """
    Toma un número real y valida la entrada de datos.

    """
    while True:
        try:
            numero = float(input(f'{mensaje}: '))

            return numero
        except ValueError:
            print('ERROR: Debe digitar un número real.')
        
        print()
        
def num_entero(mensaje):
    """
    Toma un número entero y valida la entrada de datos.
    """
    while True:
        try:
            numero = int(input(f'{mensaje}: '))

            return numero
        except ValueError:
            print('ERROR: Debe digitar un número entero.')
        
        print()
        
def continuar():
    """
    Muestra mensaje de continuación en la consola.
    """
    print()
    print('Presione Enter para continuar...', end='')
    input()
    print()

def cargar_inventario():
    while True:
        print('¿Desea cargar los datos del inventario y las ventas desde el archivo `inventario.pickle`?:')
        print('1.- Sí')
        print('2.- No')
        opcion = num_entero('Digite la opción')

        if opcion == 1 or opcion == 2:
            break
    
    if opcion == 1:
        with open('inventario/inventario.pickle', 'rb') as f:
            inventario = pickle.load(f)
            return inventario
    
    return None

def listar_productos(productos):
    """
    Imprime un listado de productos.
    """
    for p in productos:
        print(f"{p.codigo} - {p.nombre}")


def guardar_datos(inventario):
    while True:
        print('¿Desea guardar los datos de productos y ventas en el archivo `inventario.pickle`?:')
        print('1.- Sí')
        print('2.- No')
        opcion = num_entero('Digite la opción')

        if opcion == 1 or opcion == 2:
            break
    
    if opcion == 1:
        with open('inventario/inventario.pickle', 'wb') as f:

            pickle.dump(inventario, f)

        return True
    else:
        return False

def main():
    """
    Punto de entrada a la aplicación.
    """
    inventario = Inventario()

    if os.path.isfile('inventario/inventario.pickle'):
        resultado = cargar_inventario()
        
        if resultado:
            inventario.productos = resultado['productos']
            inventario.ventas = resultado['ventas']

    while True:
        while True:
            try:
                imp_opciones()
                opcion = int(input('Digite la opción: '))
                if 0 <= opcion <= 7:
                    break
                else:
                    print('MENSAJE: Debe digitar un número mayor o igual a 0 y menor o igual a 7.')
            except ValueError:
                print()
                print('ERROR: Debe digitar un número entero válido.')
            
            continuar()
        
        print()

        if opcion == 0:
            break
        elif opcion == 1:
            while True:
                codigo_producto = num_entero('Digite el ID del nuevo producto')

                if codigo_producto > 0:
                    producto = inventario.buscar_producto(codigo_producto)

                    if producto is None:
                        break
                    else:
                        print()
                        print('MENSAJE: Ya existe un producto con el ID digitado.')
                else:
                    print()
                    print('MENSAJE: El ID del producto debe ser un número positivo.')
                
                continuar()
            
            nombre_producto = capturar_cadena('Digite el nombre del producto a agregar')

            while True:
                precio_producto = num_real('Digite el precio del producto a agregar')

                if precio_producto > 0:
                    break
                else:
                    print()
                    print('MENSAJE: Debe digitar un precio positivo para el producto.')
                
                continuar()
            
            while True:
                cantidad_producto = num_entero('Digite la cantidad del nuevo producto')

                if cantidad_producto > 0:
                    break
                else:
                    print()
                    print('MENSAJE: Debe digitar una cantidad positiva para el producto.')
                
                continuar()
            
            while True:
                print('1. Disponible')
                print('2. No Disponible')
                disponible = num_entero('Digite la opción para la disponibilidad del producto')

                if disponible == 1 or disponible == 2:
                    disponible = disponible == 1
                    break
                else:
                    print()
                    print('MENSAJE: La opción {} de disponibilidad no existe.'.format(disponible))
                
                continuar()
            
            nuevo_producto = Producto(codigo_producto, nombre_producto, precio_producto, cantidad_producto, disponible)

            inventario.registrar_producto(nuevo_producto)

            print()
            print('MENSAJE: El producto se ha creado de forma satisfactoria.')
        if opcion == 2:
            if len(inventario.productos):
                while True:
                    listar_productos(inventario.productos)
                    codigo_producto = num_entero('Digite el ID del producto')

                    producto = inventario.buscar_producto(codigo_producto)

                    if producto:
                        break
                    else:
                        print()
                        print('MENSAJE: Debe escribir un ID de producto existente.')
                
                while True:
                    cantidad_producto = num_entero('Digite la cantidad del producto')

                    if cantidad_producto > 0:
                        if cantidad_producto <= producto.cantidad:
                            break
                        else:
                            print()
                            print('MENSAJE: No existe cantidad suficiente para la venta. Sólo hay {} unidades.'.format(producto.cantidad))
                    else:
                        print()
                        print('MENSAJE: Debe digitar una cantidad positiva para el producto.')

                    continuar()
                
                nueva_venta = Venta(codigo_producto, cantidad_producto, producto.precio * cantidad_producto)

                inventario.realizar_venta(nueva_venta)

                print('Total: $%.2f' % (nueva_venta.total_sin_igv * 1.18))

                print()
                print('MENSAJE: La venta se ha realizado de forma satisfactoria.')
            else:
                print()
                print('MENSAJE: Aún no ha registrado productos.')
        elif opcion == 3:
            if len(inventario.productos):
                while True:
                    listar_productos(inventario.productos)
                    codigo_producto = num_entero('Digite el ID del producto')

                    producto = inventario.buscar_producto(codigo_producto)

                    if producto:
                        break
                    else:
                        print()
                        print('MENSAJE: Debe escribir un ID de producto existente.')
                    
                    continuar()
                
                print()
                inventario.mostrar_datos_producto(producto)
            else:
                print()
                print('MENSAJE: Aún no ha registrado productos.')
        elif opcion == 4:
            if len(inventario.productos):
                while True:
                    listar_productos(inventario.productos)
                    codigo_producto = num_entero('Digite el ID del producto')

                    producto = inventario.buscar_producto(codigo_producto)

                    if producto:
                        break
                    else:
                        print()
                        print('MENSAJE: Debe escribir un ID de producto existente.')
                    
                    continuar()
                
                inventario.cambiar_estado_producto(producto)
                inventario.mostrar_datos_producto(producto)
            else:
                print()
                print('MENSAJE: Aún no ha registrado productos.')
        elif opcion == 5:
            if len(inventario.productos):
                if len(inventario.ventas):
                    while True:
                        try:
                            fecha_inicio = capturar_cadena('Digite la fecha de inicio (AAAA-MM-DD)')

                            fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
                            break
                        except ValueError:
                            print()
                            print('ERROR: Debe digitar una fecha válida con el formato AAAA-MM-DD.')
                        
                        print()

                    while True:
                        try:
                            fecha_final = capturar_cadena('Digite la fecha final (AAAA-MM-DD)')

                            fecha_final = datetime.datetime.strptime(fecha_final, '%Y-%m-%d')
                            break
                        except ValueError:
                            print()
                            print('ERROR: Debe digitar una fecha válida con el formato AAAA-MM-DD.')
                        
                        print()
                    
                    ventas_rango = inventario.ventas_rango_fecha(fecha_inicio, fecha_final)

                    if len(ventas_rango):
                        for v in ventas_rango:
                            inventario.mostrar_datos_venta(v)
                            print()
                    else:
                        print()
                        print('MENSAJE: No hay ventas para el rango seleccionado.')
                else:
                    print()
                    print('MENSAJE: Aún no ha efectuado ninguna venta.')
            else:
                print()
                print('MENSAJE: Aún no ha registrado productos.')
        elif opcion == 6:
            if len(inventario.productos):
                if len(inventario.ventas):
                    productos_vendidos = inventario.top_5_mas_vendidos()

                    print('Top 5 de los productos más vendidos')
                    for p in productos_vendidos:
                        inventario.mostrar_datos_venta_producto( p)
                        print()
                else:
                    print()
                    print('MENSAJE: Aún no ha efectuado ninguna venta.')
            else:
                print()
                print('MENSAJE: Aún no ha registrado productos.')
        elif opcion == 7:
            if len(inventario.productos):
                if len(inventario.ventas):
                    productos_vendidos = inventario.top_5_menos_vendidos()

                    print('Top 5 de los productos menos vendidos')
                    for p in productos_vendidos:
                        inventario.mostrar_datos_venta_producto(p)
                        print()
                else:
                    print()
                    print('MENSAJE: Aún no ha efectuado ninguna venta.')
            else:
                print()
                print('MENSAJE: Aún no ha registrado productos.')
        
        continuar()
    
    print()

    if len(inventario.productos):
        if guardar_datos(inventario):
            print('Los datos del inventario (productos y ventas) se han guardado en disco.')
        else:
            print('Ha omitido almacenar los datos en disco.')

    print()

    print('Fin del programa.')

if __name__ == '__main__':
    main()
