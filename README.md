# 🚀 Dados de vendas com AI — Inteligência de Dados com IA Generativa

🌐 Live App: https://iavendas.streamlit.app/

# 🚀 Dados de vendas com AI — Chat Inteligente com Banco de Dados usando IA Generativa <p align="center"> ![Python](https://img.shields.io/badge/Python-3.12-blue) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-App-red) ![Gemini](https://img.shields.io/badge/Google-Gemini_AI-green) ![Plotly](https://img.shields.io/badge/Plotly-Interactive-orange) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-lightgrey) </p> --- # 💡 Visão Geral O **DataMind AI** é uma aplicação desenvolvida para transformar perguntas em linguagem natural em consultas SQL inteligentes, executando consultas diretamente em um banco PostgreSQL e retornando: - SQL gerado automaticamente - Dados encontrados - Gráficos interativos - Explicação dos resultados em linguagem natural O objetivo é permitir que usuários de negócio consultem grandes volumes de dados sem precisar conhecer SQL. --- # 🎯 Problema Resolvido Muitas empresas possuem milhares de informações armazenadas em bancos de dados, porém dependem de analistas para responder perguntas simples como: - Qual vendedor vendeu mais? - Qual produto teve maior faturamento? - Como estão as vendas por região? - Qual cliente mais compra? - Qual foi o faturamento do último trimestre? O DataMind AI elimina essa barreira utilizando Inteligência Artificial para gerar consultas SQL automaticamente. --- # 🧠 Arquitetura
text
Usuário
     │
     ▼
Streamlit
     │
     ▼
AI Engine
     │
     ├────────► Gemini AI
     │
     ▼
SQL Generator
     │
     ▼
SQL Validator
     │
     ▼
PostgreSQL
     │
     ▼
DataFrame
     │
     ├────────► Plotly
     │
     ▼
Análise Inteligente
--- # ⚙️ Tecnologias - Python - Google Gemini AI - PostgreSQL - SQLAlchemy - Pandas - Plotly - Streamlit - Python Dotenv --- # 🧩 Principais Recursos ✅ Perguntas em linguagem natural ✅ Geração automática de SQL ✅ Execução segura das consultas ✅ Validação de SQL ✅ Gráficos automáticos ✅ Histórico das perguntas ✅ Explicação dos resultados utilizando IA ✅ Arquitetura modular --- # 📊 Exemplo Pergunta:
text
Qual vendedor vendeu mais em 2025?
SQL gerado automaticamente:
sql
SELECT
    vendedor,
    SUM(valor_total) AS faturamento
FROM fato_vendas
GROUP BY vendedor
ORDER BY faturamento DESC
LIMIT 1;
Resultado:
Carlos Souza
R$ 1.248.350,00
Gráfico: 📈 Barra Resumo: > Carlos Souza foi o vendedor com maior faturamento em 2025. --- # 📁 Estrutura do Projeto
IA_STREAMLIT/

│
├── ai/
│   ├── engine.py
│   ├── client.py
│   ├── sql_generator.py
│   ├── sql_validator.py
│   ├── result_analyzer.py
│   ├── chart_generator.py
│
├── database/
│   ├── connection.py
│   ├── executor.py
│   ├── schema.py
│
├── app.py
├── requirements.txt
└── README.md
--- # 🚀 Como executar Clone o projeto
bash
git clone https://github.com/SEU_USUARIO/DataMind-AI.git
Instale as dependências
bash
pip install -r requirements.txt
Configure o arquivo .env
env
DATABASE_URL=

GEMINI_API_KEY=
Execute
bash
streamlit run app.py
--- --- # 📚 Conhecimentos Aplicados - Engenharia de Dados - Inteligência Artificial Generativa - Prompt Engineering - SQL Avançado - PostgreSQL - Desenvolvimento Backend - Arquitetura de Software - ETL - Business Intelligence - Data Visualization --- # 👨‍💻 Sobre o Projeto Este projeto foi desenvolvido como estudo avançado em Engenharia de Dados, Inteligência Artificial Generativa e Business Intelligence, simulando um assistente corporativo capaz de consultar bancos de dados através de linguagem natural. Além do aspecto técnico, o objetivo foi explorar boas práticas de arquitetura, modularização, integração com modelos de IA e experiência do usuário. --- # 📬 Contato Caso tenha interesse em conversar sobre o projeto ou oportunidades na área de Dados, BI, IA ou Desenvolvimento Backend, fique à vontade para entrar em contato. LinkedIn: https://www.linkedin.com/in/cristian-camargo/
