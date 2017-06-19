count = 0
print ("\nBonjour")
print ("Question 1: Qu'elle années est-ce que chapitre est sur?")
answer1=input("Mis seulement les numéros\nExample: 1990\n")
if answer1.lower()== "1920":
 print ("Correcte")
 count += 1
else: 
 print ("Incorrect")

print ("\nQuestion 2: Vrai ou faux: Est-ce qu'il y a du racisme dans Canada")
answer2=input("Répondre avec Vrai ou Faux\n")
if answer2.lower()== "vrai":
 print ("Correcte")
 count += 1
else:
 print ("Incorrect")
 
print ("\nQuestion 3: Qui etait nommée une juge en Alberta")
answer3=input ("A)Emily Murphy\nB)Mackenzie King\nC)Lionel Conacher\nD)Bobbie Rosenfeld\nMis seulement un lettre\n")
if answer3 == "a" :
 print("Correcte")
 count += 1
else:
 print ("Incorrect")
 
print ("\nQuestion 4: Quoi est-ce que Frederick Banting et Charles Best invente?")
answer4=input ("Mis seulement le nom du invention\n")
if answer4.lower() == "insulin" :
 print("Correcte")
 count += 1
else:
 print ("Incorrect")
 
print ("\nQuestion 5: Qui est le gouverneur général?")
answer5=input ("Mis tout le nom\n")
if answer5.lower() == "julian byng" :
 print("Correcte")
 count += 1
else:
 print ("Incorrect")
 
print ("\nQuestion 6:Combien des Canadiens écoutaient les émissions américaines?")
answer5=input ("A)20 000\nB)50 000\nC)100 000\nD)300 000\nMis seulement un lettre\n")
if answer5.lower() == "d" :
 print("Correcte")
 count += 1
else:
 print ("Incorrect")

print ("\nQuestion 7:Quoi est-ce que Wilfird <<Wop>> May fait?")
answer5=input ("A)Acteur\nB)Athlète\nC)Pilote\nD)Politicien\nMis seulement un lettre\n")
if answer5.lower() == "c" :
 print("Correcte")
 count += 1
else:
 print ("Incorrect")
 
print ("\nQuestion 7:Quand est-ce que le prohibition finis dans États-Unis?")
answer5=input ("Mis seulement les numéros\nExample: 1990\n")
if answer5.lower() == "1933" :
 print("Correcte")
 count += 1
else:
 print ("Incorrect")
 
print ("\nFinis\nRésultat")

print ("Score total: " + str(count) + "/8")
division = float(count)/float(8)
multiply = float(division*100)
result = round(multiply)
print ("Pourcentage total", int(result), "%")

quit=input ("Est-ce que vous voules quitter?\n")
if quit.lower() == "oui" :
  sys.exit 

 