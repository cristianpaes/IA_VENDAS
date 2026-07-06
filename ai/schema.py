from database.schema import DatabaseSchema


class SchemaService:

    def __init__(self):
        self.db = DatabaseSchema()

    def get(self, question: str):

        schema = self.db.get_schema()

        schema += """

REGRA IMPORTANTE:
- Use APENAS tabelas do schema acima
- NUNCA invente views (ex: vw_vendas_analiticas)
- dim_tempo.dia é a única coluna de data
"""

        return schema