# TODO: Ask the user for input
#TODO: Save data into dictionary
# TODO: Whether if new bids are entered or not
# TODO: Compare bids and find the highest bid


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
bidding = True
while bidding :
    name = input("What is your name?: ")
    price = int(input("What is the price?:$ "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if should_continue == "no":
        bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)