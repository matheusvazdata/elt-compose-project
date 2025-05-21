# 🐳 ELT Compose Project

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Engine-blue?logo=docker)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue?logo=postgresql)](https://www.postgresql.org/)
[![Makefile](https://img.shields.io/badge/Makefile-Automation-blue?logo=gnu)](https://www.gnu.org/software/make/)
[![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-yellow)](#)

---

Projeto de engenharia de dados com Python, Docker e PostgreSQL.  
Implementa uma pipeline **ELT (Extract, Load, Transform)** local e containerizada.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.11** – Extração e carga de dados
- **PostgreSQL 14** – Banco relacional como destino
- **Docker** – Empacotamento e isolamento
- **Docker Compose** – Orquestração local
- **Makefile** – Automação de build, run e limpeza

---

## 📦 Histórico de versões Docker

| Versão | Otimizações aplicadas                                      | Tamanho estimado |
|--------|-------------------------------------------------------------|------------------|
| `v1`   | Base `python:3.11`, sem otimizações, pip com cache          | ~1.04 GB         |
| `v2`   | Base `python:3.11-slim`, uso de `--no-cache-dir`, `.dockerignore` | ~400–600 MB      |
| `v3`   | Multi-stage build, apenas runtime final na imagem           | ~140 MB          |

> 🔜 Futuras versões: execução como user não-root (`v4`), base distroless, deploy com Airflow e FastAPI.

---

## 🛠️ Comandos úteis

### 🔧 Build da imagem Docker
```bash
make build VERSION=v1     # ou v2, v3...
````

### 🚀 Rodar a aplicação com Docker Compose

```bash
make run
```

### 📜 Listar imagens construídas

```bash
make list
```

### 🧼 Limpar containers e imagens antigas

```bash
make clean
```

## 📂 Estrutura do Projeto

```bash
elt-compose-project/
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── README.md
├── requirements.txt
├── main.py
├── extract/
│   └── api_client.py
├── load/
│   └── to_postgres.py
└── .dockerignore
```

## ✅ Próximos passos

* [ ] `v4`: execução como usuário não-root
* [ ] `v5`: base distroless + segurança reforçada
* [ ] Exposição via FastAPI
* [ ] Orquestração com Airflow + DAGs

---

**Feito por [@matheusvazdata](https://github.com/matheusvazdata)**