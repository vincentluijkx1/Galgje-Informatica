print("Welkom bij galgje!")

print ()
naam = input ("Hoe heet je: ")
print( )
print("Hallo, %s we gaan nu beginnen met galgje!" % (naam))

import random
woorden = ("informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk")
randomWoord = random.choice(woorden)
goed = woorden
streepjes = []

gekozenletter = input("kies een letter")
for letter in randomWoord:
  if gekozenletter in randomWoord:
    streepjes.append(letter)
  else:
    streepjes.append("_")


print(streepjes)

