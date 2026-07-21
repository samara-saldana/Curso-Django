
from core_engine.servicio import CartService
from core_engine.repositorios import CartRepositorySQLAlchemy
from core_engine.models import Usuario, Producto, Orden, DetalleOrden, Base, engine
from sqlalchemy.orm import Session

with Session(engine)as session:
    usuario = Usuario(email="persona1@mail.com", nombre="Persona1")
    producto1 = Producto(sku="P001", nombre="Mouse", precio=300, stock=20)
    producto2 = Producto(sku="P002", nombre="Teclado", precio=500, stock=20)

    session.add_all([usuario,producto1,producto2])
    session.commit()



if __name__ == '__main__':

    repo = CartRepositorySQLAlchemy()
    service = CartService(repo)

    items = []
    items.append(
        service.agregar_item(1,1,2)
    )
    items.append(
        service.agregar_item(1,4,1)
    )
    items.append(
        service.agregar_item(1,2,1)
    )

    service.procesar_checkout(1, items)

