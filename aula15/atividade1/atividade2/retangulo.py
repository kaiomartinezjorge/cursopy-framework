# Inicio classe
class retangulo:

    __base:float
    __altura:float

    @property
    def base(self):
        return self.__base
    @base.setter
    def base(self, base:float):
        if base < 0:
            base = 0
            return print("A altura não pode ser negativa, valor definido como")
        self.__base = base

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura:float):
        if altura < 0:
            altura = 0
            return print("A altura não pode ser negativa, valor definido como")
        self.__altura = altura

    def __init__(self, base:float, altura:float):
        self.altura = altura
        self.base = base


    # METODOS
    def area(self) -> float:
        return self.altura * self.base

    def perimetro(self) -> float:
        return (self.altura * 2) + (self.base * 2)

    def diagonal(self) -> float:
        from math import sqrt, pow
        return sqrt(pow(self.base, 2) + pow(self.altura, 2))

    def dadosretangulo(self) -> str:
        saida = f"""
    Area = {self.area()}\n
    Perimetro = {self.perimetro()}\n
    Diagonal = {self.diagonal()}
    """
        return saida
    

# Inicio programa principal

# Entrada de dados
try:
    base = float(input("Digite a base do retangulo: "))
    altura = float(input("Digite a altura do retangulo: "))
    #Instanciar o objeto do tipo do retangulo
    Retangulo = retangulo(base, altura)
    # Saida de dados
    print(Retangulo.dadosretangulo())
except: ValueError