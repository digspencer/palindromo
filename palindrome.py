nome_digitado = input('Digite um nome: ')

reverse = nome_digitado[::-1]

if reverse == nome_digitado:
    print('Este nome é palíndrome')
else:
    print('Este nome não é palíndrome')