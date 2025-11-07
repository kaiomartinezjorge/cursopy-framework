import streamlit as st

def celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_celsius(kelvin):
    return kelvin - 273.15

def kelvin_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

st.sidebar.title(" Conversor de Temperatura ")
st.title(" Conversor de Temperatura ")
st.sidebar.markdown("""
Este aplicativo converte temperaturas entre Celsius, Fahrenheit e Kelvin.
""")

opcao_selecionada = st.sidebar.radio("Selecione a escala de temperatura", options=["Celsius", "Fahrenheit", "Kelvin"], key="opcao_radio")

temp = st.number_input("Valor da temperatura", format="%.2f", step=1.0)



if st.button("Converter", icon="🌡"):
    if opcao_selecionada == "Celsius":
        st.write(f"Temperatura em Celsius: {temp:.2f} °C")
        st.write(f"Temperatura em Fahrenheit: {celsius_fahrenheit(temp):.2f} °F")
        st.write(f"Temperatura em Kelvin: {celsius_kelvin(temp):.2f} K")
    elif opcao_selecionada == "Fahrenheit":
        st.write(f"Temperatura em Fahrenheit: {temp:.2f} °F")
        st.write(f"Temperatura em Celsius: {fahrenheit_celsius(temp):.2f} °C")
        st.write(f"Temperatura em Kelvin: {fahrenheit_kelvin(temp):.2f} K")
    else:
        st.write(f"Temperatura em Kelvin: {temp:.2f} K")
        st.write(f"Temperatura em Celsius: {kelvin_celsius(temp):.2f} °C")
        st.write(f"Temperatura em Fahrenheit: {kelvin_fahrenheit(temp):.2f} °F")
