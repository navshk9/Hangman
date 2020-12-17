#array of words
easyWords = ["cat", "dog", "hat", "fit", "sit"]
hardWords = ["elephant", "microwave", "television", "computer", "breakfast"]

#user selects difficulty
difficulty = input("""
Select a difficulty
1.Easy (press 1)
2.Hard (press 2)
""")

#randomly selecting a word from array of selected difficulty
import random
if int(difficulty) == 1:
    password = random.choice(easyWords)
elif int(difficulty) == 2:
    password = random.choice(hardWords)
else:
    print("Incorrect selection, choosing Easy words for you....")

#create an array of letters from the word
wordLetters = []
for i in range(0,len(password)):
    wordLetters.append(password[i])

#array for correctly guessed words
blanks = []
for i in range(0,len(password)):
    blanks.append("_")

numOfGuesses = 5 #number of guesses given to user
isGuessed = False #initially word is not guessed

#game loop
while numOfGuesses > 0 and isGuessed == False:
    print("Tries left: " + str(numOfGuesses)) #prints number of tries

    #prints contents of blanks array
    for i in range(0,len(blanks)):
        print(blanks[i], end=" ")

    #user is prompted to enter a letter to guess    
    guess = input("\nEnter a letter to guess: ")

    #if user input is not in wordLetters array, print error and take away a try
    if guess not in wordLetters: 
        print("Incorrect guess, try again.")
        numOfGuesses-=1
    else:
        #if letter has already been guessed, do not take away tries and display error
        if guess in blanks:
            print("'" +str(guess)+ "' has already guessed, please try a different letter.")
        else:
            #if user guess matches the word at index i, replace blanks array with guess at index i
            for i in range(0, len(wordLetters)):
                if(guess == wordLetters[i]):
                    blanks[i] = guess

    #if wordLetters and blanks array match, the word has been guessed and the loop ends
    if (wordLetters == blanks):
        isGuessed = True

#if user guesses the word 
if isGuessed == True:
    print(password)
    print("Congratulations! You guessed the word.")

#if user runs out of tries
if numOfGuesses == 0:
    print("You ran out of tries. The word was '" +str(password)+ "'. Better luck next time.")


