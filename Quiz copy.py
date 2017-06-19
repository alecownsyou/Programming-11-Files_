count = 0
print ("\nHello and welcome to this quiz")
print ("Question 1: Who plays Indiana Jones? Answer with a single character")
print ("\n A: Robert Downey Jr.\n B: Harrison Ford \n C: Shia Labeouf \n D: Dwayne Johnson")
answer1=input(" ? ")
if answer1.lower()== "b":
 print ("Correct")
 count += 1
else: 
 print ("Incorrect")

print ("\nQuestion 2: True or false: Is Harrison Ford dead?")
answer2=input("Answer with either True or False\n ? ")
if answer2.lower()== "false":
 print ("Correct")
 count += 1
else:
 print ("Incorrect")
 
print ("\nQuestion 3: What does 3 + 5 = ?")
answer3=input (" ? ")
if answer3 == "8" :
 print("Correct")
 count += 1
else:
 print ("Incorrect")
 
print ("\nQuestion 4: What is the capital of Canada")
answer4=input ("Only type the city name\n ? ")
if answer4.lower() == "toronto" :
 print("Correct")
 count += 1
else:
 print ("Incorrect")
 
print ("\nQuestion 5: What year did Steve Jobs pass away")
answer5=input ("Only type the year\n ? ")
if answer5.lower() == "2011" :
 print("Correct")
 count += 1
else:
 print ("Incorrect")
 
print ("\nEND OF QUIZ\nYour Result is\n")

print ("Total score: " + str(count) + "/5")
division = float(count)/float(5)
multiply = float(division*100)
result = round(multiply)
print ("Total percentage is", int(result), "%")

 