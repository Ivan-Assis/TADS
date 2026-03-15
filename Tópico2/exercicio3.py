#3.8

locais = ["azerbaijão", "brasil", "cannes", "dinamarca", "estonia", "finlandia"]

if locais != sorted(locais):
    print("Lista não está em ordem alfabetica")
else:
    print("Lista ordenada alfabeticamente!")

locais.sort(reverse=True)

#print(locais)

print(sorted(locais))

locais.sort()
print(locais)

print(sorted(locais, reverse=True))
print(locais)


locais.reverse()
print(locais)
locais.reverse()
print(locais)

locais.sort()
print(locais)

locais.sort(reverse=True)
print(locais)

#3.9

convidados = ["CONVIDADO 1", "CONVIDADO 2", "CONVIDADO 3", "CONVIDADO 4", "CONVIDADO 5",]

qtdConvidados = len(convidados)

print(qtdConvidados)



