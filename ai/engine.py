import time

from ai.client import AIClient
from ai.sql_generator import SQLGenerator
from ai.sql_validator import SQLValidator
from ai.schema import SchemaService
from ai.sql_guard import SQLGuard
from database.executor import SQLExecutor


class AIEngine:

    def __init__(self):

        self.client = AIClient()
        self.generator = SQLGenerator(self.client)
        self.validator = SQLValidator()
        self.schema = SchemaService()
        self.executor = SQLExecutor()

    def ask(self, question: str):

        start = time.time()

        try:

            # =========================
            # 1. SCHEMA
            # =========================
            schema = self.schema.get(question)

            # =========================
            # 2. SQL GERADO
            # =========================
            result = self.generator.generate(question, schema)
            sql = result["sql"]

            # =========================
            # 3. VALIDAÇÃO BÁSICA
            # =========================
            self.validator.validate(sql)

            # =========================
            # 4. GUARD DE SEGURANÇA (NOVO)
            # =========================
            guard = SQLGuard(schema)
            guard.validate(sql)

            # =========================
            # 5. EXECUÇÃO
            # =========================
            df = self.executor.execute(sql)

            # =========================
            # 6. RESPOSTA FINAL
            # =========================
            return {
                "success": True,
                "question": question,
                "sql": sql,
                "data": df,
                "rows": len(df),
                "columns": list(df.columns),
                "preview": df.head(10),
                "time": round(time.time() - start, 2)
            }

        except Exception as e:

            return {
                "success": False,
                "question": question,
                "error": str(e)
            }