tijdstip = int(input('Tijdstip: '))
afstand = 0

stappen_voor = 2
stappen_achter = 1


for i in range(tijdstip):
    if (i % 2) == 0: #stappen naar voor
        afstand += stappen_voor
        stappen_voor += 2
    else: #stappen naar achter
        afstand -= stappen_achter
        stappen_achter += 1


print(afstand)
