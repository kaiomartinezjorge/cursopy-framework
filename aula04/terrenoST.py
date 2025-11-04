import streamlit as st

st.title("Problema Terreno")

st.write("Digite a largura do terreno (em metros): ")
largura = st.number_input("largura (m): ")
st.write("Digite o comprimento do terreno (em metros): ")
comprimento = st.number_input("comprimento (m): ")
st.write("Digite o valor do metro quadrado do terreno (em R$): ")
valor = st.number_input("valor (R$): ")

area = largura * comprimento
valorTotal = area * valor

st.write(f"A area do terreno é de {area:.2f} m²")
st.write(f"O preço do terreno é de R$ {valorTotal:.2f}")