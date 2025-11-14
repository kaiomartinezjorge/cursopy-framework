from calculadora import calculadora1

raio = float(input("Digite o valor do raio: "))

circunferencia = calculadora1.circunferencia(raio)
area = calculadora1.area(raio)

print("""
    Circunferencia: {circunferencia:.2f}
    Area: {area:.2f}
    PI: {PI}
""")