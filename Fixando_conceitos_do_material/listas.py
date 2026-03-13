#Aprendendo litas

# Montando uma lista

bicicletas = ["bicicleta 1", "bicicleta 2", "bicicleta 3"]

print(bicicletas) #é normal sair com o colchetes, pra sair sem o colchetes precisa fazer aquele [0:3] ou seja, do 0 ao 3, ou seja, do começo ao fim da lista

#Pra retornar só um elemento da lista a gente faz

print(bicicletas[0]) #aqui ele vai retornar só o primeiro elemento da lista, ou seja, bicicleta 1. Note também que ele imprimiu sem os colchetes

print(bicicletas[0].title()) #aqui ele imprimiu o primeiro elemento da lista, ou seja, bicicleta 1, e deixou a primeira letra maiúscula

print(bicicletas[-1]) #aqui ele imprimiu o último elemento da lista, ou seja, bicicleta 3. Tem que ficar ligado pq é como se fosse uma coisa giratória, ou seja, depois do último elemento vem o primeiro elemento, e depois do primeiro elemento vem o último elemento, e assim por diante. Então, se a gente colocar -2 ele vai retornar o penúltimo elemento da lista, ou seja, bicicleta 2

#Com f-strings a gente pode fazer uma mensagem junto com algum elemento da lista, por exemplo:

mensagem = f"Minha bicicleta favorita é a {bicicletas[0].title()}"

print(mensagem)

#modificando elementos da lista

#Alterar elementos da lista é bem parecido com referenciar elementos da lista, TOMAR CUIDADO! Não precisa fazer for, é só referenciar normal, por exemplo:

motos = ["honda", "Yamaha", "Ducati"]

print(motos)

#veja que aqui yamaha é o segundo elemento!
#vou modificá-lo agoa

motos[1] = "TIREI YAMAHA"

print(motos)
print(motos[1])

#Para  acrescentar elementos à uma lista, nós usamos append

motos.append("ACRESCIMO1")
print(motos)

#Note que o append sempre adicionar NO FINAL DA LISTA

#para adicionarmos numa posição específica usamos insert, confira

lista_insert = ["elemento1", "elemento2", "elemento3", "elemento4"]

lista_insert.insert(1,"ACRESCENTADO") #ACRESCENTOU NO INDICE 1

print(lista_insert)

#REMOVENDO ELEMENTOS DA LISTA - "instrução del" - vale SE VC SOUBER O INDICE

lista_del = ["elemento1", "elemento2", "elemento3", "elemento4"]

del lista_del[2]

print(lista_del)