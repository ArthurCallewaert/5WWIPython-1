n = int(input('n: '))

F1 = 1
F2 = 1

if n > 2:
    for i in range(n-2):
        getal = F1 + F2

        F1 = F2
        F2 = getal

else:
    getal = 1


print(getal)
