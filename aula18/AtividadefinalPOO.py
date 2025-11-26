import os

class Pessoas:
    __nome: str
    __renda: float

    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        if not nome:
            raise ValueError("Valor inválido")
        self.__nome = nome

    @property
    def renda(self) -> float:
        return self.__renda
    @renda.setter
    def renda(self, renda: float):
        if renda < 0:
            raise ValueError("Valor inválido")
        self.__renda = renda

    def __init__(self, nome: str, renda: float):
        self.nome = nome
        self.renda = renda


# ---------- Subclasse Pessoa Física ----------

class PessoaFisica(Pessoas):
    __gastosaude: float

    @property
    def gastosaude(self) -> float:
        return self.__gastosaude
    @gastosaude.setter
    def gastosaude(self, gastosaude: float):
        if gastosaude < 0:
            raise ValueError("Valor inválido")
        self.__gastosaude = gastosaude * 0.5

    def __init__(self, nome: str, renda: float, gastosaude: float):
        super().__init__(nome, renda)
        self.gastosaude = gastosaude

    def jurosfisica(self):
        if self.renda < 20000:
            return self.renda * 0.15 
        else:
            return self.renda * 0.25
 

    def dadosfisica(self):

        saida = f'''
    Nome: {self.nome}
    Renda: {self.renda}
    gasto com saude: {self.gastosaude}
    Imposto a pagar: {self.jurosfisica() + gastosaude}
    '''
        return saida


# ---------- Subclasse Pessoa Jurídica ----------

class PessoaJuridica(Pessoas):
    __numfuncionarios: int

    @property
    def numfuncionarios(self) -> int:
        return self.__numfuncionarios
    @numfuncionarios.setter
    def numfuncionarios(self, numfuncionarios: int):
        if numfuncionarios < 0:
            raise ValueError("Valor inválido")
        self.__numfuncionarios = numfuncionarios

    def __init__(self, nome: str, renda: float, numfuncionarios: int):
        super().__init__(nome, renda)
        self.numfuncionarios = numfuncionarios

    def jurosJuridica(self):
        if self.numfuncionarios > 10:
            return self.renda * 0.14  
        else:
            return self.renda * 0.16  

    def dadosjuridica(self):

        saida = f'''
    Nome: {self.nome}
    Renda: {self.renda}
    Funcionários: {self.numfuncionarios}
    Imposto a pagar: {self.jurosJuridica()}
    '''
        return saida
  
# ----------Fim das classes----------

# Inicio do codigo princial

os.system('cls')

pessoasj = []
pessoasf = []
print("Bem vindo!")
contri = int(input("Insira o número de contribuintes que deseja calcular: "))

for i in range(contri):
    print(f"Dados da pessoa {i+1}")
    resposta = str(input("\nInsira (j) para pessoa juridica ou (F) para pessoa fisica: "))
    if resposta == "j":
        nome = str(input("\nInsira o nome: "))
        renda = float(input("\nInsira a renda anual: "))
        funcionarios = int(input("\nInsira o número de funcionarios da pessoa: "))

        pj = PessoaJuridica(nome, renda, funcionarios)

        print("\n----- Resultado -----")
        print(pj.dadosjuridica())  

        pessoasj.append(pj)


    else:
    
        nome = str(input("\nInsira o nome: "))
        renda = float(input("\nInsira a renda anual da pessoa: "))
        gastosaude = float(input("\nInsira o gasto com saude da pessoa: "))

        pf = PessoaFisica(nome, renda, gastosaude)

        print("\n----- Resultado -----")
        print(pf.dadosfisica()) 

        pessoasf.append(pf)

