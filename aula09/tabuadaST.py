import streamlit as st

st.title("Tabuada")
st.set_page_config("Tabuada")
n = None
try:
    n = int(st.text_input("Deseja a tabuada de qual numero: "))
    for i in range(1, 11):
        saida = f"{n} x {i} = {n * i}"
        st.markdown(f"""{saida}""")
except ValueError:
    if n is None:
        st.warning("Digite apenas números")
    else:
        st.error("Digite apenas números inteiros.")
