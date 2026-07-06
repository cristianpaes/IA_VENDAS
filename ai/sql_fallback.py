class SQLFallback:

    def simple_query(self):

        return {
            "sql": """
            SELECT *
            FROM fato_vendas
            LIMIT 10;
            """
        }

    def error_query(self, question: str):

        return {
            "sql": f"""
            SELECT 'IA indisponível' as status,
                   '{question}' as pergunta;
            """
        }