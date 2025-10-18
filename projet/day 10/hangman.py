from english_words import get_english_words_set
import random
import os

mots = get_english_words_set(['web2'], lower=True)

def mot_aleatoire():
    return random.choice(list(mots))

mot_a_deviner = mot_aleatoire()
print(mot_a_deviner)

mot_cacher = "_" * len(mot_a_deviner)

n=0
lettre = ""

while n<12:

    if mot_cacher != mot_a_deviner:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Mot à deviner : ", mot_cacher)
        print("nombre de vie restantant: ",12-n)
        print("vous avé utiliser: ",lettre)
        utilisateur = input("Entrez une lettre:")
        
        lettre_trouvee = False

        for i in range(len(mot_a_deviner)):

            if utilisateur == mot_a_deviner[i]:
                mot_cacher = mot_cacher[:i] + utilisateur + mot_cacher[i+1:]
                lettre_trouvee = True

        if not lettre_trouvee:
            n += 1
            for i in utilisateur:
                lettre=lettre+" "+i
        
        print(mot_cacher)


    elif mot_a_deviner == mot_cacher:

        print("\033[32mBravo ! Le mot\033[0m",mot_a_deviner,"\033[32ma été trouvé\033[0m" )
        break

if n>=12:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[31mVOUS AVEZ PERDU\033[0m")
    print("Le mot a deviner était: ",mot_a_deviner)