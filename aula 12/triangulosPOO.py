class triangulo:
    # Atributos
    a: int
    b: int
    c: int
    a = 0
    b = 0
    c = 0

    def area(a, b, c):
        p = ((a + b + c) / 2)
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
