#j'initialise une variable ou l'on stockera les premieres lettres de l'acronym
#transformer la string en majuscule
#split la string dans une liste
#pour chaque mot de la liste
#récuperer la 1ere lettre
#on fait grandir notre acronym

def acronym(string):
    result = ""
    upper_string = string.upper()
    words = upper_string.split()
    for word in words:
        result += word[0]
    return result

print(acronym("read the fucking manual"))

#initialiser le resultat avec la premiere lettre de la string
#pour chaque index correspondant au lettre de la string
#je retrouve la lettre à partir de l'index
#si la lettre est " "
#alors je trouve la lettre à l'index suivante
#je fais grandir le resultat de cette lettre
