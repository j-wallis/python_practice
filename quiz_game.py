#greeting
print("Welcome to my computer quiz!")

#asks user if they want to play, accepts an input and converts it to lowercase
playing = input("Do you want to play? ").lower()

#check if player wants to play
if playing != "yes":
    quit()

#greeting into game
print("Okay! Let's play :)")


#initializes a score
score = 0

#Asks user the first question and converts to lowercase
answer = input("What does CPU stand for? ").lower()

#check if answer is correct then let them know
if answer == "central processing unit":
    print("Correct!")
    #increment score if they got it right
    score += 1
else:
    print("Incorrect!")
    
#Asks second question and converts to lower case
answer = input("What does GPU stand for? ").lower()

#check if answer is correct then let them know
if answer == "graphics processing unit":
    print("Correct!")
    #increment score if they got it right
    score += 1
else:
    print("Incorrect!")
    
#Asks third question and converts to lower case
answer = input("What does RAM stand for? ").lower()

#check if answer is correct then let them know
if answer == "random access memory":
    print("Correct!")
    #increment score if they got it right
    score += 1
else:
    print("Incorrect!")
    
#Asks fourth question and converts to lower case
answer = input("What does PSU stand for? ").lower()

#check if answer is correct then let them know
if answer == "power supply":
    print("Correct!")
    #increment score if they got it right
    score += 1
else:
    print("Incorrect!")
    
#Tells user their score
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%")
