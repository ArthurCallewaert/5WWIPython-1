aantal_lifters = int(input('Aantal lifters: '))

hoogste_score = 0


for i in range(aantal_lifters // 2):
    score = float(input('Score van de lifter: '))

    if score > hoogste_score:
        hoogste_score = score

for n in range(aantal_lifters % 2):
    score = float(input('Score van de lifter: '))

    if score > hoogste_score:
        score_meegenomen = score
        hoogste_score = score

print(hoogste_score)
