names = ["Lucas", "Patrick", "Leonardo"]

print(names[0])
print(names[1])
print(names[2].title())

#imprimindo todos sem colchetes so de bobeira

print(*names)


#Fazendo um loop 

for nome in names:
    print(f"Olá {nome}! Como vai vc?")

transportes = ["Honda", "Yamaha", "Ducati", "Royal Enfield"]

for transporte in transportes:
    print(f"Queria muito ter uma moto {transporte} ")

