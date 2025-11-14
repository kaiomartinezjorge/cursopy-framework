class Produto:
    nome:str
    preco:float
    quantidade:int
    saida:str
    #metodos
    def valortotalemestoque(self) -> float:
        return self.preco * self.quantidade
    
    def adicionarprodutos(self, quantidade) -> int:
         self.quantidade =  self.quantidade + quantidade 
         return self.quantidade

    def removerprodutos(self, quantidade) -> int:
        self.quantidade = self.quantidade - quantidade

    def dadosdoproduto(self) -> str:
        saida = f"""
            \tDados do produto: {self.nome}
            \tValor da compra do produto: {self.preco}
            \tQuantidade em estoque: {self.quantidade}
            \tValor total em estoque: {self.valortotalemestoque()}
            """
        return saida