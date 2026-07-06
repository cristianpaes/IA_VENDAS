class SQLGuard:

    def __init__(self, schema_text: str):
        self.allowed_tables = self._extract_tables(schema_text)

    def _extract_tables(self, schema_text: str):

        tables = set()

        for line in schema_text.split("\n"):

            line = line.strip()

            if line.startswith("Tabela"):

                table = line.replace("Tabela", "").split(":")[0].strip()
                tables.add(table)

        return tables

    # 🔥 ESTE MÉTODO TEM QUE EXISTIR
    def validate(self, sql: str):

        sql_lower = sql.lower()

        for table in self.allowed_tables:

            if table.lower() in sql_lower:
                return True

        raise ValueError(
            f"SQL usa tabela inexistente no schema:\n{sql}"
        )