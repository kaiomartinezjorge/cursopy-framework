import streamlit as st

st.title("Verificação de triangulo  e trapezio com calculo de perimetro ou area")

opcao = st.radio("Escolha a operação que deseja:", ("perimetro_Triângulo", "area_Trapézio"))


if opcao == "perimetro_Triângulo":
    st.write("Cálculo do perímetro do triângulo")
    a = st.number_input("Digite o valor do lado 1:", min_value=0.1)
    b = st.number_input("Digite o valor do lado 2:", min_value=0.1)
    c = st.number_input("Digite o valor do lado 3:", min_value=0.1)

    if st.button("Calcular"):
        if (a < b + c) and (b < a + c) and (c < a + b):
            perimetro = a + b + c
            st.write("O triângulo é válido")
            st.write(f"O perímetro do triângulo é: {perimetro}")
        else:
            st.error("O triângulo não é válido")
    
else:
    st.write("Cálculo da área do trapézio")  
    a = st.number_input("Digite o valor da base 1:", min_value=0.1)
    b = st.number_input("Digite o valor da base 2:", min_value=0.1)
    c = st.number_input("Digite o valor da altura:", min_value=0.1)

    if st.button("Calcular"):
        if a == b:
            st.error("As bases não podem ser iguais para um trapézio.")
        else:
            area = ((a + b) * c) / 2
            st.write(f"A área do trapézio é: {area}")
