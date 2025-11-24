class Produto:  #Super classe
    # 1° Membro - Atributos privados
    __nome:str
    __preco:float
    __quantidade:int

    # 2° Membro - Propriedades
    @property
    def _nome(self)->str:
        return self.__nome
    
    @_nome.setter
    def _nome(self, nome:str)->str:
        self.__nome = nome

    # Propredades do atributo preço
    @property
    def _preco(self)->float:
        return self.__preco
    @_preco.setter
    def _preco(self, preco:float)->float:
        self.__preco = preco

    #Propriedades do atributo quantidade
    @property
    def quantidade(self)->int:
        return self.__quantidade
    @quantidade.setter
    def quantidade(self,quantidade:int)->int:
        self.__quantidade = quantidade

    # 3° Membro - Construtor
    def __init__(self, nome:str, preco:float, quantidade:int):
        self._nome = nome
        self._preco  = preco
        self._quantidade = quantidade

    # 4° Membro - Métodos
    def operacao(self):
        print("Operação do Produto")
        print(f"Nome: {self._nome}")

class Software(Produto): #Classe filha de Produto
    # 1° Membro - atributo
    licenca:str
    # 2° Membro - Propriedade
    @property
    def _licenca(self)->str:
        return self.__licenca
    @licenca.setter
    def _licenca(self, licenca:str)-> str:
        self.__licenca = licenca
    # 3° Membro - Construtor
    def __init__(self, nome:str, preco:float, quantidade:int,
                 licenca: str):
        super().__init__(nome,preco,quantidade)
        self._licenca = licenca

class Hardware(Produto): #Classe filha de Produto
    # 1° Membro - Atributo
    __garantia:int

    # 2° Membro - Propriedades
    @property
    def _garantia(self):
        return self.__garantia
    @_garantia.setter
    def _garantia(self, garantia:int)->int:
        self._garantia = garantia
    
    # 3° Membro - Construção
    def __init__(self, nome:str, preco:float, quantidade:int, garantia:int):
        super().__init__(nome, preco, quantidade)
        self._garantia = garantia
# --------Fim classes--------

# ----------Main code----------

software = Software("Adobe", 1000, 10, "2010")
hardware = Hardware("Dell", 2000, 10, 6)

software.operacao()
hardware.operacao()
        