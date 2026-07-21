from abc import ABC, abstractmethod
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, Session


Base = declarative_base() #declaramos nuestra clase base


class LeadEntity(Base):   #entidad de base de datos
    """Modelo de la base de datos mapeado a un objeto Python"""
    __tablename__ = 'leads'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    empresa = Column(String, nullable=False)
    presupuesto = Column(Float, default=0.0)

    def __str__(self):
        return f"{self.nombre} | {self.empresa} | {self.presupuesto}"
    

class ILeadrepository(ABC):  #interaz
    @abstractmethod
    def guardar(self, lead:LeadEntity) -> None:
        pass

    @abstractmethod
    def obtener_todos(self) -> list[LeadEntity]:
        pass


class LeadRepositorySQLite(ILeadrepository):
    """Implementación usando SQLite crudo"""

    def __init__(self, db_path:str = "crm_local_raw.db"):
        self.db_path =db_path
        self._inicializar_db()

    def _inicializar_db(self):
        
        with sqlite3.connect(self.db_path) as conexion:
            cursor = conexion.cursor()    #es quien se encarga de ejecutar las querys
            try:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS leads (
                        id INTEGER  PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        empresa TEXT NOT NULL,
                        presupuesto REAL                         
                    )
                '''
                )
                conexion.commit()    # si no se ejecuta no se crea nada
            except:
                conexion.rollback()  #regresa al paso anterior donde si se ejecuto

    def guardar(self, lead: LeadEntity )-> None:
        with sqlite3.connect(self.db_path) as conexion:
            cursor = conexion.cursor()    #es quien se encarga de ejecutar las querys
            try:
                cursor.execute('''
                    INSERT INTO leads (nombre, empresa, presupuesto)
                    VALUES (?,?,?)
                '''
                , (lead.nombre, lead.empresa, lead.presupuesto)
                )

                conexion.commit()    # si no se ejecuta no se crea nada
            except:
                conexion.rollback()  #regresa al paso anterior donde si se ejecuto

    def obtener_todos(self) -> list[LeadEntity]:
        leads=[]
        
        with sqlite3.connect(self.db_path) as conexion:
            cursor = conexion.cursor()    #es quien se encarga de ejecutar las querys
            try:
                cursor.execute('''
                    SELECT nombre, empresa, presupuesto FROM leads
                '''
                )
                for fila in cursor.fetchall():   #es mala practic, pero cen la vida real usar #fetchmany()
                    leads.append(LeadEntity(nombre=fila[0],empresa=fila[1],presupuesto=fila[2]))
                return leads
            except:
                conexion.rollback()  #regresa al paso anterior donde si se ejecuto
            
class LeadRepositorySQLAlchemy(ILeadrepository):
    """Implementamos usando el ORM de SQLAlchemy"""

    def __init__(self, db_url: str ="sqlite:///crm_alchemy.db"):
        self.engine = create_engine(db_url,echo=False)
        Base.metadata.create_all(self.engine)

    def guardar(self, lead: LeadEntity) -> None:
        with Session(self.engine) as session:
            try: 
                session.add(lead)
                session.commit()
            except:
                session.rollback()
            finally: 
                session.close()

    def obtener_todos(self) -> list[LeadEntity]:
        with Session(self.engine) as session:
            try: 
                lista_datos = session.scalars(session.query(LeadEntity)).all()
                return lista_datos
            except:
                session.rollback()
                return []
            finally: 
                session.close()


class LeadService:
    """
    Este servicio coordina la logica. Depende de las interfaces.
    No depende de las implementaciones concretas
    Esto es el principio D en la metodologia SOLID
    """

    def __init__(self, repositorio: ILeadrepository):
        self.repositorio = repositorio

    def registrar_nuevo_lead(self, nombre:str, empresa:str, presupuesto:float):
        print(f"procesando registro para: {nombre}")

        if presupuesto < 0:
            print("Error: El presupuesto no puede ser negativo")
            return None
        nuevo_lead = LeadEntity(nombre = nombre,empresa = empresa,presupuesto=presupuesto)
        self.repositorio.guardar(nuevo_lead)
        print(f"Lead {nombre} guardado correctamete")

    def mostrar_reporte_leads(self):
        leads = self.repositorio.obtener_todos()

        for lead in leads:
            print(lead)

if __name__ == "__main__":
    repo_actual = LeadRepositorySQLAlchemy()
    repo_actual_1 = LeadRepositorySQLite()

    crm_service = LeadService(repo_actual_1)

    crm_service.registrar_nuevo_lead("Sara Connor", "Skynet Dynamics", 150000.0)
    crm_service.registrar_nuevo_lead("Bruce Wayne", "Wayne enterprise", 500000.0)
    crm_service.registrar_nuevo_lead("Homero Simpson", "Planta Nuclear", 15.0)

    crm_service.mostrar_reporte_leads()