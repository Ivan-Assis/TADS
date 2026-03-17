amigos_linguagens = {
    'amigo 1' : 'linguagem 1',
    'amigo 2' : 'linguagem 2',
    'amigo 3' : 'linguagem 3',
    'amigo 4': 'linguagem 4' ,
    'amigo 5' : 'linguagem 4'                   
}

print(f"O amigo 1 gosta de programar em {amigos_linguagens['amigo 1']}")
print(f"O amigo 2 gosta de programar em {amigos_linguagens['amigo 2']}")

for key,value in amigos_linguagens.items():
    print(f"{key.title()} gosta de programar em {value}.\n")

for key,value in amigos_linguagens.items():
    print(f"{key.title()} gosta de programar em {value}.\n")

for key in amigos_linguagens.keys():
    print(f"meus amigos que responderam a pesquisa são {key}")

print(amigos_linguagens.values())
values_list = list(amigos_linguagens.values)
values_set = set(amigos_linguagens.values()) #esse set é conjunto, ta transformando em conjunto

print(values_list)
print(values_set)

#CONJUNTO NAO TEM ELEMENTOS REPETIDOS

for language in set(amigos_linguagens.values):
    print(language)