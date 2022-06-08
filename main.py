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

galgVisual = {
	"1": '''
                                          	  
                                                
                                                
                                                
                                                
                                          =========
	''',
	"2": '''
                                            	|
                                                |
                                                |
                                                |
                                                |
                                          =========
	''',
	"3":'''                                            +---+
                                            |   |
                                                |
                                                |
                                                |
                                                |
                                          =========
	''',
	"4": '''                                            +---+
                                            |   |
                                            O   |
                                                |
                                                |
                                                |
                                          =========
	''',
	"5": '''                                            +---+
                                            |   |
                                            O   |
                                            |   |
                                                |
                                                |
                                          =========
	''',
	"6": '''                                            +---+
                                            |   |
                                            O   |
                                           /|   |
                                                |
                                                |
                                          =========
	''',
	"7": '''                                            +---+
                                            |   |
                                            O   |
                                           /|\  |
                                                |
                                                |
                                          =========
	''',
	"8": '''                                            +---+
                                            |   |
                                            O   |
                                           /|\  |
                                           /    |
                                                |
                                          =========
	''',
	"9": '''                                            +---+
                                            |   |
                                            O   |
                                           /|\  |
                                           / \  |
                                                |
                                          =========
	'''
}

def gameloop():
  global fouten, run, woord, streepjes, randomWoord, goed
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
    galgFouten = str(fouten)
    print(galgVisual[galgFouten])

  if gekozenletter.isdigit():
    print("Dat is geen letter!")
    fouten -=1
  if gekozenletter == randomWoord or not "_" in streepjes:
    print("Goedzo %s je hebt het woord geraden!" % (naam))
    print("Het woord was " + randomWoord) 
    fouten = 9
  else:
    print(" ".join(streepjes))
    print("%s fout" % fouten) 

  streepjes = []
  
  print( )
  if fouten > 8: 
    print("Helaas, je hebt verloren %s." % (naam))
    print( )
    print("Het woord was " + randomWoord + ".")
    keus = input("nog een keer?")
    if(keus == "ja"):
      randomWoord = random.choice(woorden)
      streepjes = []
      goed = []
      fouten = 0
    else:
      exit()


while run == True:
  while fouten < 9:
    gameloop()
  randomWoord = random.choice(woorden)
  streepjes = []
  goed = []
  fouten = 0

  



 