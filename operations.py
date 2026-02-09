from cmath import sqrt

from pyparsing import empty

file=open('defi1.txt', 'a+')
#addition
def addition(a, b):
    return a + b

#soustraction
def soustraction(a, b):
    return a - b
#multiplication
def multiplication(a, b):
    return a * b
#division
def division(a, b):
   if b != 0:
        return a / b
   else:
       print('division impossible')


#puissance
def puissance(a,n):
    return a**n
#racine carre
def carre(a):
   if a < 0:
       print("carre impossible entrer un nombre valide")
   else :
    return sqrt(a)


#menu
def menu():

    print(f"{'menu':=^20}")
    print("1.addition")
    print("2.soustraction")
    print("3.multiplication")
    print("4.division")
    print("5.racine carre")
    print("6.puissance")
    print("7.Historique")
    print("8.quit")
#pour sauvegarder
def sauvegarde(file,resultat):
    file.write(f"{resultat}\n")
#pour afficher
def historique(file):
    if file is empty:
        print("historique vide ")
    else:
     return file
