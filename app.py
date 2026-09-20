import streamlit as st

st.set_page_config(page_title="Cianb", page_icon="✨")

st.title("Cianb")
st.write("Bem-vindo à página inicial do Cianb!")

nome = st.text_input("Como você se chama?")
if nome:
    st.success(f"Olá, {nome}! 👋")
