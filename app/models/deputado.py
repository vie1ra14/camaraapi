from pydantic import BaseModel


class Deputado(BaseModel):
    id: int
    nome: str
    siglaPartido: str
    siglaUf: str
    urlFoto: str
    email: str
