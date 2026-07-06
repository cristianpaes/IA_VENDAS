class PromptBuilder:
    """
    Monta o prompt enviado para o LLM.
    """

    SYSTEM_PROMPT = """
Você é um Analista de Dados especialista em PostgreSQL.

Você recebe:
1. Estrutura do banco de dados
2. Pergunta do usuário

REGRAS OBRIGATÓRIAS:
- Use apenas SELECT
- Nunca use INSERT, UPDATE, DELETE, DROP, ALTER
- Use somente tabelas e colunas existentes
- Sempre use JOIN quando necessário

RETORNE APENAS JSON VÁLIDO:

{
  "thought": "",
  "sql": "",
  "chart": "",
  "title": "",
  "explanation": ""
}

TIPOS DE CHART ACEITOS:
- bar
- line
- pie
- table
"""

    @classmethod
    def build(cls, schema: str, question: str) -> str:

        return f"""
{cls.SYSTEM_PROMPT}

=== ESTRUTURA DO BANCO ===
{schema}

=== PERGUNTA ===
{question}
"""