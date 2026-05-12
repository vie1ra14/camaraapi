from fastapi import APIRouter
from typing import List
from app.models.deputado import Deputado
from app.services.camara import get_deputados

router = APIRouter(prefix="", tags=["Deputados"])


@router.get("/deputados", response_model=List[Deputado], summary="Lista de Deputados",
            description="Retorna uma lista de deputados federais.")
async def listar_deputados(uf: str = None, partido: str = None):
    """
    Retorna uma lista de deputados federais.

    - **id**: Identificador do deputado
    - **nome**: Nome completo do deputado
    - **partido**: Partido político do deputado
    - **uf**: Unidade federativa do deputado
    """
    data = await get_deputados()
    if uf:
        data = [d for d in data if d.siglaUf == uf]
    if partido:
        data = [d for d in data if d.siglaPartido == partido]

    print(data)
    return data


@router.get("/resumo")
async def resumo():
    data = await get_deputados()

    total = len(data)

    por_estado = {}
    for d in data:
        uf = d.siglaUf
        por_estado[uf] = por_estado.get(uf, 0) + 1

    return {
        "total_deputados": total,
        "por_estado": por_estado
    }
