import streamlit as st

st.title("Sistema de login simples")
USUARIO = "Clodoaldo"
SENHA = "senha123"

usuario_entrada = st.text_input("Nome do usuário")
senha_entrada = st.text_input("Senha", type="password")

MAXIMO_TENTATIVAS = 3
if "tentativas" not in st.session_state:
    st.session_state.tentativas = 0

if st.button("Logar"):
    if st.session_state.tentativas >= MAXIMO_TENTATIVAS:
        st.error("Número máximo de tentativas excedido, acesso bloqueado.")

    else:
        while st.session_state.tentativas < MAXIMO_TENTATIVAS:
            if usuario_entrada == USUARIO and senha_entrada == SENHA:
                st.success("Login bem-sucedido!")
                st.session_state.tentativas = 0
                break
            else:
                st.session_state.tentativas += 1
                st.error(f"Login falhou! Tentativas restantes: {st.session_state.tentativas} de {MAXIMO_TENTATIVAS}")
                break
