import re
import random

print("Welkom bij galgje!")

print ()
naam = input ("Hoe heet je?: ")
print( )
print("Hallo, %s we gaan nu beginnen met galgje!" % (naam))


woorden = ("informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk")
randomWoord = random.choice(woorden)
streepjes = []
goed = []
fouten = 0
while True:
  gekozenletter = input("Kies een letter: ")
  if gekozenletter == randomWoord:
    print("Goedzo %s je hebt het woord geraden!" % (naam))
    break
  print( )
  for letter in randomWoord:
    if gekozenletter in randomWoord and gekozenletter == letter or letter in goed: 
      streepjes.append(letter)
      if letter not in goed:
        goed.append(letter)
    else:
      streepjes.append("_")
      
  if gekozenletter not in randomWoord :
    fouten += 1
  if gekozenletter.isdigit():
    print("Thats not a letter!")
    fouten -=1
    
  print(streepjes)
  woord = "".join(streepjes)
  if(woord == randomWoord):
    print("Goedzo %s je hebt het woord geraden!" % (naam))
  print("%s fout" % fouten)
  streepjes = []
  print( )
  if fouten >9: 
   print("Helaas, je hebt verloren %s." % (naam))
   print( )
   print("Het woord was " + randomWoord + ".")
   break
 
  



  



