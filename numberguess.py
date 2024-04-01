#import random module
import random

#accepts an input from user
top_of_range = input("Type a number: ")

#check if top of range is digit then convert to integer
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    #checks if top of range is less than or equal to zero
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()

#if top of range is not a digit requests user to type a number
else:
    print("Please type a number next time.")
    quit()
    
#generate a random number between 0 and user input
random_number = random.randint(0,top_of_range)

#initialize guesses variable
guesses = 0

while True:
    #increment guesses everytime while loop runs
    guesses += 1
    
    #accepts a guess from user
    user_guess = input("Make a guess: ")
    
    #converts guess to int
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
    #requests user to type number
    else:
        print("Please type a number next time.")
        continue
    
    #checks if guess equals random number
    if user_guess == random_number:
        print("You got it!")
        #break out of while loop because guess is correct
        break
    else:
        if user_guess > random_number:
            print("You were above the number")
        else:
            print("You were below the number!")
        
print("You got it in", guesses, "guesses")
