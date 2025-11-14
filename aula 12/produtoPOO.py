class Produto:
    nome:str
    preco:float
    quantidade:int
    #metodos
    def valortotalemestoque(self) -> float:
        return self.preco * self.quantidade
    
    def adicionarprodutos(self, quantidade) -> int:
         self.quantidade =  self.quantidade + quantidade 
         return self.quantidade

    def removerprodutos(self, quantidade) -> int:
        self.quantidade = self.quantidade - quantidade
