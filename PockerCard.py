import random

def number_to_card(card):
    suit = int(card / 13)
    if (suit == 0):
        return ( str(card% 13) + "Spade" )
    elif (suit == 1):
        return ( str(card % 13) + "Diamond" )
    elif  (suit == 2):
        return ( str(card % 13) + "Club" )
    else:
        return ( str(card % 13) + "Heart" )

def convert_poker_hand_list(hand):
    return [number_to_card(i) for i in hand]


#check for flush hand

def flush_hand(hand):
    cards_suit = int(hand[0]/13)
    for i in hand:
        if (not(cards_suit == int(i/13))):
            return False
    return True

#check for straight hand

def straight_hand(hand):
    lowest_card = min(hand)% 13
    for i in hand[1:]:
        print(str(lowest_card) + " " + str(i%13))
        if (not ((lowest_card + 1) == i%13)):
            return False
        lowest_card += 1
    return True

#check for straight flush hand

def straight_flush_hand(hand):
    return (straight_hand(hand) and flush_hand(hand))


#check for three of a kind

def three_of_kind_hand(hand):
    temp_hand = [i%13 for i in hand]
    print(temp_hand)
    for i in temp_hand[:3]:
        print(temp_hand.count(i))
        if (temp_hand.count(i) == 3):
            return True
    return False

#check for four of a kind

def four_of_kind_hand(hand):
    temp_hand = [i%13 for i in hand]
    print(temp_hand)
    for i in temp_hand[:2]:
        print(temp_hand.count(i))
        if (temp_hand.count(i) == 4):
            return True
    return False

#check for pair in hand

def pair_hand(hand):
    temp_hand = [i%13 for i in hand]
    print(temp_hand)
    for i in temp_hand[:4]:
        print(temp_hand.count(i))
        if (temp_hand.count(i) == 2):
            return True
    return False

#check for two pair in hand

def two_pair_hand(hand):
    temp_hand = [i%13 for i in hand]
    print(temp_hand)
    for i in temp_hand[:1]:
        print(i)
        if (temp_hand.count(i) == 2):
            hand_without_second_pair = list(filter(lambda a: a != i, temp_hand))
            print(hand_without_second_pair)
            for i in hand_without_second_pair[:2]:
                if (hand_without_second_pair.count(i) == 2):
                    return True
    return False

#check for a full house

def full_house_hand(hand):
    return (three_of_kind_hand(hand) and pair_hand(hand))


if __name__ == "__main__":
    for i in range(0,52):
        print(str(i)+". "+number_to_card(i))

    hand_one = [int(i) for i in input().split()]

    print("")
    print("Is the hand a STRAIGHT: ")
    print(straight_hand(hand_one))
    print("\nIs the hand a FLUSH:")
    print(flush_hand(hand_one))
    print("\n Is the hand a STRAIGHT FLUSH: ")
    print(straight_flush_hand(hand_one))
    print("\nIs the hand a THREE OF A KIND: ")
    print(three_of_kind_hand(hand_one))
    print("\nIs the hand a FOUR OF A KIND: ")
    print(four_of_kind_hand(hand_one))
    print("\nDoes the hand have a PAIR: ")
    print(pair_hand(hand_one))
    print("\nDoes the hand have a TWO PAIR: ")
    print(two_pair_hand(hand_one))
    print("\nDoes the hand have a FULL HOUSE: ")
    print(full_house_hand(hand_one))
    print("")
    print(hand_one)
    print(convert_poker_hand_list(hand_one))





    

