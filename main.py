import sys
from cmath import sqrt
import operations
while True:
 operations.menu()
 # choix
 choix_valide = [1, 2, 3, 4, 5, 6,7,'quit']
 essaie = 3
 choix = input("choix : ")
 if choix not in choix_valide:
    # boucle pour verifier si le choix est valide avec un nombre d'essaie a 3
    while essaie != 1:
        essaie = essaie - 1
        print(f"il vous reste {essaie} essaie")
        print("choix invalide. veuillez entrer un nombre valide")
        choix = int(input("choix : "))
 elif choix == 1:
    a=int(input("entrer la premiere valeur : "))
    b=int(input("entrer la deuxieme valeur : "))
    resultat=operations.addition(a, b)
    print(f"{a}+{b} = {resultat}")

 elif choix == 2:
    a = int(input("entrer la premiere valeur : "))
    b = int(input("entrer la deuxieme valeur : "))
    resultat = operations.soustraction(a, b)
    print(f"{a}-{b} = {resultat}")

 elif choix == 3:
    a = int(input("entrer la premiere valeur : "))
    b = int(input("entrer la deuxieme valeur : "))
    resultat = operations.multiplication(a, b)
    print(f"{a}*{b} = {resultat}")

 elif choix == 4:
    a = int(input("entrer la premiere valeur : "))
    b = int(input("entrer la deuxieme valeur(different de zero) : "))
    resultat = operations.division(a, b)
    print(f"{a}//{b} = {resultat}")

 elif choix == 5:
    a = int(input("entrer la valeur : "))
    resultat=operations.carre(a)
    print(f'la racine carre de {a} est {resultat}')

 elif choix == 6:
     a = int(input("entrer le nombre : "))
     n = int(input("entrer la puissance: "))
     resultat = operations.puissance(a, n)
     print(f"{a}a la puissance{n}={resultat}")

 elif choix == 7:
    operations.historique()

 elif choix == 'quit':
    print("merci et a la prochaine")
    sys.exit(0)

