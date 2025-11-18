import produtoPOO as p

p1 = p.Produto()

p1.nome = input("\tNome: ")
p1.preco = float(input("\tpreco(R$): "))
p1.quantidade = int(input("\tQuantidade: "))

print(p1.dadosdoproduto())

q = int(input("Digite o número de produtos a ser adicionado ao estoque: "))
p1.adicionarprodutos(q)

print("--Dados atualizado--")
print(p1.dadosdoproduto())

q = int(input("Digite o número de produtos a ser removido ao estoque: "))
p1.removerprodutos(q)

print("--Dados atualizado--")
print(p1.dadosdoproduto())