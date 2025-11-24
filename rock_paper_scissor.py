import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock,paper,scissors]

user_input = input("Rock, Paper, scissors??\n").lower()

user_choice = ["rock","paper","scissors"]

if user_input not in user_choice:
    print("Invalid choice!!")
else:
    user_index = user_choice.index(user_input)
    comp_index = random.randint(0,2)

    print("Your Choice: ")
    print(game_list[user_index])

    print("Computer choice: ")
    print(game_list[comp_index])


#game logic
    if user_index == comp_index:
        print("Its a draw!!")

    elif (user_index == 0 and comp_index == 2) or \
         (user_index == 1 and comp_index == 0) or \
         (user_index == 2 and comp_index == 1):
        print("You win!")

    else:
        print("You lose!!")


