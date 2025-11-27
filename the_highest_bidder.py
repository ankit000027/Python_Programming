def details():
    while True:
        name = input("Enter bidder name: ")
        price = int(input("Enter bid amount: "))
        bidders[name] = price

        answer = input("Is there any other bidder? (yes/no): ").lower()
        if answer != "yes":
            break

        print("\n" * 20)

bidders = {}
details()
max_value= 0
winner= ""

for key in bidders:
    if bidders[key] > max_value:
        max_value=bidders[key]
        winner = key

print(f"The winner of the bidding is {winner} with a massive bid of ${max_value}")