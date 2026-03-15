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


#atribuind valor novo a objeto da lista

lista_teste = ["1", "2", "3"]

lista_teste[1] = "MODIFICADO"

print(lista_teste)


#pop() remove o ultimo elemento da lista e possibilita usa-lo mesmo depois disso

lista_teste.pop()
print(lista_teste)#lista com o elemento removido

#Mas com o pop dá pra vc tirar e ao mesmo tempo colocar ele numa variavel:
print("_________________________________________")
lista_teste.append("TESTANDO O POP")
print(lista_teste)



variavelPOP = lista_teste.pop()
print(lista_teste)
print(variavelPOP)

#da pra usar o pop com outros elementos da lista que nao sao o ultimo, por exemplo:

print("--------------------------------------------------")
print()
print()
print()

lista_pop = ["elemento1", "elemento2", "elemento3", "elemento4"]

elemento_pop = lista_pop.pop(-1)

print(lista_pop)
print(elemento_pop)

lista_pop.append("ELEMENTO ADICIONAL")

print(lista_pop)

#Dá pra remover um elemento digitando seu conteudo com o remove

print(lista_pop)
lista_pop.remove("ELEMENTO ADICIONAL")

print(lista_pop)

#Dá pra remover passando variavel por parametro tambem,

lista_A = ["ELEMENTO 1", "ELEMENTO 2", "ELEMENTO 3", "ELEMENTO 4", "ELEMENTO 5"]
print(lista_A)
elementoRemover = "ELEMENTO 3"

lista_A.remove(elementoRemover)
print(lista_A)
print(elementoRemover)

#O remove SÓ REMOVE A PRIMEIRA OCORRENCIA, se quiser remover todas as ocorrencias tem que repetir o metodo



