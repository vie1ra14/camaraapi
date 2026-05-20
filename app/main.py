from fastapi import FastAPI
from app.routes import deputados
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API Pública - Dados Abertos da Câmara dos Deputados")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://camara-api.vercel.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(deputados.router)
