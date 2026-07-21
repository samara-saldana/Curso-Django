from core_engine.servicio import CartService
from core_engine.repositorios import CartRepositorySQLAlchemy
from core_engine.models import Usuario, Producto, Orden, DetalleOrden, Base, engine
from sqlalchemy.orm import Session


def inicializar_db():
    Base.metadata.create_all(engine)
    print("\n Base de datos inicializada correctamente")


def crear_datos_iniciales():
    with Session(engine) as session:
        if session.query(Usuario).count() == 0:
            usuario = Usuario(email="cliente@mail.com", nombre="Cliente")
            productos = [Producto(sku="P001", nombre="Mouse", precio=300,stock=20),
                Producto(sku="P002", nombre="Teclado", precio=500, stock=15),
                Producto(sku="P003", nombre="Monitor", precio=3000, stock=5)]

            session.add(usuario)
            session.add_all(productos)
            session.commit()

            print("\n Datos iniciales creados")


def crear_usuario():
    with Session(engine) as session:
        email = input("Ingrese su email: ").lower()
        nombre= input("Ingrese su nombre: ").lower()
        usuario = Usuario(email=email,nombre=nombre)

        session.add(usuario)
        session.commit()

        usuario_id = session.query(Usuario.id).filter(Usuario.email == email).one_or_none()

        print(f"\ Usuario agregado con exito, su ID de usuario es: {usuario_id[0]}")


def mostrar_productos():
    with Session(engine) as session:
        productos = session.query(Producto).all()

        if not productos:
            print("No hay productos disponibles")
            return False

        print("\n PRODUCTOS DISPONIBLES:")

        for producto in productos:
            print(f"\n ID: {producto.id} - Nombre: {producto.nombre} - Precio: ${producto.precio} - Stock: {producto.stock}")
    return True


def mostrar_usuarios():
    with Session(engine) as session:
        usuarios = session.query(Usuario).all()

        if not usuarios:
            print("No hay usuarios en la base de datos")
            return

        print("\n USUARIOS:")

        for  usuario in usuarios:
            print(f"\n ID: {usuario.id} - Nombre: {usuario.nombre} - Email: {usuario.email}")


def mostrar_ordenes():
    with Session(engine) as session:
        ordenes = session.query(Orden).all()
        if not ordenes:
            print("No hay ordenes disponibles")
            return
        
        print("\n ORDENES PROCESADAS:")

        for orden in ordenes:
            print(f"\n ID:{orden.id} - ID de Usuario: {orden.usuario_id}  - Total de la Orden: ${orden.total} - Estad de la orden: {orden.estado} - Fecha de creacion: {orden.fecha_creacion}")

        detalle_id = input("\nIngrese el ID de la orden para saber los detalles o presione enter para regresar al menu principal: ")
        if detalle_id != "":
            detalles = session.query(DetalleOrden).filter(DetalleOrden.orden_id == int(detalle_id)).all()
            for detalle in detalles:
                print("\n Mostrando el detalle de la orden:")
                print(f"\n ID:{detalle.id} - ID de Orden: {detalle.orden_id}  - ID del producto: {detalle.producto_id} - Cantiddad: {detalle.cantidad} - Precio unitario: {detalle.precio_unitario_historico}")


def comprar_producto():
    repo = CartRepositorySQLAlchemy()
    service = CartService(repo)

    try:
        hay_productos = mostrar_productos()

        if not hay_productos:
            return

        usuario_id = int(input("Ingrese su ID de usuario"))
        producto_id = int(input("Ingrese el ID del producto: "))
        cantidad = int(input("Ingrese la cantidad que deseas comprar: "))

        item = service.agregar_item(usuario_id=usuario_id, producto_id=producto_id, cantidad=cantidad)

        print(f"\n Producto agregado al carrito")

        confirmar = input("¿Deseas comprar los productos agregados a tu carrito? (s/n): ").lower()

        if confirmar == "s":
            orden = service.procesar_checkout(usuario_id=1, items_carrito=[item])
            print(f"Compra con ID ({orden.id}) realizada con exito")

        else:
            print("Compra cancelada")

    except Exception as e:
        print(f"Ocurrio un error al comprar el producto: {e}")


if __name__ == '__main__':
    while True:
        print("--\n Sistema ecommerce--")
        print("1. Inicializar base de datos")
        print("2. Crear datos iniciales")
        print("3. Crear usuario")
        print("4. Empezar a comprar")
        print("5. Mostrar ordenes")
        print("6. Mostrar usuarios")
        print("7. Salir")

        opcion = input("\n Selecciona una opción: ")

        if opcion == "1":
            inicializar_db()
        elif opcion == "2":
            crear_datos_iniciales()
        elif opcion == "3":
            crear_usuario()
        elif opcion == "4":
            comprar_producto()
        elif opcion == "5":
            mostrar_ordenes()
        elif opcion == "6":
            mostrar_usuarios()
        elif opcion == "7":
            print("Cerrando el sistema...")
            break
        else:
            print("Opción inválida, intenta de nuevo")




#docker compose -f Docker-compose-main.yml up -d subo el contenedor
# docker exec -it ecommerce_python python main.py       ejecuta el main


#      