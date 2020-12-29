# Hangman

## Description
This simple Hangman game asks the user to guess a mystery word before running out of tries. The user can select the difficulty of the game in the menu
and the word would be randomly selected from an array of words. The user guesses I letter at a time.

## Sample Run
```bash
Select a difficulty
1.Easy (press 1)
2.Hard (press 2)
2
Tries left: 5
_ _ _ _ _ _ _ _
Enter a letter to guess: a
Incorrect guess, try again.
Tries left: 4
_ _ _ _ _ _ _ _
Enter a letter to guess: e
Tries left: 4
_ _ _ _ _ _ e _
Enter a letter to guess: c
Tries left: 4
c _ _ _ _ _ e _
Enter a letter to guess: c
'c' has already guessed, please try a different letter.
Tries left: 4
c _ _ _ _ _ e _
Enter a letter to guess: o
Tries left: 4
c o _ _ _ _ e _
Enter a letter to guess: t
Tries left: 4
c o _ _ _ t e _
Enter a letter to guess: g
Incorrect guess, try again.
Tries left: 3
c o _ _ _ t e _
Enter a letter to guess: m
Tries left: 3
c o m _ _ t e _
Enter a letter to guess: p
Tries left: 3
c o m p _ t e _
Enter a letter to guess: u
Tries left: 3
c o m p u t e _
Enter a letter to guess: r
computer
Congratulations! You guessed the word.
```

## What I would do to improve the application
To improve the application, I would use a file of possible words instead of an array. This would make it easier to store a large amount of possible words. I would also
add a category option to allow the user to select words from a certain category.
