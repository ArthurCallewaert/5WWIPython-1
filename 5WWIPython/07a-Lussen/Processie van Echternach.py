t = int(input('Tijdstip: '))
bereik = t+1

afstand = 1

for i in range(0, bereik):
    if i%2 == 0:
        afstand += 2

    else:
        afstand -= 1



print(afstand)
