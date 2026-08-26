import random

words = ["school","college","python","apple","mango"]
word = random.choice(words)
display = ["_"]*len(word)
wrong_guesses= 0 
guessed_letters = []

print("=====HANGMAN GAME=====")

while wrong_guesses < 6:
    print("Word :"," ".join(display))
    guess = input ("Guess a letter :").lower()

    #Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Enter single letter!")
        continue

    #check repeated guess
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue
    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
        for i in range (len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        wrong_guesses+= 1
        print("Wrong guess!")
        print("Wrong guess :",wrong_guesses,"/6")
    print()

    if "_" not in display:
        print("Word :"," ".join(display))
        print("Congratulations!")
        print("You won!")
        break

if wrong_guesses == 6:
    print("Game over")
    print("You lost")
    print("The word was :",word)