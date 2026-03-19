#parte de loop for pulada.

#listas numericas - RANGE

#printando um intervalo numerico com range -> LEMBRAR QUE ELE SEMPRE ROUBA O ÚLTIMO NÚMERO

for valor in range(0,5):
    print(valor)

#CRIANDO UMA LISTA numerica com range -> lembrando que ele sempre rouba o ultimo numero

numeros  = list(range(1,5))
print(numeros)

#Ao passar um terceiro valor para o metodo range vc estara informando o PASSO, ou seja, qual o ritmo de passos o python deve seguir ao montar seu range. Vejamos como fazer de 2 em 2

numerosPassos = list(range(0,10,2))
print(numerosPassos)

#Dá pra manipular essas listas tambem, por exemplo fazer uma lista com o quadrado desses numeros

quadrados = []

for valor in range(0,11):
    quadrados.append(valor ** 2)

print(quadrados)

#metodos de manipoulacao de lista
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits))

print(max(digits))

print(sum(digits))

#List comprehension é encurar as listas no python pra ficarem melhores de ler e escrever e ficarem mais curtas  EX:

quadradosC = [valor ** 2 for valor in range(0,10,2)]

print(quadrados)

#da pra fazer com string tambem

palavras = ["ay", "papay", "que", "isso"]

maiusculas = [palavra.upper for palavra in palavras]

print(maiusculas)

#Adicionando condicao em loop com listas

numerosCondicao = [valor * 2 for valor in range(0,11) if valor % 2 == 0 ]
print("---------------------------------------------")
print(numerosCondicao)

#LISTAS ANINHADAS -> DÁ PRA FAZER MATRIZ NISSO --------------------------------- IMPORTANTE, NAO TREINADO

matriz = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matriz)

#FATIANDO/SLICING UMA LISTA

jogadores = ["jogador0", "jogador1", "jogador2", "jogador3","jogador4", "jogador5", "jogador6"  ]

print(jogadores[0:3])

print(jogadores[1:4])

print(jogadores[:3])

print(jogadores[3:])

print(jogadores[0::3])

print(jogadores[-2:])

#utilizando LOOP em slicing de uma lista

for jogador in jogadores[1::2]:
    print(jogador)

#copiando uma lista - PRECISA USAR FATIA, SE NÃO 

comidas = ["comida 1", "comida 2", "comida 3", "comida 4", "comida 5", "comida 6", "comida 7", "comida 8", "comida 9"]

comidasCopia = comidas[:]

print(comidasCopia)

comidas.append("teste1")
comidasCopia.append("teste2")

print(comidas)
print(comidasCopia)

#TUPLAS

#TUPLA É UMA LISTA IMUTÁVEL, o uso de uma tupla é exatamente como o de uma lista, a única diferença é que ela é construída com () em vez de []

tupla = ("objeto 1", "objeto 2", "objeto 3")
print(tupla[1])
print(tupla[2])

#tupla[0] = "alteração" -> NÃO FUNCIONA

#EM TERMOS TÉCNICOS -> Uma tupla SEMPRE tem vírgula, MESMO QUANDO TEM APENAS 1 ELEMENTO, aí nesse caso cria-se uma tupla com uma vírgula solta a direita, veja exemplo:

tupla_unica =("ObjetoUnico",)
print(tupla_unica)