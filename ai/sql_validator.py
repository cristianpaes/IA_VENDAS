class SQLValidator:

    def validate(self, sql: str):

        forbidden = [
            "DROP",
            "DELETE",
            "UPDATE",
            "INSERT",
            "ALTER"
        ]

        for f in forbidden:
            if f in sql.upper():
                raise ValueError(f"SQL bloqueado: {f}")

        return True