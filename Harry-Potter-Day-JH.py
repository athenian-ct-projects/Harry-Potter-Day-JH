#Keeps Score
def point_score(score):
    score=score+1
    return score
#Determines if they got it right
def correct_answer(housename):
    print("Correct! 1 point for " + housename)
    print("\n")
#Determines if they got it wrong
def incorrect_answer(housename): 
    print("INCORRECT! No points for you, " + housename)
    print("\n")
#Introduction
print ("Happy Harry Potter Day! This is a trivia quiz about the books!")
print("Each book will have 2 questions, so it's 14 questions total.")
print ("If you answer a question correctly, you will get 1 point. At the end, the points will be counted up and you'll get your final score!")
beginning=(input("Are you ready to begin? If so, print 'yes': "))
if beginning=="yes" or beginning=="Yes":
    print ("Brilliant! Let's begin. ")
else:
    print ("Well I'm afraid you don't have a choice. Let's begin. ")
#Countdown
for countdown in range (1,4):
    print (countdown)
#Housename
housename=(input("What is your Hogwarts House? "))
if housename=="Ravenclaw" or housename=="ravenclaw" or housename=="Slytherin" or housename=="slytherin":
    print("Proud honestly. Let's get started, shall we?")
else:
    print("Huh. Well anyway let's get started!")
#Base score
score=0
#First Question
print("In the first book 'The Sorcerer's Stone', how did Harry manage to defeat Voldemort and Professor Quirrell? ")
print("a. He zapped him using his wand")
print("b. He shot him with a gun")
print("c. He burned them with his hands")
print("d. He pulled them into the magic stone")
#Inputs the answer
answer1= (input("What's the correct answer? "))
#Determines if it's the right one
if answer1== "c" or answer1=="C" or answer1=="c." or answer1=="C.":
    correct_answer(housename)
    score=point_score(score)
#If they got it wrong: 
else:
    incorrect_answer(housename)
#Second Question
print("What animal did Neville loose on the train ride?")
print("a. A cat")
print("b. An owl")
print("c. A newt")
print("d. A toad")
answer2=(input("What's the correct answer? "))
if answer2=="d" or answer2=="D"or answer2=="d." or answer2=="D.":
    correct_answer(housename)
    score=point_score(score)
else:
    incorrect_answer(housename)
#Third Question
print("In the 2nd book 'The Chamber of Secrets', what is living in the walls?")
print("a. A big snake, like a REALLY big snake")
print("b. A worm, just a really big one")
print("c. Bats, normal sized")
print("d. Fish.")
answer3=(input("What's the correct answer? "))
if answer3=="a" or answer3=="A" or answer3=="A." or answer3=="a.":
    correct_answer(housename)
    score=point_score(score)
else:
    incorrect_answer(housename)
#Fourth Question
print("Who's diary does Harry find?")
print("a. Ginny's")
print("b. Good ol' Voldemort's")
print("c. Ron's")
print("d. Hermione's (ooh gossip)")
answer4=input("What's the correct answer? ")
if answer4=="b" or answer4=="B" or answer4=="b." or answer4=="B.":
    correct_answer(housename)
    score=point_score(score)
else:
    incorrect_answer(housename)
#Fifth Question
print("In the 3rd book 'The Prisoner of Azkaban', who is Ron's rat?")
print("a. Peter Pettigrew")
print("b. Rufus Stoppable")
print("c. Sirius Black")
print("d. Kim Possible")
answer5=input("What's the correct answer? ")
if answer5=="a" or answer5=="A" or answer5=="a." or answer5=="A.":
    correct_answer(housename)
    score=point_score(score)
else:
    incorrect_answer(housename)
#Sixth Question
print("What was Buckbeak?")
print("a. A flying lion")
print("b. A dragon")
print("c. A hippogriff")
print("d. A pig")
answer6=input("What's the correct answer? ")
if answer6=="c" or answer6=="C" or answer6=="c." or answer6=="C.":
    correct_answer(housename)
    score=point_score(score)
else:
    incorrect_answer(housename)
#Seventh Question
print("In the 4th book 'The Goblet of Fire', what is ONE of the schools that participate in the Triwizard Tournament(that isn't Hogwarts)?")
print("a. Durmstrang Institute")
print("b. Ilvermorny")
print("c. Castelobruxo ")
print("d. Beauxbatons Academy of Magic")
answer7=input("What's the correct answer? ")
if answer7=="a" or answer7=="A" or answer7=="a." or answer7=="A." or answer7=="d" or answer7=="D" or answer7=="d." or answer7=="D.":
    correct_answer(housename)
    score=point_score(score)
else:
    incorrect_answer(housename)
#Break
print("You are now half way done! Take a breather!")
input("Are you ready?")
print("OK!")
countdown2 = 0
while (countdown2) < 6:
    print(countdown2)
    countdown2=countdown2+1
else:
    print("Alright NEXT QUESTION YOUNG WIZARDDDD")
#Eighth Question
print("What was NOT a name of one of the competitors?")
print("a. Harry Potter")
print("b. Cedric Diggory")
print("c. Flora Comtois")
print("d. Viktor Krum")
answer8=input("What's the correct answer? ")
if answer8=="c" or answer8=="C" or answer8=="c." or answer8=="C.":
    correct_answer(housename)
    score=point_score(score)
else:
    incorrect_answer(housename)
#Ninth Question
print("In the 5th book 'The Order of the Phoenix', who dies?")
print("a. Lucious")
print("b. Sirius")
print("c. Dumbledore")
print("d. Snape")
answer9=input("What is the correct answer? ")
if answer9=="b" or answer9=="B" or answer9=="b." or answer9=="B.":
    correct_answer(housename)
    score=point_score(score)
else:
    incorrect_answer(housename)
#Tenth Question
print("What's the name of the secret army Harry, Hermoine and Ron created?")
print("a. Umbridge's Army")
print("b. Lupin's Army")
print("c. Dumbledore's Army")
print("d. Seven Nation Army")
answer10=input("What is the correct answer? ")
if answer10=="c" or answer10=="C" or answer10=="C." or answer10=="c.":
    correct_answer(housename)
    score=point_score(score)
else:
    incorrect_answer(housename)
#Eleventh Question
print("In the 6th book 'The Half Blood Prince', who gets kidnapped?")
print("a. Harry")
print("b. Narcissa Malfoy")
print("c. Ginny Weasley")
print("d. Garrick Ollivander")
answer11=input("What is the correct answer? ")
if answer11=="d" or answer11=="D" or answer11=="d." or answer11=="D.":
    correct_answer(housename)
    score=point_score(score)
else:
    incorrect_answer(housename)
#Twelfth Question
print("Whose potion's book did Harry use throughout the book?")
print("a. His own that he bought")
print("b. Hermione's")
print("c. Snape's")
print("d. Mcgonagall")
answer12=input("What is the correct answer? ")
if answer12=="c" or answer12=="C" or answer12=="C." or answer12=="c.":
    correct_answer(housename)
    score=point_score(score)
else:
    incorrect_answer(housename)
#Thirteenth Question
print("In the book 'The Deathly Hallows Part 1', which friend saves Harry and his friends and then dies?")
print("a. Draco")
print("b. Dobby")
print("c. Luna")
print("d. Neville")
answer13=input("What is the correct answer? ")
if answer13=="b" or answer13=="B" or answer13=="b." or answer13=="B.":
    correct_answer(housename)
    score=point_score(score)
else:
    incorrect_answer(housename)
#Fourteenth Question
print("Finally, in 'The Deathly Hallows Part 2', who kills Nagini the snake, aka one of the Horcruxes?")
print("a. Fred")
print("b. Ron")
print("c. Harry")
print("d. Neville")
answer14=input("What is the correct answer? ")
if answer14=="d" or answer14=="D" or answer14=="d." or answer14=="D.":
    correct_answer(housename)
    score=point_score(score)
else:
    incorrect_answer(housename)
#Ending
print("Congradulations! Time to tally up your score...")
print (score)
print("Thank you for playing, " + housename)
print("Until we meet again!")
print("\n")
#Credits and Citations/Sources
print("----------------------------------------------------------------------------------------------------------------------------")
print("This quiz was written by Jia Hwang '23")
print("\n")
print("Works cited:")
print("Rowling, J. K., author. Harry Potter And the Sorcerer's Stone. New York :Arthur A. Levine Books, 1998.")
print("Rowling, J. K. Harry Potter And the Chamber of Secrets. New York :Scholastic, Inc., 2000.")
print("Rowling, J. K. Harry Potter And The Prisoner Of Azkaban. New York : Arthur A. Levine Books, 1999.")
print("Rowling, J. K., author. Harry Potter And the Goblet of Fire. New York :Scholastic, 2002.")
print("Rowling, J. K. Harry Potter And the Order of the Phoenix. New York :Listening Library, 2003.")
print("Rowling, J. K. Harry Potter And the Half-Blood Prince. New York :Listening Library, 2005.")
print("Rowling, J. K. Harry Potter And the Deathly Hallows. New York, NY :Arthur A. Levine Books, 2007.")
