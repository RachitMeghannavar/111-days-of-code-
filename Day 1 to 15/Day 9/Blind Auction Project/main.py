# TODO-1: Ask the user for input
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
continue_playing = True
while continue_playing:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    should_continue = input("Would you like to continue? 'yes' or 'no' ")
    if should_continue == "no":
        continue_playing = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


