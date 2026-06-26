# plataforma-analise-dados-edap
Plataforma corporativa de análise de dados com ETL, qualidade de dados, dashboards e exportação de relatórios (PDF, Excel, CSV, JSON e HTML).

# EDAP - Plataforma de Análise de Dados

Sistema corporativo de análise de dados com pipeline ETL, qualidade de dados, dashboards e exportação de relatórios.

---

## 🚀 Funcionalidades

- Ingestão de dados (CSV, Excel, JSON)
- Pipeline ETL
- Análise de qualidade de dados
- Dashboard analítico
- Exportação de relatórios

---

## 📤 Exportações

- PDF Executivo
- Excel (.xlsx)
- CSV
- JSON
- HTML Responsivo

---

## 🧠 Arquitetura

- Backend: Python + FastAPI
- Processamento: Pandas / Polars
- Exportação: ReportLab / OpenPyXL / Jinja2
- API REST

---

## ▶️ Execução

```bash
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
