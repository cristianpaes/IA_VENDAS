class SQLGenerator:

    def __init__(self, client):
        self.client = client

    def generate(self, question: str, schema: str):

        prompt = f"""
Você é um especialista em PostgreSQL.

REGRAS:
- Use apenas PostgreSQL
- Nunca invente colunas
- Use apenas o schema abaixo

SCHEMA:
{schema}

PERGUNTA:
{question}

Responda apenas JSON:
{{"sql": "SELECT ..."}}
"""

        result = self.client.generate(prompt)

        sql = result["sql"]

        return {"sql": sql}