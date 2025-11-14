import calculadora as c

circulo = c.calculadora()

raio = float(input("Digite o valor do raio: "))

circunferencia = circulo.circunferencia(raio)
area = circulo.area(raio)

print(f"""
    Circunferencia = {circunferencia:.2f}
    Area = {area:.2f}
    PI = {circulo.PI:.2f}
""")