aantal = int(input('Hoeveel basen: '))

type_t = False
type_a = False
type_c = False
type_g = False

soort_base = ''

for i in range(aantal):
    base = input('Base: ')


    if base not in soort_base:
        if base == 'T':
            type_t = True

        if base == 'A':
            type_a = True

        if base == 'G':
            type_g = True

        if base == 'C':
            type_c = True

    soort_base = soort_base + base + ''

aantal_basen = type_t + type_g + type_c + type_a


print(aantal_basen)
print(soort_base)
