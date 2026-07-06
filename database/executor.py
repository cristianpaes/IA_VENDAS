import pandas as pd
from database.connection import DatabaseConnection


class SQLExecutor:

    def __init__(self):

        self.engine = DatabaseConnection().get_engine()

    def execute(self, query: str):

        return pd.read_sql(query, self.engine)