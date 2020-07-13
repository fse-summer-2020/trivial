# Interactive console for Trivial Purfuit to display skeleton capability
import sys

print("Welcome to Trivial Purfuit Interactive Console!")
print("This console allows you to interact with the skeleton increment of Samthe Trivial Purfuit software")
name = input ("Please enter your name :") 
print("Hi "+name+", welcome to the game.") 
counter = 0 #setup a counter to count total questions
correct = 0 #setup a counter to count correct questions
incorrect = 0 #setup a counter to count incorrect questions
quit = False

while (quit == False): #loop to allow for exit (check if quit game is true/false?)
    print(" ")
    print("--- Main Menu--- ")
    print("1. Give me a question!")
    print("2. View metrics")
    print("3. Quit game")
    choice = input ("Please choose from above: ")

    if (choice == "1"):
        counter = counter + 1
        #put some text about question screen / can label this is your X question!
        #contact data layer to get question 
        #say if it was successful
        print(" ")
        print("Here is question",counter,"!")
        print("This will show a question once the data layer is connected correctly")
        input("Press a key to continue...")

    elif (choice == "2"):
        #display person's name, how many correct incorrect answers, and how long they've been playing?
        print(" ")
        print("Here are your current stats:")
        print("Total questions answered: ",counter)
        print("Questions answered correctly: ",correct)
        print("Questions answered incorrectly: ",incorrect)
        input("Press a key to continue...")

    elif (choice == "3"):
        #set quit game check to value to break the loop
        print(" ")
        print("Here are your final stats:")
        print("Total questions answered: ",counter)
        print("Questions answered correctly: ",correct)
        print("Questions answered incorrectly: ",incorrect)
        sys.exit("Thanks for playing "+name+"!")
    else:
        #later can do input validation, but let's just ask to quit if they don't enter 1,2, or 3
        print(" ")
        choice = input ("Invalid entry, would you like to exit (y/n)? ")
        if (choice == "y"): 
            #Quit
            sys.exit("Thanks for playing!")