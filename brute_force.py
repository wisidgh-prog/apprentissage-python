import itertools
import string

password =input("Mot de passe : ")
chars = string.ascii_lowercase
print("\n brute force en cours...\n")
for length in range(1,6):
    for attempt in itertools.product(chars,repeat=length):
        attempt = "".join(attempt)
        print("test :",attempt,end="\r")

        if password == attempt:
            print("Mot de passe trouver:",attempt)
            exit()

print("mot de passe trop complexe pour ce test")