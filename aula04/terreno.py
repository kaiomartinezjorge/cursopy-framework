import os

os.system("cls")

largura=float(input("Digite a largura do terreno (em metros): "))
comprimento=float(input("Digite o comprimento do terreno (em metros): "))
valor=float(input("Digite o valor do metro quadrado do terreno (em R$): "))

area=largura*comprimento
valorTotal=area*valor

print(f"A area do terreno é de {area:.2f} m²")
print(f"O preço do terreno é de R$ {valorTotal:.2f}")