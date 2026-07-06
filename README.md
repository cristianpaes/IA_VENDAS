# 🚀 DataMind AI — Chat Inteligente com Banco de Dados usando IA Generativa

🌐 Acesse o projeto em produção: https://iavendas.streamlit.app/  
📦 Repositório: https://github.com/cristianpaes/IA_VENDAS  

---

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_AI-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-lightgrey)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-orange)

</p>

---

# 💡 Visão Geral do Projeto

O **DataMind AI** é um sistema inteligente que permite consultar bancos de dados utilizando **linguagem natural**, eliminando a necessidade de escrever SQL manualmente.

A aplicação interpreta perguntas de negócio, gera consultas SQL automaticamente, executa no banco de dados e retorna:

- 📊 Dados estruturados
- ⚡ SQL gerado pela IA
- 📈 Gráficos interativos
- 🧠 Explicações em linguagem natural

---

# 🎯 Problema que o projeto resolve

Empresas possuem grandes volumes de dados, mas a análise depende de profissionais técnicos.

Isso gera:

- Dependência de analistas para perguntas simples
- Tempo elevado para respostas
- Barreiras entre negócio e dados

### 💥 Solução

O DataMind AI permite que qualquer usuário pergunte:

> "Qual vendedor vendeu mais em 2025?"

E receba instantaneamente:

- SQL gerado automaticamente
- Resultado da consulta
- Visualização gráfica
- Explicação em linguagem natural

---

# 🧠 Arquitetura da Solução

```text
Usuário
   │
   ▼
Streamlit (Interface Web)
   │
   ▼
AI Engine (Orquestrador Central)
   │
   ├── Gemini AI (Geração de SQL)
   ├── SQL Generator
   ├── SQL Validator (Segurança)
   ├── SQL Guard (Proteção contra queries perigosas)
   ├── Result Analyzer (IA explicativa)
   │
   ▼
Camada de Dados
   ├── PostgreSQL
   ├── SQLAlchemy
   ├── Executor de Queries
   │
   ▼
Camada de Output
   ├── Pandas DataFrame
   ├── Plotly (Visualização)
   ├── Insights gerados por IA

⚙️ Tecnologias Utilizadas
Python 3.12
Streamlit
Google Gemini AI
PostgreSQL
SQLAlchemy
Pandas
Plotly
python-dotenv
