from abc import ABC, abstractmethod 
from models import Persona, Lead, Vendedor

class IRepositorioPipeline(ABC):  #interaz
    @abstractmethod
    def guardar_en_campana(self, persona:Persona) -> None:
        pass


class PipelineRepositoryMemoria(IRepositorioPipeline):
    def __init__(self):
        self._db_campana = []

    def guardar_en_campana(self,persona:Persona):
        self._db_campana.append(persona)
        print(f"Persona {persona.get_full_name()} agreagada al pipeline")

    def obtener_datos(self) -> list:
        return self._db_campana
    

class PipelineService:
    """
    Este servicio coordina la logica. Depende de las interfaces.
    No depende de las implementaciones concretas
    Esto es el principio D en la metodologia SOLID
    """

    def __init__(self, repositorio: IRepositorioPipeline):
        self.repositorio = repositorio

    def agregar_a_campana(self, persona: Persona):

        if isinstance(persona, Lead):
            if persona.presupuesto_estimado <= 0:
                print("El Lead no tiene presupuesto suficiente.")
                return False

        self.repositorio.guardar_en_campana(persona)
        print("Persona agregada correctamente a la campaña.")
        return True


        