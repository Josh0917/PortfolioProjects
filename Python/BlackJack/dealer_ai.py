#Blackjack Dealer AI Start
def next_move(a_string):
    hand_total = 0
    a_count = 0
    for i in a_string:
        if i == "K" or i == "Q" or i == "J":
            hand_total += 10
        elif i != "A":
            hand_total += int(i)
        elif i == "A":
            a_count += 1
    if a_count > 0:
        while a_count > 0:
            if (hand_total + 11) > 21:
                hand_total += 1
                a_count -= 1
            else:
                hand_total += 11
                a_count -= 1
    if hand_total in range(0,17):
        return "Hit"
    elif hand_total in range(17,22):
        return "Stay"
    else:
        return "Bust"