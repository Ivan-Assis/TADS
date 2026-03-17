#DICIONARIOS -> Formado com {}, key : value é a estrutura, válido lembrar também que aceita dados imutaveis dentro dele apenas

alien_0 = {
    'color': 'green',
    'points' : 5
}

alien_0['alive'] = True

print(alien_0)

alien_1 = {}
alien_1['color'] = 'black'

print(alien_1)


alien_0['points'] = 0
alien_0['alive'] = False

print(alien_0)

alien_2 = {
    'color': 'red',
    'points' : 5

}

