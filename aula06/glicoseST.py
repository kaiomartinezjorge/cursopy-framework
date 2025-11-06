import streamlit as st

st.title("Monitoramento de Glicose Sanguínea")
st.markdown(
"""
| Nível de glicose | Classificação  | 
| ---------------- | -------------- |
| 0 - 69 mg/dL     | Hipoglicemia   |
| 70 - 100 mg/dL   | Normal         |
| 101 - 140 mg/dL  | Pré-diabetes   |
| > 140 mg/dL      | Diabetes       |
""")

glicose = st.number_input("insira o nível de glicose sanguínea (mg/dL):", min_value=0)


if st.button("Verificar Nível de Glicose"):
    if 70 < glicose <= 100:
        st.success("Nível de glicose normal.")
    elif 100 < glicose <= 140:
        st.warning("Nível de glicose elevado.")
    elif glicose > 140:
        st.error("Nível de glicose muito alto!")
    else:
        st.error("Nível de glicose abaixo do normal.")