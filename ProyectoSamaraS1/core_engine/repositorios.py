from abc import ABC, abstractmethod
from core_engine.models import Producto, Orden, DetalleOrden, Base, engine
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine

class ICartRepository(ABC):
    @abstractmethod
    def iniciar_transaccion(self) -> None:
        pass

    @abstractmethod
    def confirmar_transaccion(self) -> None:
        pass

    @abstractmethod
    def cancelar_transaccion(self) -> None:
        pass

    @abstractmethod
    def obtener_por_id(self, id_prod: int) -> Producto:
        pass

    @abstractmethod
    def obtener_por_id_transaccion(self, id_prod: int) -> Producto:
        pass

    @abstractmethod
    def actualizar_producto(self, producto: Producto) -> None:
        pass

    @abstractmethod
    def guardar_orden(self, orden: Orden) -> None :
        pass

    @abstractmethod
    def guardar_detalle(self, detalle: DetalleOrden) -> None:
        pass



class CartRepositorySQLAlchemy(ICartRepository):
    
    def __init__(self):
        self.engine = engine
        Base.metadata.create_all(self.engine)
        self.session = None

    def iniciar_transaccion(self):
        self.session = Session(self.engine)
        self.session.begin()

    def confirmar_transaccion(self):
        self.session.commit()
        self.session.close()
        self.session = None

    def cancelar_transaccion(self):
        if self.session:
            self.session.rollback()
            self.session.close()
            self.session = None

    def obtener_por_id(self, id_prod):
        if self.session is not None:                                                                                    #ya hay una sesión abierta y se quiere reutilizar
            return self.session.get(Producto, id_prod)

        with Session(self.engine) as session:                                                                           #no hay una esion abierta y la quiero abrir para consultar el id
            return session.get(Producto, id_prod)

    def actualizar_producto(self, producto: Producto):
        self.session.add(producto)

    def guardar_orden(self, orden: Orden):
        self.session.add(orden)
        self.session.flush()

    def guardar_detalle(self, detalle: DetalleOrden):
        self.session.add(detalle)

    def obtener_por_id_transaccion(self, id_prod) -> Producto:
        return (
            self.session.query(Producto)
            .filter(Producto.id == id_prod)
            .with_for_update()                                                                                                  #Se utiliza en consultas para bloquear filas seleccionadas durante una transacción, bloquea la fila hasta que se haga commit o rollback
            .one_or_none()                                                                                                      #Es un método que se aplica al final de un Query de SQLAlchemy.Recupera exactamente un resultado de la consulta, o ninguno si no coincide.Si hay más de un resultado, lanza una excepción MultipleResultsFound.     
        )

















"""class CartRepositoryMemoria(ICartRepository):

    def __init__(self):
        self.productos = {}
        self.ordenes = []
        self.detalles = []

    def obtener_por_id(self, id_prod):
        return self.productos.get(id_prod)

    def obtener_por_id_transaccion(self, id_prod):
        return self.productos.get(id_prod)

    def actualizar_producto(self, producto):
        self.productos[producto.id] = producto

    def guardar_orden(self, orden):
        orden.id = len(self.ordenes) + 1
        self.ordenes.append(orden)

    def guardar_detalle(self, detalle):
        detalle.id = len(self.detalles) + 1
        self.detalles.append(detalle)

    def iniciar_transaccion(self):
        pass

    def confirmar_transaccion(self):
        pass

    def cancelar_transaccion(self):
        pass
    
"""




"""add() → registra el objeto en la sesión.
flush() → envía los cambios a la BD pero sin confirmar la transacción.
commit() → confirma la transacción y hace permanentes los cambios."""