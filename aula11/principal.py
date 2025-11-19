import streamlit as st
import numpy as np

lista_nome = []
lista_idade = []
lista_altura = []

pessoas = int(st.number_input("Quantas pessoas serão digitadas", min_value=0, step=1))

for i in range(pessoas):
    st.write(f"Dados da {i + 1}ª pessoa")
    nome = st.text_input(f"Nome {i+1}: ")
    idade = st.number_input(f"Idade {i+1}: ", min_value=0, step=1)
    altura = st.number_input(f"Altura (m) {i+1}: ", min_value=0.0, step=0.01)

    lista_nome.append(nome)
    lista_idade.append(idade)
    lista_altura.append(altura)

if st.button("Calcular"):

    if len(lista_altura) > 0:
        altura_media = np.mean(lista_altura)
    else:
        altura_media = 0

    menor16 = sum(1 for idade in lista_idade if idade < 16)

    percentual = (menor16 / pessoas * 100) if pessoas > 0 else 0

    st.write(f"Altura média: {altura_media:.2f} m")
    st.write(f"Pessoas com menos de 16 anos: {percentual:.1f}%")

    


