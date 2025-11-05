import streamlit as st

st.title("Calculadora de Troco")

valorUn = st.number_input("Insira o valor unitario do produto:", min_value=0.0, step=0.01,)
quantidade = st.number_input("Insira a quantidade comprada:", min_value=0, step=1,)

valorTotal = valorUn * quantidade

valorPago = st.number_input("Insira o valor pago:", min_value=valorTotal, step=0.01,)

troco = valorPago - valorTotal

st.write(f"Valor Unitario do produto: R$ {valorUn:.2f}")
st.write(f"Quantidade comprada: {quantidade}")
st.write(f"Dinheiro recebido: R$ {valorPago:.2f}")
st.write(f"Valor Total: R$ {valorTotal:.2f}")
st.write(f"Troco: R$ {troco:.2f}")