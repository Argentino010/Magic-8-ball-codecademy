import random

namn = input("Vad heter du?")
fråga = input("Fråga någonting ")
svar = ""

random_number = random.randint(1, 9)

if random_number == 1:
    svar = "Ja, Naturligtvis"
elif random_number == 2:
    svar = "Självklart ja"
elif random_number == 3:
    svar = "Utan tvekan"
elif random_number == 4:
    svar = "Vet ej, fråga igen!"
elif random_number == 5:
    svar = "Fråga senare!"
elif random_number == 6:
    svar = "Ja, Jag tror det!"
elif random_number == 7:
    svar = "Jag tror inte det"
elif random_number == 8:
    svar = "Svårt att säga just nu"
elif random_number == 9:
    svar = "Nej!"

print(namn + " frågar: " + fråga)
print("Magic 8-ball svarar: " + svar)
