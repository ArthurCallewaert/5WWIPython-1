woord = input('Woord: ')
bedrag = int(input('Bedrag: '))
gegokte_letters = ''
geldsom = 0
letter = input('Letter: ')

while letter in woord and not letter in gegokte_letters:
    gegokte_letters += letter
    geldsom += bedrag
    letter= input('Letter: ')

print(geldsom)
