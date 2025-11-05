import streamlit as st
import math as mt

TITULO = "Cálculo de Área, Perímetro e Diagonal de um Retângulo"
st.title(TITULO)

altura = st.number_input("Digite a altura do retangulo (em metros):", min_value=0.0)
base = st.number_input("Digite a base do retangulo (em metros):", min_value=0.0)

area = altura * base
perimetro = 2 * altura + 2 * base
x = mt.pow(base, 2) + mt.pow(altura, 2)
diagonal = mt.sqrt(x)

st.write(f"A área do retângulo é {area:.2f} m²")
st.write(f"O perímetro do retângulo é {perimetro:.2f} m")
st.write(f"A diagonal do retângulo é {diagonal:.2f} m")
