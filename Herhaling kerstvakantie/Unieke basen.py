from math import fsum

aantal = int(input('Aantal basen: '))

aantal_soorten = 0

t_base = False
a_base = False
c_base = False
g_base = False

for i in range(aantal):
    soort = input('Letter: ')

    if soort == 'T':
        t_base = True
    if soort == 'A':
        a_base = True
    if soort == 'C':
        c_base = True
    if soort == 'G':
        g_base = True


aantal_soorten = t_base + a_base + c_base + g_base


