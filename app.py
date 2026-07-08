import streamlit as st
from ai.engine import AIEngine
import plotly.express as px

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Dados de vendas AI Chat",
    layout="wide"
)

engine = AIEngine()

# =========================
# INIT CHAT HISTORY
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# HEADER
# =========================
st.title("💬 Dados de vendas com AI - Chat de Dados + Gráficos")

# =========================
# INPUT
# =========================
question = st.chat_input("Pergunte sobre seus dados...")

# =========================
# PROCESSA PERGUNTA
# =========================
if question:

    response = engine.ask(question)

    st.session_state.messages.append(response)

# =========================
# EXIBE CHAT
# =========================
for msg in st.session_state.messages:

    if msg.get("error"):
        st.error(f"❌ {msg['question']} → {msg['error']}")
        continue

    st.markdown(f"### ❓ {msg['question']}")
    st.code(msg["sql"], language="sql")
    st.dataframe(msg["data"])

    # =========================
    # GRÁFICO AUTOMÁTICO
    # =========================
    df = msg["data"]

    if len(df.columns) >= 2:

        col1 = df.columns[0]
        col2 = df.columns[1]

        try:
            fig = px.bar(df, x=col1, y=col2, title="📊 Gráfico automático")
            st.plotly_chart(fig, use_container_width=True)
        except:
            pass

    st.divider()