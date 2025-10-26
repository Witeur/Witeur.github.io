from english_words import get_english_words_set
import random
import os

mots = get_english_words_set(['web2'], lower=True)

def mot_aleatoire():
    return random.choice(list(mots))

mot_a_deviner = mot_aleatoire()
print(mot_a_deviner)

mot_cache = "_" * len(mot_a_deviner)

n = 0
lettres = ""

while n < 12:

    if mot_cache != mot_a_deviner:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Mot à deviner :", mot_cache)
        print("Nombre de vies restantes :", 12 - n)
        print("Vous avez utilisé :", lettres)
        utilisateur = input("Entrez une lettre : ")
        
        lettre_trouvee = False

        for i in range(len(mot_a_deviner)):
            if utilisateur == mot_a_deviner[i]:
                mot_cache = mot_cache[:i] + utilisateur + mot_cache[i+1:]
                lettre_trouvee = True

        if not lettre_trouvee:
            n += 1
            for i in utilisateur:
                lettres = lettres + " " + i
        
        print(mot_cache)

    elif mot_a_deviner == mot_cache:
        print("\033[32mBravo ! Le mot\033[0m", mot_a_deviner, "\033[32ma été trouvé\033[0m")
        break

if n >= 12:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[31mVOUS AVEZ PERDU\033[0m")
    print("Le mot à deviner était :", mot_a_deviner)
