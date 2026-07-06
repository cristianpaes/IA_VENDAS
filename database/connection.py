from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()


class DatabaseConnection:
    def __init__(self):
        host = os.getenv("DB_HOST")
        database = os.getenv("DB_NAME")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        port = os.getenv("DB_PORT")
        sslmode = os.getenv("DB_SSLMODE", "require")

        connection_string = (
            f"postgresql+psycopg2://{user}:{password}"
            f"@{host}:{port}/{database}"
            f"?sslmode={sslmode}"
        )

        self.engine = create_engine(connection_string, pool_pre_ping=True)

    def get_engine(self):
        return self.engine