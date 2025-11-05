import streamlit as st
import math as mt

TITULO = "Cálculo da Área de um Quadrado, Triângulo e Trapézio"
st.markdown(f"<h1 style='text-align: center;'>{TITULO}</h1>", unsafe_allow_html=True)

medidaA = st.number_input("Digite a medida A (em metros):", min_value=0.0)
medidaB = st.number_input("Digite a medida B (em metros):", min_value=0.0)
medidaC = st.number_input("Digite a medida C (em metros):", min_value=0.0)

area_quadrado = mt.pow(medidaA, 2)
area_triangulo = (medidaA * medidaB) / 2
area_trapezio = ((medidaA + medidaB) * medidaC) / 2

st.markdown(f"<h2 style='text-align: center;'>Resultados</h2>", unsafe_allow_html=True)
st.write(f"A área do quadrado é {area_quadrado:.4f}")
st.write(f"A área do triângulo é {area_triangulo:.4f}")
st.write(f"A área do trapézio é {area_trapezio:.4f}")