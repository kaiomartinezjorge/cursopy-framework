lista = ["SENAI", True, 22, 3.5]
print(lista)
print(type(lista))
print(lista[2])
print(len(lista))
lista.insert(1, "campeao")
lista.append("Feriado")
del lista[3]
lista.append("SENAI")
print(lista)
for i in range(len(lista)):
    print(lista[i])

tupla = ["SENAI", True, 56, 74.6]
print(tupla)
print(type(tupla))
print(tupla[3])
print(tupla[1])
tupla.insert(1, "campeao")
del  tupla[1]
print(tupla)
TUPLA = ("SENAI", True, 56, 74.6)

dicionario = {"nome": "SENAI","logica": False,"num1":2, "num2":1.5 }
print(dicionario)
print(type(dicionario))
print(dicionario["logica"])
for chave in dicionario.keys():
    print(chave, "->",dicionario[chave])
dicionario.update({"novo": "SENAI"})
dicionario.update({"nome": "Terca"})

conjunto = {"SENAI", False, 10, 2.69}
print(conjunto)