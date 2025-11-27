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

if bidders:
    max_val = max(bidders, key=bidders.get)
    print(f"The bidding is won by {max_val} with the highest bid of ${bidders[max_val]}")
else:
    print("No bids were placed.")
