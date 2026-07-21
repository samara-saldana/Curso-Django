from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime, func, CheckConstraint
from dotenv import load_dotenv
import os


Base = declarative_base()
load_dotenv(".env.docker")
DB_URL = os.getenv("DB_URL")
#print(DB_URL)
engine = create_engine(DB_URL, echo=False)


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    nombre = Column(String, nullable=False)


class Producto(Base):
    __tablename__ = 'producto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sku = Column(String, unique=True, nullable=False)
    nombre = Column(String, nullable=False) 
    precio = Column(Float, default=0) 
    stock = Column(Integer, default=0) 

    __table_args__ = (
        CheckConstraint('precio > 0', name='revisar_precio_mayor_cero'),
        CheckConstraint('stock >= 0', name='revisar_stock_positivo')
    )


class Orden(Base):
    __tablename__ = 'orden'

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id", ondelete="CASCADE" ), nullable=False)
    total = Column(Float, default=0)
    estado = Column(String, nullable=False) #"Pendiente", "Completada", "Cancelada"
    fecha_creacion = Column(DateTime, nullable=False, default=func.now())   #func.now(fecha de creacion)


class DetalleOrden(Base):
    __tablename__ = 'detalle_orden'

    id = Column(Integer, primary_key=True, autoincrement=True)
    orden_id = Column(Integer, ForeignKey("orden.id", ondelete="CASCADE"), nullable=False)
    producto_id = Column(Integer, ForeignKey("producto.id", ondelete="CASCADE"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario_historico = Column(Float, nullable=False)

    __table_args__ = (
        CheckConstraint('cantidad > 0', name='revisar_cantidad_mayor_cero'),
     )
    



"""Descripción: Crear los modelos y las tablas base. Deben respetar las restricciones de integridad relacional (Foreign Keys) y usar tipos de datos correctos.

Modelo Usuario: id (PK), email (Unique), nombre.

Modelo Producto: id (PK), sku (Unique), nombre, precio (Float/Decimal, > 0), stock (Integer, >= 0).

Modelo Orden: id (PK), usuario_id (FK), total (Float/Decimal), estado (String: "Pendiente", "Completada", "Cancelada"), fecha_creacion.

Modelo DetalleOrden: id (PK), orden_id (FK), producto_id (FK), cantidad (Integer, > 0), precio_unitario_historico (Float/Decimal).

Nota Técnica: Asegurar que la base de datos tenga un CHECK constraint en el stock de Producto para que nunca pueda ser negativo a nivel estructural.

 

Nomenclatura: 

PK = Primary Key

FK = Foreign Key"""