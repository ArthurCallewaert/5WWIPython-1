aantal_getallen = int(input('Aantal getallen: '))

eerste_getal = int(input('Getal: '))
som = eerste_getal
grootste = eerste_getal


for i in range(aantal_getallen - 1):
    getal = int(input('Getal: '))

    som += getal

    if getal > grootste:
        grootste = getal

gemiddelde = som / aantal_getallen

uitvoer = 'Het grootste getal is {} en het gemiddelde is {:.2f}'

print(uitvoer.format(grootste, gemiddelde))
