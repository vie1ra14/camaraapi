# 📊 API Pública - Dados Abertos da Câmara dos Deputados

Este projeto é uma aplicação fullstack simples que consome dados públicos da Câmara dos Deputados do Brasil, utilizando uma API construída com FastAPI e um frontend em HTML + JavaScript.

---

## 🚀 Tecnologias utilizadas

### Backend
- Python
- FastAPI
- Uvicorn

### Frontend
- HTML5
- JavaScript (Fetch API)

---

## 📌 Funcionalidades

- Listagem de deputados federais
- Filtro por UF (opcional)
- Filtro por partido (opcional)
- Exibição de dados em cards
- Endpoint de resumo
- Consumo da API via frontend simples

---

## 📡 Endpoints da API

### 🔹 Listar deputados

GET /deputados


Parâmetros opcionais:
- `uf` → sigla do estado (ex: SP, RJ, DF)
- `partido` → sigla do partido (ex: PT, PL)

Exemplo:

/deputados?uf=SP&partido=PT


---

### 🔹 Resumo

GET /resumo


Retorna informações gerais da base de dados.
