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