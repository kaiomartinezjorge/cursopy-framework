import streamlit as st
from produtod import pessoas, funcionarios




col1, col2 = st.columns(2)

with col1:


    st.header("Função 1: Pessoa mais velha")
    if st.button("Calcular a pessoa mais velha"):

        with st.form(key="formulario1"):


            nome1 = st.text_input("Insira o nome da pessoa 1")
            idade1 = st.number_input("Insira a idade da pessoa 1", min_value=1, step=1)

            nome2 = st.text_input("Insira o nome da pessoa 2")
            idade2 = st.number_input("Insira a idade da pessoa 2", min_value=1, step=1)

            p1 = pessoas(nome1, idade1)
            p2 = pessoas(nome2, idade2)
            if st.form_submit_button("Calcular"):
                st.write(p1.mais_velha(p2))


with col2:

    st.header("Função 2: Salario médio dos funcionarios")

    if st.button("Calcular a media salarial"):

        with st.form(key="formulario1"):

            funcionario1 = st.text_input("Insira o nome do funcionario 1: ")
            salario1 = st.number_input("Digite o salario do funcionario 1: ")

            funcionario2 = st.text_input("Insira o nome do funcionario 2: ")
            salario2 = st.number_input("Digite o salario do funcionario 2: ")

            f1 = funcionarios(funcionario1, salario1)
            f2 = funcionarios(funcionario2, salario2)

            if st.form_submit_button("Calcular"):
                st.write(f1.salario_medio(f2))

