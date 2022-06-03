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
run = True

def gameloop():
  global fouten, run, woord, streepjes
  gekozenletter = input("Kies een letter: \n")  
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
    print("Dat is geen letter!")
    fouten -=1
  if gekozenletter == randomWoord or not "_" in streepjes:
    print("Goedzo %s je hebt het woord geraden!" % (naam))
    print("Het woord was " + randomWoord)
    run = False
  else:
    print(" ".join(streepjes))
    print("%s fout" % fouten)
  woord = "".join(streepjes)

  streepjes = []
  print( )
  if fouten >9: 
   print("Helaas, je hebt verloren %s." % (naam))
   print( )
   print("Het woord was " + randomWoord + ".")

while run == True:
  gameloop()


