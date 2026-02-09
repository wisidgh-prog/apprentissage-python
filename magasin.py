prix_unit= float(input("Entrer le prix de l'article:"))
quantite=int(input("Entrer le quantite:"))
TX_TVA=0.18
prix_HT=prix_unit*quantite
TVA=prix_HT* TX_TVA
prix_TTC=prix_unit+TVA
print("________facture________")
print("__prix__ :",prix_unit)
print("__quantite__ :",quantite)
print("__TX_TVA__ :",TX_TVA)
print("__prix_TTC__ :",prix_TTC)
print("______________________________")