import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)


life=len(chosen_word)
display = ["_"]*life


while life!=0 and "_" in display:
    guess_letter = input("Guess the letter: ").lower()


    if guess_letter in display:
        print("Word already found")
        life -= 1
        print(f"Wrong..You have {life} chances left")


    elif guess_letter in chosen_word :
        print("Correct!!")
        for i in range(len(chosen_word)):
            if chosen_word[i]==guess_letter:
                display[i]=chosen_word[i]
        print(display)


    else:
        life-=1
        print(f"Wrong..You have {life} chances left")

if "_" not in display:
    print("You saved the hangman..")
    print(f"The word was: "+"".join(display))


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
