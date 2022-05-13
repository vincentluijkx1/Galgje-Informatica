print("Welkom bij galgje!")

print ()
naam = input ("Hoe heet je: ")
print( )
print("Hallo, %s we gaan nu beginnen met galgje!" % (naam))

import random
woorden = ("informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk")
woorden = random.choice(woorden)
goed = woorden
print(woorden)
