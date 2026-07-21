from core_engine.repositorios import ICartRepository
from core_engine.models import Orden, DetalleOrden
from core_engine.exception import StockInsuficienteError

class CartService:
    def __init__(self, repositorio: ICartRepository):
        self.repositorio = repositorio
   
    def agregar_item(self, usuario_id:int, producto_id :int, cantidad:int):
        try:
            producto = self.repositorio.obtener_por_id(producto_id)

            if producto is None:
                raise ValueError("Producto inexistente")

            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a cero")

            if cantidad > producto.stock:
                raise StockInsuficienteError(
                    f"Stock insuficiente para {producto.nombre}"
                )
            
            nuevo_producto = {
                "usuario_id": usuario_id,
                "producto_id": producto.id,
                "cantidad": cantidad,
                "precio_unitario": producto.precio
            }

            print(f"[Servicio] Se agregó {producto.nombre} al carrito")
            return nuevo_producto
        
        except Exception:
            raise
            

    def procesar_checkout(self, usuario_id, items_carrito):

        self.repositorio.iniciar_transaccion()
        try:
            total = 0
            detalles = []

            for item in items_carrito:
                producto = self.repositorio.obtener_por_id_transaccion(
                    item["producto_id"]
                )
                if producto is None:
                    raise ValueError("Producto inexistente")

                if producto.stock < item["cantidad"]:
                    self.repositorio.cancelar_transaccion()
                    raise StockInsuficienteError()
                    
            
                producto.stock -= item["cantidad"]
                self.repositorio.actualizar_producto(producto)
                subtotal = producto.precio * item["cantidad"]
                total += subtotal

                detalles.append({
                    "producto": producto,
                    "cantidad": item["cantidad"]
                })

            orden = Orden(
                usuario_id=usuario_id,
                total=total,
                estado="Completada"
            )

            self.repositorio.guardar_orden(orden)

            for detalle in detalles:

                nuevo = DetalleOrden(
                    orden_id=orden.id,
                    producto_id=detalle["producto"].id,
                    cantidad=detalle["cantidad"],
                    precio_unitario_historico=detalle["producto"].precio
                )

                self.repositorio.guardar_detalle(nuevo)

            self.repositorio.confirmar_transaccion()

            return orden

        except Exception:
            self.repositorio.cancelar_transaccion()
            raise



"""Descripción: Implementar la clase/servicio CartService que maneje las reglas de negocio antes de tocar la persistencia final.

Crear método agregar_item(usuario_id, producto_id, cantidad).

Validación 1: Verificar que el producto_id exista.

Validación 2: Verificar que cantidad sea mayor a 0.

Validación 3: Lanzar una excepción personalizada StockInsuficienteError si la cantidad solicitada supera el stock actual del producto."""








"""Descripción: Construir el método procesar_checkout(usuario_id, items_carrito). Este es el núcleo duro del ticket.

Debe ejecutarse dentro de un bloque transaccional (ej. with session.begin(): o bloques transaccionales nativos de SQL).

Paso 1: Descontar el stock de cada producto en la base de datos.

Paso 2 (Anti-Race Condition): Implementar bloqueos a nivel de fila (SELECT ... FOR UPDATE) o depender del CHECK constraint de la BD para que si el stock baja de 0 durante el query, la base de datos rechace la operación.

Paso 3: Si algún producto falla por stock, atrapar la excepción, ejecutar un ROLLBACK total y notificar al usuario.

Paso 4: Si todo es exitoso, guardar el registro en Orden, guardar los múltiples registros en DetalleOrden copiando el precio exacto del producto en ese instante, y hacer COMMIT."""