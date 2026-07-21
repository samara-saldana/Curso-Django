from crm_pipeline import PipelineService, PipelineRepositoryMemoria
from models import Lead
import pytest

@pytest.fixture
def servicio_pipeline():

    repo_pipeline = PipelineRepositoryMemoria()
    return PipelineService(repo_pipeline)


def test_agregar_lead_exitoso(servicio_pipeline):

    lead=Lead("Juan", "Perez", "juan@ejemplo.com", 2500)
    pipeline = servicio_pipeline.agregar_a_campana(lead)
    assert pipeline == True

def test_rechazar_lead_sin_presupuesto(servicio_pipeline):
    lead=Lead("Juan", "Perez", "juan@ejemplo.com", -500)
    pipeline = servicio_pipeline.agregar_a_campana(lead)
    assert pipeline == False

