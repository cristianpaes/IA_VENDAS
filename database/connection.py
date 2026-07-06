from sqlalchemy import create_engine
import os


class DatabaseConnection:
    def __init__(self):

        # ---------------------------------------------
        # STREAMLIT CLOUD
        # ---------------------------------------------
        try:
            import streamlit as st

            if "DB_HOST" in st.secrets:

                host = st.secrets["DB_HOST"]
                database = st.secrets["DB_NAME"]
                user = st.secrets["DB_USER"]
                password = st.secrets["DB_PASSWORD"]
                port = st.secrets["DB_PORT"]
                sslmode = st.secrets.get("DB_SSLMODE", "require")

            else:
                raise Exception

        # ---------------------------------------------
        # LOCAL (.env)
        # ---------------------------------------------
        except Exception:

            from dotenv import load_dotenv

            load_dotenv()

            host = os.getenv("DB_HOST")
            database = os.getenv("DB_NAME")
            user = os.getenv("DB_USER")
            password = os.getenv("DB_PASSWORD")
            port = os.getenv("DB_PORT")
            sslmode = os.getenv("DB_SSLMODE", "require")

        # ---------------------------------------------
        # STRING DE CONEXÃO
        # ---------------------------------------------
        connection_string = (
            f"postgresql+psycopg2://{user}:{password}"
            f"@{host}:{port}/{database}"
            f"?sslmode={sslmode}"
        )

        self.engine = create_engine(
            connection_string,
            pool_pre_ping=True,
            pool_recycle=300,
            pool_size=5,
            max_overflow=10,
        )

    def get_engine(self):
        return self.engine