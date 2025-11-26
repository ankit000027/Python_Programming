import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

random_word = random.choice(word_list)
spaces = ["_"]*len(random_word)


life = 7

while life>0 and "_" in spaces:
    guess = input("Guess the letter: ").lower()

    if guess not in random_word or guess in spaces:
        life-=1
        print("Incorrect")
        print(f"*********************(life remaining:{life})*********************")
        print(stages[life])
        print("\n",spaces)

    elif guess in random_word:
        print("Correct")
        for i in range(len(random_word)):
            if guess==random_word[i]:
                spaces[i]=guess
        print(spaces)

if life==0:
    print(f"You lost!! The word was {random_word}")

else:
    print(f"You won!! The word was {random_word}")