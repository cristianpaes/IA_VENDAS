from sqlalchemy import inspect
from database.connection import DatabaseConnection


class DatabaseSchema:

    def __init__(self):
        self.engine = DatabaseConnection().get_engine()
        self.inspector = inspect(self.engine)

    def get_schema(self):

        schema = ""

        for table in self.inspector.get_table_names():

            columns = self.inspector.get_columns(table)

            cols = ", ".join([c["name"] for c in columns])

            schema += f"Tabela {table}: {cols}\n"

        return schema