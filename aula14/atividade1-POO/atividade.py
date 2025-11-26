import streamlit as st
from produtod import pessoas, funcionarios

col1, col2 = st.columns(2)

# COLUNA 1 -------------------------------------------------
with col1:

    st.header("Função 1: Pessoa mais velha")

    with st.form(key="form_pessoa"):
        nome1 = st.text_input("Insira o nome da pessoa 1")
        idade1 = st.number_input("Insira a idade da pessoa 1", min_value=1, step=1)

        nome2 = st.text_input("Insira o nome da pessoa 2")
        idade2 = st.number_input("Insira a idade da pessoa 2", min_value=1, step=1)

        submit = st.form_submit_button("Calcular")

        if submit:
            p1 = pessoas(nome1, idade1)
            p2 = pessoas(nome2, idade2)
            st.write(p1.mais_velha(p2))



# COLUNA 2 -------------------------------------------------
with col2:

    st.header("Função 2: Salário médio dos funcionários")

    with st.form(key="form_func"):
        funcionario1 = st.text_input("Insira o nome do funcionário 1: ")
        salario1 = st.number_input("Digite o salário do funcionário 1: ")

        funcionario2 = st.text_input("Insira o nome do funcionário 2: ")
        salario2 = st.number_input("Digite o salário do funcionário 2: ")

        submit2 = st.form_submit_button("Calcular")

        if submit2:
            f1 = funcionarios(funcionario1, salario1)
            f2 = funcionarios(funcionario2, salario2)
            st.write(f1.salario_medio(f2))

