import httpx  # type: ignore
from app.models.deputado import Deputado

BASE_URL = "https://dadosabertos.camara.leg.br/api/v2"


async def get_deputados():
    url = f"{BASE_URL}/deputados"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json().get("dados", [])

        deputados = [Deputado(**d) for d in data]
        return deputados
