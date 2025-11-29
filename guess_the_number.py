import random

answer = random.randint(1,100)
print(answer)
easy_hard = input("Easy or Hard?").lower()

def guess(num):
    for i in range(num):
        user_answer = int(input(f"You have {num-i} attempts left, You have to guess a number between 1-100: "))
        if user_answer == answer:
            return user_answer
        elif user_answer>answer:
            print("too high")
        elif user_answer<answer:
            print("Too low")
    return False

if easy_hard == "easy":
    easy_result=guess(10)
    if easy_result==False:
        print("Better luck next time")
    else:
        print(f"You won the answer was {answer}")
elif easy_hard == "hard":
    hard_result=guess(5)
    if hard_result==False:
        print("Better luck next time")
    else:
        print(f"You won the answer was {answer}")