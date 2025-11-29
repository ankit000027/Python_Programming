import random

answer = random.randint(1, 100)

easy_hard = input("Easy or Hard? ").lower()


def guess(attempts):
    for i in range(attempts):
        print(f"You have {attempts - i} attempts left.")
        user_answer = int(input("Guess a number between 1-100: "))

        if user_answer == answer:
            print("Correct! 🎉")
            return True

        elif user_answer > answer:
            print("Too high.")

        else:
            print("Too low.")

    return False

if easy_hard == "easy":
    result = guess(10)
elif easy_hard == "hard":
    result = guess(5)
else:
    print("Invalid mode!")
    result = False

if result:
    print(f"You won! The answer was {answer}")
else:
    print(f"Better luck next time! The answer was {answer}")
