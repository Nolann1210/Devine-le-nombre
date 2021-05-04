'''
Devine le nombre !!!
L'ordinateur pense à un nombre et le joueur doit deviner ce nombre
Lances le programme, entre entre quelles valeurs tu veux jouer et suis les conseils de l'ordinateur pour réussir à deviner le bon nombre
'''

# Importation des modules necessaires
from random import randint

# Permet d'initialiser les nombres utilisées dans la récursion
def nombres():
    global v_min, v_max, valeur
    v_min = int(input("Valeur minimale : "))
    v_max = int(input("Valeur maximale : "))
    valeur = randint(v_min, v_max)

# Récursion jusqu'à ce que l'utilisateur trouve la bonne réponse
def devine():
    chiffre = int(input("Devinez le nombre : "))
    if chiffre == valeur:
        return "Bravo, vous avez trouvé, c'était",chiffre
    else:
        if chiffre < valeur:
            print("Plus Grand")
            return devine()
        print("Plus Petit")
        return devine()

if __name__ == "__main__":
    print(nombres())
    print(devine())
