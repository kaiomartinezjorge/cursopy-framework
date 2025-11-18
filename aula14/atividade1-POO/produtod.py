class pessoas:
    def __init__(self, nome: str = "", idade: int = 0):
        self.nome = nome
        self.idade = idade

    def mais_velha(self, outra) -> int:
        if self.idade > outra.idade:
            return self.nome
        else:
            return outra.nome


class funcionarios:
    def __init__(self, nome: str = "", salario: float = 0.0):
        self.nome = nome
        self.salario = salario

    def salario_medio(self, outro):
        return (self.salario + outro.salario) / 2

        
        



   

