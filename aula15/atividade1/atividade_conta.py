# ----------Conta Bancaria----------
class ContaBancaria:
    # Atributos privados
    __numero: int
    __titular: str
    __saldo:float

    # propiedades para acessar os membros da classe
    @property
    def numero(self, numero) -> int:
        self.__numero = numero
    
    @property
    def titular(self,titular):
        self.titular = titular

    @property
    def saldo(self,saldo):
        self.__saldo = saldo

    # Construtor
    def __init__(self, num: int = 0, titular: str = "", saldo: float = 0.0):
        self.numero = num
        self.titular = titular
        self.saldo = saldo

    # Metodos
    def depositar(self, quantia):
        self.__saldo = self.__saldo + quantia

    def sacar(self, quantia):
        self.__saldo = self.__saldo - quantia

    def mostrar_dados(self):
        print(f"Número da conta: {self.numero}")
        print(f"Titular da conta: {self.titular}")
        print(f"Saldo da conta: R$ {self.saldo:.2f}")

numero = int(input("Digite o número da conta: "))
titular = str(input("Digite o titular da conta: "))
adriano = str(input("Deseja fazer um deposito incial? (s/n):  "))

if adriano == "s":
    saldo = float(input("Digite o saldo incial: "))
    conta = c(numero, titular, saldo)
else:
    conta = c(numero, titular, 0.0)

print("Dados da conta")
c.mostrar_dados(conta)

quantia = float(input("Digite a quantia a ser depositada: R$"))
conta.depositar(quantia)
print("Dados da conta atualizados: ")
conta.mostrar_dados()

quantia = float(input("Digite a quantia a ser sacada: R$"))
conta.sacar(quantia)
print("Dados da conta atualizados: ")
conta.mostrar_dados()