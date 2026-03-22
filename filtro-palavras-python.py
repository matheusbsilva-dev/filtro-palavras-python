lista = []

while True:
    palavra = input('Coloque uma palavra: ')
    lista.append(palavra)

    r = input('Quer continuar? (s/n): ').lower()

    if r == 'n':
        break

print('\nLista final:', lista)

print('\nPalavras com 4 letras:')
for p in lista:
    if len(p) == 4:
        print(p)