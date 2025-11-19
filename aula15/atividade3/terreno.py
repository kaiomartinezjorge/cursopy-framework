class Terreno:
    # 1° membro - atributos
    __largura:float
    __comprimento: float

    @property
    def largura(self):
        return self.__largura
    @largura.setter
    def largura(self,largura:float):
        self.largura = largura

    @property
    def comprimento(self):
        return self.__comprimento
    @comprimento.setter
    def comprimento(self, comprimento:float):
        self.__comprimento = comprimento
        
    # 3° membro - construtores

    def __init__(self, largura:float, comprimento:float):
        self.comprimento = comprimento
        self.largura = largura

    # 4° Membro - Metodos

    def __area(self) -> float:
        return self.comprimento * self.largura
    def __preco(self, preco:float) -> float:
        return self.__area() * preco
    
    def dadosterreno(self, preco:float) -> str:
        saida = f"""
    Largura: {self.largura}
    Comprimento: {self.comprimento}
    Area: {self.__area():.2f}
    Preço: {self.__preco(preco):.2f}
    """
        return saida
        


    try:
        largura = float(input("Digite a largura do terreno: "))
        comprimento = float(input("Digite o comprimento do terreno: "))
        preco = float(input("Digite o preço do metro quadrado: "))

        terreno = Terreno()

    except:ValueError
        
