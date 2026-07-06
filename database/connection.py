import os
from sqlalchemy import create_engine

# ---------------------------------------------------
# Detecta automaticamente Streamlit Cloud ou Local
# ---------------------------------------------------

try:
    import streamlit as st

    if hasattr(st, "secrets") and "DB_HOST" in st.secrets:

        DB_HOST = st.secrets["DB_HOST"]
        DB_NAME = st.secrets["DB_NAME"]
        DB_USER = st.secrets["DB_USER"]
        DB_PASSWORD = st.secrets["DB_PASSWORD"]
        DB_PORT = st.secrets["DB_PORT"]
        DB_SSLMODE = st.secrets["DB_SSLMODE"]

    else:
        raise Exception()

except:

    from dotenv import load_dotenv

    load_dotenv()

    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_PORT = os.getenv("DB_PORT")
    DB_SSLMODE = os.getenv("DB_SSLMODE", "require")


DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    f"?sslmode={DB_SSLMODE}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
)

def get_engine():
    return engine