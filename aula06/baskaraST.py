import streamlit as st
import math as mt

st.header("Calculadora de Bhaskara")
st.write("Calculadora de raízes de uma \n de" \
"uma equação do segundo grau")
st.write("ax² + bx + c = 0")

a = st.text_input("Insira o valor de a:")
b = st.text_input("Insira o valor de b:")
c = st.text_input("Insira o valor de c:")

if st.button("Calcular raízes"):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        delta = b**2 - 4 * a * c
        st.write(f"O valor de Δ é: {delta}")
        if delta < 0:
            st.warning("A equação não possui raízes reais.")
        elif delta == 0:
            raiz = -b / (2 * a)
        else:
            raiz1 = (-b + mt.sqrt(delta)) / (2 * a)
            raiz2 = (-b - mt.sqrt(delta)) / (2 * a)
            st.write(f"A equação possui duas raízes reais: x1 =  {raiz1} e x2 =  {raiz2}")

    except ValueError:
        st.error("Por favor, insira valores válidos.")