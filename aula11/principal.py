import streamlit as st
import numpy as np

lista_nome = []
lista_idade = []
lista_altura = []
pessoas = int(st.number_input("Quantas pessoas serão digitadas", min_value=0, step=1))

for i in range(pessoas):
    st.write(f"dados da {i + 1}a pessoa")
    nome = st.text_input("Nome: ")
    idade = st.number_input("Idade: ")
    altura = st.number_input("Altura (Em metros)")
    lista_nome.append(nome)
    lista_idade.append(idade)
    lista_altura.append(altura)
    
if st.button("Calcular"):

    altura_media = np.mean(altura)
    if idade < 16:
        menor16 =+ 1
        nome = nome
    percentual = (menor16 / pessoas) * 100

    st.write(f"A altura Média é {altura_media}")
    st.write(f"Pessoas com menos de 16 anos {percentual}%") 
    


