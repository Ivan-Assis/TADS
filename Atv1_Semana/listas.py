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