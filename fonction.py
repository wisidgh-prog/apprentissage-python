#Creer liste fruit
fruit=['pomme','banane','cerise','datte']
#affichage du premier et dernier element
fin_list=len(fruit)
print(fruit[1],fruit[fin_list-1])
#ajouter l'element orange a la fin
fruit.append('orange')
#remplacer banane par kiwi
fruit[1]='kiwi'
print(fruit[:])


