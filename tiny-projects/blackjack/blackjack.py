def value(hand):
    """
    Calculate the value of a Blackjack hand.
    Example of a hand: [3, 7, "King"]

    Sum the value of the cards.
    Named cards are worth 10.
    The Ace is worth 1 or 11.
    Maximise the value without exceeding 21.
    """
    sum_hand = 0
    for x in hand:
        # order
        if type(x) == str and x.lower() == "ace":
            hand.append(hand.pop(hand.index(x)))

    # print(hand)

    for iter_hand, x in enumerate(hand, start=1):
        # order
        if type(x) == str and x.lower() == "ace":
            hand.append(hand.pop(hand.index(x)))

        if type(x) == str:
            if x.lower() in ["king", "queen", "jack"]:
                x = 10
                sum_hand += x
            elif x.lower() == "ace":
                x = 1 if ((sum_hand > 10 or iter_hand < len(hand)) and sum_hand != 0) else 11
                sum_hand += x
        else:
            sum_hand += x
    return sum_hand

#approx 40min


