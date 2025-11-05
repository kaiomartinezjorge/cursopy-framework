import streamlit as st
TITULO = "Calculadora de Duração de tempo"
st.set_page_config(page_title=TITULO)

st.title(TITULO)

tempo = st.number_input("Insira o tempo em segundos:", min_value=0, step=1,
help="Digite o tempo total em segundos para converter em horas, minutos e segundos.")

horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60

st.write(f"{horas} Horas , {minutos} Minutos , {segundos} Segundos")
