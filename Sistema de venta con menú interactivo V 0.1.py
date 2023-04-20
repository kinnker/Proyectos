def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (opcion_incorrecta := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return opcion_incorrecta


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_principal():
    opciones = {
        '1': ('Ingresar a la Venta', accion1),
        '2': ('Agregar un producto nuevo al sistema', accion2),
        '3': ('Ingresar stock de un producto existente',accion3),
        '4': ('Eliminar producto del sistema', accion4),
        '5': ('Cambiar precio a un producto', accion5),
        '6': ('Consultar un producto', accion6),
        '7': ('Mostrar listado de productos', accion7),
        '8': ('Salir', salir)
    }

    generar_menu(opciones, '8')



productos = {}
carrito = {}


def agregar_producto_sistema(nombre,precio_lista,stock):
    global productos
    productos.update({nombre: [precio_lista,stock]})


agregar_producto_sistema("pan flauta",58,3)
agregar_producto_sistema("agua salus sin gas 2L",60,6)
agregar_producto_sistema("agua salus sin gas 1.5L",52,5)


def agregar_producto_venta():
    global productos
    global carrito
    producto_agregado = str(input("Agregar producto: "))
    if producto_agregado in productos:
        cantidad = int(input("Cantidad: "))
        if cantidad <= productos[producto_agregado][1]:
            carrito.update({producto_agregado: [productos[producto_agregado][0] * cantidad]})
            print(f"{carrito}")
            productos[producto_agregado][1] -= cantidad
            opcion = int(input("Ingrese 0 para agregar otro producto a la venta o 1 para terminar: "))
            if opcion == 0:
                agregar_producto_venta()
            else:
                calcular_total()
                vaciar_carrito()
        else:
            print("Stock del producto insuficiente")
            agregar_producto_venta()
    else:
        print("Producto no encontrado \nSi desea volver a la venta presione 0 \nSi desea volver al inicio presione 1 ")
        volver_menu = int(input(""))
        if volver_menu == 0:
            if carrito == {}:
                agregar_producto_venta()
            else:
                opcion = int(input("Si desea agregar otro articulo presione 0, sino presione 1 "))
                if opcion == 0:
                    agregar_producto_venta()
                else:    
                    calcular_total()
                    vaciar_carrito()
        else:
            menu_principal()
        pass


def calcular_total():
    global carrito
    total = sum(carrito[nombre][0] for nombre in carrito)
    print(f"El total de la compra es: {total}")
    recibo = int(input("Usted recibe: "))
    if recibo >= total:
        vuelto = recibo - total
        print(f"El vuelto es: {vuelto} \nMuchas gracias por su compra!")
    else:
        print(f"El importe digitado es menor al total")
        calcular_total()


def vaciar_carrito():
    global carrito
    carrito.clear()


def agregar_producto_manual():
    global productos
    nombre = str(input("Ingrese nombre del producto: "))
    precio_lista = float(input("Ingrese precio de lista del producto: "))
    stock = int(input("Ingrese stock del producto: "))
    productos.update({nombre: [precio_lista,stock]})
    print(f"Se agregó excitosamente el producto {nombre} con precio ${precio_lista} y stock {stock}")


def agregar_stock():
    global productos
    producto = str(input("Ingrese nombre del producto: "))
    cantidad_a_ingresar = int(input("Ingrese la cantidad a ingresar: "))
    if producto in productos and cantidad_a_ingresar != 0:
        productos[producto][1] += cantidad_a_ingresar
        print(f"Se ingresaron {cantidad_a_ingresar} unidades de {producto}")
    else:
        print(f"El producto {producto} no se encuentra agregado o la cantidad a ingresar es 0")

def cambiar_precio():
    global productos
    producto = str(input("Ingrese nombre del producto: "))
    nuevo_precio = int(input("Nuevo precio: "))
    if producto in productos and nuevo_precio != 0:
        productos[producto][0] = nuevo_precio
        print(f"Se ajustó el precio de lista al producto {producto} a: ${nuevo_precio}")
    elif producto in productos and nuevo_precio == 0:
        print(f"Imposible asignarle 0 al precio")
    else:
        print(f"El producto {producto} no se encuentra agregado o el nuevo precio es 0")
        

def eliminar_producto_sistema():
    global productos
    nombre = str(input("Nombre del producto a eliminar: "))
    if nombre in productos:
        del productos[nombre]
        print(f"Se eliminó con exito {nombre}")
    else:
        print(f"{nombre} no se encuentra en el sistema")


def consultar_producto():
    global productos
    nombre = str(input("Nombre del producto a consultar: "))
    if nombre in productos:
        print(f"El producto {nombre} tiene precio: ${productos[nombre][0]} y stock: {productos[nombre][1]}")
    else:
        print(f"El producto {nombre} no se encuentra en el sistema, verifique por favor")


def accion1():
    print('Bienvenido a la venta')
    agregar_producto_venta()


def accion2():
    agregar_producto_manual()


def accion3():
    agregar_stock()


def accion4():
    eliminar_producto_sistema()


def accion5():
    cambiar_precio()


def accion6():
    consultar_producto()


def accion7():
    print(productos)


def salir():
    print('Saliendo')


menu_principal()