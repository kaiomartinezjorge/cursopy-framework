from enum import Enum

class Estados_pedidos(Enum):
    PAGAMENTO_PENDENTE = 0
    PROCESSAMENTO = 1
    ENVIADO = 2
    ENTREGUE = 3
    CANCELADO = 4

print(Estados_pedidos(2))
print(Estados_pedidos.CANCELADO)
print(Estados_pedidos.ENVIADO.name) #Mostra apenas o nome
print(Estados_pedidos.ENTREGUE.value)#Mosttra apenas o valor
print(Estados_pedidos(1).name)#Apresenta o nome a partir do valor 