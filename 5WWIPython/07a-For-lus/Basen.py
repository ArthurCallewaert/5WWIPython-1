aantal_basen = int(input('Aantal basen: '))
type_a = 0
type_t = 0
type_g = 0
type_c = 0


for i in range(aantal_basen):
    type = str(input('Type base: '))

    if 'A' in type:
        type_a += 1


    elif 'T' in type:
        type_t += 1

    elif 'G' in type:
        type_g += 1

    elif 'C' in type:
        type_c += 1





uitvoer = 'De DNA-ketting bevat {} soorten basen: {} {}'



