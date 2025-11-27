def add(n1, n2):
    return n1 + n2
def divide(n1,n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2
def subtract(n1,n2):
    return n1-n2

calculation = {
    "+":add,
    "-":subtract,
    "/":divide,
    "*":multiply
}

n1 = int(input("num1: "))
while True:
    operation = input("choose which operation you want to do +,-,*,/: ")
    if operation not in calculation:
        print("Enter a valid sign..")
        break
    n2 = int(input("Choose another number: "))
    answer = (calculation[operation](n1,n2))
    print(answer)
    further_calculation = input("Do you want to perform more operations? y for yes n for no: ").lower()
    if further_calculation=="y":
        n1=answer
    else:
        break

