lista_convidados = ["CONVIDADO 1", "CONVIDADO 2", "CONVIDADO 3", "CONVIDADO 4"]

for convidado in lista_convidados:
    print(f"Ola, {convidado}! Venha para meu jantar!")

print(f"{lista_convidados[0]} não irá ao jantar")
lista_convidados[0] = "NOVO CONVIDADO!"

for convidado in lista_convidados:
    print(f"{convidado}, VOCE ESTA CONVIDADO")

# convidado_faltante = lista_convidados.pop(0)
# print(f"{convidado_faltante} não irá ao jantar")

# print(lista_convidados)

print("__________________________________________________________")

meio = len(lista_convidados)// 2
print(meio)



print("__________________________________________________________")

print("__________________________________________________________")

lista_convidados.insert(0,"CONVIDADO ADICIONAL 1")

lista_convidados.insert(len(lista_convidados),"CONVIDADO ADICIONAL 3")
lista_convidados.insert(meio,"CONVIDADO ADICIONAL 2")

print(lista_convidados)

for convidado in lista_convidados:
    print(f"{convidado}, vamos para o jantar!")

print("CONVIDAREMOS APENAS 2 PESSOAS PARA O JANTAR")

for convidado in range(2,len(lista_convidados)):
    desconvidado = lista_convidados.pop()

    print(f"{desconvidado}, sinto mt, mas vc está fora!")

for convidado in lista_convidados:
    print(f"{convidado}, VOCE ESTA CONVIDADO AINDA!!")

del lista_convidados[1]
del lista_convidados[0]

print(lista_convidados)