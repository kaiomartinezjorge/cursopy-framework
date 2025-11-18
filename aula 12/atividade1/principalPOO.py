import triangulosPOO as tl

trianguloX = tl.triangulo() 
trianguloY = tl.triangulo()

print("Digite as medidas do triangulo X")
trianguloX.a = int(input("Digite a medida a: "))
trianguloX.b = int(input("Digite a medida b: "))
trianguloX.c = int(input("Digite a medida c: "))

print("Digite as medidas do triangulo Y")
trianguloY.a = int(input("Digite a medida a: "))
trianguloY.b = int(input("Digite a medida b: "))
trianguloY.c = int(input("Digite a medida c: "))

areax = trianguloX.area()

areay = trianguloY.area()

if areax > areay:
    saida = "A area do triangulo X é maior que a area do triangulo Y"
elif areay > areax:
    saida = "A area do triangulo Y é maior que a area do triangulo X"
else:
    saida = "As areas dos triangulos são iguais"

print(f"A area do triangulo X é igual a: {areax:.1f}")
print(f"A area do triangulo Y é igual a: {areay:.1f}")
print(f"{saida}")
