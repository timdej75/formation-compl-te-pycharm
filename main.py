# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # Un autre commentaire
    # Un troisième commentaire
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
nom = input("Quel est ton nom ? ")
age = input("Quel est votre âge ? ")

try:
    age_prochain = int( age)+1
except:
    print( "Erreur : Vous devez sasir un nombre pour l'age !")
else:
    print("Hello " + nom + " vous avez " + age + " ans !")
    print("L'an prochain vous aurez " + str(age_prochain) + " ans !")

print( type( age))

n=0
while n<10:
    print( "La valeur de n est " + str(n))
    n=n+1

print( "Fin de la boucle")

if __name__ == '__main__':
    print_hi('PyCharm Welcome ' + nom + ' !')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# URL d'accès au Git-Hub
# https://github.com/timdej75/DeT-Formation-Python.git
# C'est bon je suis connecté sur le GITHUB
# Il reste à vérifier la synchronisation avec GITHUB
# C'est un nouveau commentaire pour le GIT

