# Interactive console for Trivial Purfuit to display skeleton capability
import sys
import requests
import json

url = "http://127.0.0.1:5000/question/random_question"
url_die = "http://127.0.0.1:5000/roll"

print("Welcome to Trivial Purfuit Interactive Console!")
print("This console allows you to interact with the skeleton increment of the Trivial Purfuit software")
name = input ("Please enter your name :") 
print("")
print("Hi "+name+"!  Welcome to the interactive console.") 
counter = 0 #setup a counter to count total questions
correct = 0 #setup a counter to count correct questions
incorrect = 0 #setup a counter to count incorrect questions
spacesMoved = 0 #setup a counter to count total spaces moved
quit = False

while (quit == False): #loop to allow for exit (check if quit game is true/false?)
    print(" ")
    print("--- Main Menu--- ")
    print("1. Answer a trivia question!")
    print("2. View metrics")
    print("3. Quit game")
    choice = input ("Please choose from above: ")

    if (choice == "1"):
        counter = counter + 1 #increment question total
        print(" ")
        print("...fetching question from Database of Questions")
        #print("...NOTE: Category not selected")
        
        #send http request to DB to get question data
        sendRequest = requests.get(url = url)
        DB_Data = sendRequest.json()
        print("...question retrieved successfully!")
        print("")

        #extract question data for display & use
        Question = DB_Data["question"]
        Category = DB_Data["category_id"]
        AnswerChoices = DB_Data["possible_answers"]
        CorrectAnswer = DB_Data["correct_answer"]
        print("Question #",counter)#,", pulled from Category ",Category)
        print("*** ",Question," ***")
        AnswerChoices[0] = "a ", AnswerChoices[0]
        AnswerChoices[1] = "b ", AnswerChoices[1]
        AnswerChoices[2] = "c ", AnswerChoices[2]
        AnswerChoices[3] = "d ", AnswerChoices[3]
        for key in range(len(AnswerChoices)):
            print(AnswerChoices[key])

        #stuff to match the correct letter to the correct answer
        choice = input("Please choose a, b, c, or d:")
        CorrectChoiceIndex = AnswerChoices[1].index(CorrectAnswer)
        CorrectChoiceLetter = AnswerChoices[CorrectChoiceIndex][0].strip()

        if CorrectChoiceLetter == choice:
            print("Correct Answer!")
            correct = correct + 1
            
            input("Press a button to roll the die!")
            print("...rolling die")
            #call roll die API
            dieRequest = requests.get(url = url_die)
            diedata = dieRequest.json()
            dieside = diedata["dice"]
            dieValue = dieside[0].get('value')
            print("...die rolled successfully")
            print("You rolled a ",dieValue,"!")
            spacesMoved = spacesMoved + dieValue
        else:
            print("Incorrect answer")
            incorrect = incorrect + 1
        print("The correct answer is: ",CorrectAnswer)
        input("Press a key to continue...")

    elif (choice == "2"):
        #display person's name, how many correct incorrect answers, and how long they've been playing?
        print(" ")
        print("Here are your current stats:")
        print("Total questions answered: ",counter)
        print("Questions answered correctly: ",correct)
        print("Questions answered incorrectly: ",incorrect)
        print("Total number of spaces moved: ",spacesMoved)
        input("Press a key to continue...")

    elif (choice == "3"):
        #set quit game check to value to break the loop
        print(" ")
        print("------------------------------------------")
        print("Here are your final stats:")
        print("Total questions answered: ",counter)
        print("Questions answered correctly: ",correct)
        print("Questions answered incorrectly: ",incorrect)
        print("Total number of spaces moved: ",spacesMoved)
        print("------------------------------------------")
        sys.exit("Thanks for playing "+name+"!")
    else:
        #later can do input validation, but let's just ask to quit if they don't enter 1,2, or 3
        print(" ")
        choice = input ("Invalid entry, would you like to exit (y/n)? ")
        if (choice == "y"): 
            #Quit
            sys.exit("Thanks for playing!")