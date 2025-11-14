import produtoPOO as p

p1 = p.Produto()

p1.nome = input("\tNome: ")
p1.preco = float(input("\tpreco(R$): "))
p1.quantidade = int(input("\tQuantidade: "))

print("Dados do produto")
print(f"\tNome do produto: {p1.nome}")
print(f"Valor da compra: R$ {p1.preco:.2f}")
print(f"Quantidade em estoque: {p1.quantidade}")
print(f"Valor total em estoque: R$ {p1.valortotalemestoque():.2f}")
