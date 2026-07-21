
from core_engine.servicio import CartService
from core_engine.repositorios import CartRepositorySQLAlchemy
from core_engine.models import Usuario, Producto, Orden, DetalleOrden, Base, engine
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)

def inicializar_db():
    Base.metadata.create_all(engine)
    print("Base de datos inicializada correctamente")


def crear_datos_iniciales():
    with Session(engine) as session:

        if session.query(Usuario).count() == 0:

            usuario = Usuario(
                email="cliente@mail.com",
                nombre="Samara"
            )

            productos = [
                Producto(
                    sku="P001",
                    nombre="Mouse",
                    precio=300,
                    stock=20
                ),
                Producto(
                    sku="P002",
                    nombre="Teclado",
                    precio=500,
                    stock=15
                ),
                Producto(
                    sku="P003",
                    nombre="Monitor",
                    precio=3000,
                    stock=5
                )
            ]

            session.add(usuario)
            session.add_all(productos)

            session.commit()

            print("Datos iniciales creados")


def mostrar_productos():

    with Session(engine) as session:

        productos = session.query(Producto).all()

        if not productos:
            print("No hay productos disponibles")
            return False

        print("\nPRODUCTOS DISPONIBLES")
        print("-"*40)

        for producto in productos:
            print(
                f"ID: {producto.id} | "
                f"{producto.nombre} | "
                f"${producto.precio} | "
                f"Stock: {producto.stock}"
            )

        return True

def mostrar_ordenes():

    with Session(engine) as session:

        ordenes = session.query(Orden).all()

        if not ordenes:
            print("No hay ordenes disponibles")
            return False

        print("\nORDENES PROCESADAS")
        print("-"*40)

        for orden in ordenes:
            print(
                f"ID: {orden.id} | "
                f"{ orden.usuario_id} | "
                f"${orden.total} | "
                f"Stock: {orden.estado} | "
                f"${orden.fecha_creacion}"

            )

        return True

def comprar_producto():

    repo = CartRepositorySQLAlchemy()
    service = CartService(repo)

    try:

        hay_productos = mostrar_productos()

        if not hay_productos:
            return


        producto_id = int(
            input("\nIngresa el ID del producto: ")
        )

        cantidad = int(
            input("Cantidad que deseas comprar: ")
        )


        item = service.agregar_item(
            usuario_id=1,
            producto_id=producto_id,
            cantidad=cantidad
        )


        print("\nProducto agregado al carrito")
        print(item)


        confirmar = input(
            "\n¿Deseas finalizar compra? (s/n): "
        )


        if confirmar.lower() == "s":

            orden = service.procesar_checkout(
                usuario_id=1,
                items_carrito=[item]
            )

            print("\nCompra realizada correctamente")
            print(
                f"Orden número: {orden.id}"
            )

        else:
            print("Compra cancelada")


    except Exception as e:

        print(f"\nError: {e}")

if __name__ == '__main__':

    while True:

        print("\n" + "="*50)
        print("      SISTEMA E-COMMERCE")
        print("="*50)

        print("""
1. Inicializar base de datos
2. Crear datos iniciales
3. Mostrar productos
4. Comprar producto
5. Mostrar ordenes
6. Salir
        """)

        opcion = input("Selecciona una opción: ")


        if opcion == "1":

            inicializar_db()


        elif opcion == "2":

            crear_datos_iniciales()


        elif opcion == "3":

            mostrar_productos()


        elif opcion == "4":

            comprar_producto()
        
        elif opcion == "5":

            mostrar_ordenes()


        elif opcion == "6":

            print("Cerrando aplicación...")
            break


        else:

            print("Opción inválida")




#docker compose -f Docker-compose-main.yml up -d subo el contenedor
    # docker exec -it ecommerce_python python main.py       ejecuta el main