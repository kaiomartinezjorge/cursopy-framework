import streamlit as st
st.title("🎯 Simulação de lançamentos de dardos 🎯")
'''Simulação de lançamento de tres dardos: o objetivo do aplicativo é
mostrar o dardo com a maior distancia'''
# entrada de dados

st.header("Inserir as tres distancias dos dardos lançados pelo jogador")
coluna1, coluna2, coluna3 = st.columns(3)
with coluna1:
    dardo1 = st.number_input("Distância do 1° dardo", min_value=0.0)
with coluna2:
    dardo2 = st.number_input("Distância do 2° dardo", min_value=0.0)
with coluna3:
    dardo3 = st.number_input("Distância do 3° dardo", min_value=0.0)

if (dardo1 > dardo2) and (dardo1 > dardo3):
    dardo_vencedor = "dardo1"
elif (dardo2 > dardo1) and (dardo2 > dardo3):
    dardo_vencedor = "dardo2"
else:
    dardo_vencedor = "dardo3"

if st.button("Apresentar resultados de lançamento"):
    st.write(f"O dardo com a maior distancia foi: {dardo_vencedor}")


