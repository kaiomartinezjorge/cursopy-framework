import produtoPOO as p

print("Entre com os dados do produto")
nome = input("Nome: ")
quantidade = float(input("Quantidade: "))
preco = float(input("Preço: "))

ps = p.Produto(nome, preco, quantidade)

print(ps.dadosdoproduto())