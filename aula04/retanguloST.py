import streamlit as st

st.title("Retangulo ST")

altura = st.number_input("Digite a altura do retangulo (em metros): ")
base = st.number_input("Digite a base do retangulo (em metros): ")

area = altura * base
perimetro = 2 * altura + 2 * base
diagonal = (altura**2 + base**2) ** 0.5

st.write(f"A área do retângulo é {area:.2f} m²")
st.write(f"O perímetro do retângulo é {perimetro:.2f} m")
st.write(f"A diagonal do retângulo é {diagonal:.2f} m")
