#exo 6
import re

s = "To be or not to be, that is the question!"

# j'initialise une variable compteur
# pour chaque lettre
# si le caractère est une lettre
# je vais faire grandir le compteur de 1
# afficher le compteur à la fin


def letter_number(string):
    count_s = 0
    for letter in string:
        if letter.isalpha():
            count_s += 1
    return count_s


def letter_number2(string):
    result = ""
    for letter in string:
        if letter.isalpha():
            result += letter
    return len(result)


def letter_number3(string):
    return len([x for x in string if x.isalpha()])


def letter_number4(string):
    return len(re.sub(r'\W','',string))


print(letter_number4(s))
