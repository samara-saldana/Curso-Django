import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from core_engine.repositorios import CartRepositorySQLAlchemy
from core_engine.servicio import CartService
from core_engine.models import Usuario, Producto, Base, engine, Orden
from sqlalchemy.orm import Session
from core_engine.exception import StockInsuficienteError


@pytest.fixture                                                #antes de cada prueba queremos que la base quede vacía, tons cada test empieza desde cero
def db_limpia():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    yield

    Base.metadata.drop_all(engine)


@pytest.fixture 
def datos_prueba(db_limpia):

    with Session(engine)as session:

        usuario = Usuario(email="persona3@mail.com", nombre="Persona3")
        producto1 = Producto(sku="P003", nombre="Coca-Cola", precio=25, stock=6)
        producto2 = Producto(sku="P004", nombre="Pepsi", precio=20, stock=5)

        session.add_all([usuario,producto1,producto2])
        session.commit()

    yield


def test_producto_guardado(datos_prueba):
    with Session(engine)as session:

        producto = session.query(Producto).filter_by(nombre="Coca-Cola").first()

        assert producto is not None                                             #comprueba que el producto existe
        assert producto.stock == 6                                              #comprueba que el stok es 6


def test_agregar_item(datos_prueba):
    repo = CartRepositorySQLAlchemy()
    service = CartService(repo)

    item = service.agregar_item(usuario_id=1, producto_id=1, cantidad=2)

    assert item['cantidad'] == 2                                           #comprueba que la cantidad de lo que se agrego al carrito
    assert item['producto_id'] == 1                                                     #comprueba el id del producto que se agrego al carrito


def test_checkout(datos_prueba):
    repo = CartRepositorySQLAlchemy()
    service = CartService(repo)

    items = []

    items.append (service.agregar_item(usuario_id=1, producto_id=1, cantidad=2))
    service.procesar_checkout(1,items)

    with Session(engine) as session:                                    #Test 1 (Happy Path)
        orden = session.query(Orden).first() 
        producto = session.get(Producto,1)                                #comprueba que la cantidad de lo que se agrego al carrito
        
        assert orden is not None
        assert orden.estado == "Completada"
        assert producto.stock == 4  


def test_cantidad_negativa(datos_prueba):            #Test 2 (Chaos Test):
    repo = CartRepositorySQLAlchemy()
    service = CartService(repo)

    with pytest.raises(ValueError):
            service.agregar_item(1,1,-5)



@pytest.mark.parametrize("stock,cantidad",[(4, 5)])                                                        
def test_race_condition_fake(db_limpia, stock, cantidad):              #Test 3 (Race Condition Fake)

    with Session(engine) as session:

        usuario = Usuario(email="ana@mail.com",nombre="Ana")

        laptop = Producto(sku="L001",nombre="Laptop",precio=15000,stock=stock)

        session.add_all([usuario, laptop])
        session.commit()

    repo = CartRepositorySQLAlchemy()
    service = CartService(repo)

    carrito = [{
        "usuario_id": 1,
        "producto_id": 1,
        "cantidad": cantidad,
        "precio_unitario": 15000
    }]

    with pytest.raises(StockInsuficienteError):
        service.procesar_checkout(1, carrito)

    with Session(engine) as session:

        ordenes = session.query(Orden).count()

        assert ordenes == 0
   
        
