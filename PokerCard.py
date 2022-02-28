import random
from collections import Counter

from cv2 import CAP_PROP_XI_HDR_T2
def number_to_card(card):
    suit = int(card / 13)
    if (suit == 0):
        return ( card_num_value(card % 13) + " Spade" )
    elif (suit == 1):
        return ( card_num_value(card % 13) + " Diamond" )
    elif  (suit == 2):
        return ( card_num_value(card % 13) + " Club" )
    else:
        return ( card_num_value(card % 13) + " Heart" )

def card_num_value(card):
    if card == 12: return 'Ace'
    elif card == 11: return 'King'
    elif card == 10: return 'Queen'
    elif card == 9: return 'Jack'
    else: return str(card+2)
        
def hand_value_string(value):
    if value == 0: return 'High Card'
    elif value == 1: return 'Pair'
    elif value == 2: return 'Two Pair'
    elif value == 3: return 'Three of a Kind'
    elif value == 4: return 'Straight'
    elif value == 5: return 'Flush'
    elif value == 6: return 'Full House'
    elif value == 7: return 'Four of a Kind'
    elif value == 8: return 'Straight Flush'

def convert_poker_hand_list(hand):
    return [number_to_card(i) for i in hand]


#check for flush hand

def flush_hand(hand):
    cards_suit = int(hand[0]/13)
    for i in hand:
        if (not(cards_suit == int(i/13))):
            return 0
    #ordered_flush = [int(i%13) for i in hand]
    #ordered_flush.sort(reverse = True)
    return 5

#check for straight hand

def straight_hand(hand):
    ordered_straight = [int(i%13) for i in hand]
    if ordered_straight == [12,3,2,1,0]:
        return 4
    #print(ordered_straight)
    for i in range(0,len(ordered_straight)-1):
        if not ordered_straight[i] == ordered_straight[i+1]+1:
            return 0
    return 4

#check for straight flush hand

def straight_flush_hand(hand):
    straight = straight_hand(hand)
    flush = flush_hand(hand)
    #hand.sort(reverse = True)
    if flush and straight:
        return 8
    return 0


#check for three of a kind

def three_of_kind_hand(hand):
    temp_hand = [i%13 for i in hand]
    #temp_hand.sort(reverse = True)
    #print(temp_hand)
    for i in temp_hand[:3]:
        #print(temp_hand.count(i))
        if (temp_hand.count(i) == 3):
            return 3
    return 0

#check for four of a kind

def four_of_kind_hand(hand):
    temp_hand = [i%13 for i in hand]
    #temp_hand.sort(reverse = True)
    #print(temp_hand)
    for i in temp_hand[:2]:
        #print(temp_hand.count(i))
        if (temp_hand.count(i) == 4):
            return 7
    return 0

#check for pair in hand

def pair_hand(hand):
    temp_hand = [i%13 for i in hand]
    #temp_hand.sort(reverse = True)
    for i in temp_hand[:4]:
        if (temp_hand.count(i) == 2):
            return 1
    return 0

#check for two pair in hand

def two_pair_hand(hand):
    #hand.sort(reverse = True)
    temp_hand = [i%13 for i in hand]
    counts = Counter(temp_hand)
    values = list(counts.values())
    if values.count(2) == 2:
        return 2
    return 0

#check for a full house

def full_house_hand(hand):
    #hand.sort(reverse = True)
    three = three_of_kind_hand(hand)
    pair = pair_hand(hand)
    if pair and three:
        return 6
    return 0

def hand_value(hand):
    hand.sort(reverse = True)
    value = max((pair_hand(hand),two_pair_hand(hand),three_of_kind_hand(hand),straight_hand(hand),flush_hand(hand),full_house_hand(hand),four_of_kind_hand(hand),straight_flush_hand(hand)))
    value_hand = [card%13 for card in hand]
    value_hand, hand = zip(*sorted(zip(value_hand,hand),key = lambda x : x[0],reverse = True))
    if (value == 4 or value == 8) and hand[0] == 12:
        if hand[1:] == [3,2,1,0]:
            hand[0],hand[4] = hand[4],hand[0]
    return value, value_hand,hand

def best_hand(hand1,hand2):
    hand1_value, check_hand1, hand1 = hand_value(hand1)
    hand2_value, check_hand2, hand2 = hand_value(hand2)
    print("Hand 1 is: " + str([number_to_card(i) for i in hand1]))
    print("Hand 1 value is: "+hand_value_string(hand1_value))

    print("Hand 2 is: "+str([number_to_card(j) for j in hand2]))
    print("Hand 2 value is: "+hand_value_string(hand2_value))

    if hand1_value > hand2_value:
        return "Hand 1 wins"
    elif hand1_value < hand2_value:
        return "Hand 2 wins"
    else:
        for card1,card2 in zip(check_hand1,check_hand2):
            if card1 > card2:
                return "Hand 1 wins"
            elif card1 < card2:
                return "Hand 2 wins"
        return "Push"
    
from itertools import combinations
from tqdm import tqdm
if __name__ == "__main__":
    for i in range(0,52):
        print(str(i)+". "+number_to_card(i))

    deck_of_cards = []
    for i in range(0,52):
        deck_of_cards.append(i)
    straight_count,two_pair_count,four_count, three_count,pair_count,flush_count, straight_flush_count, full_house_count, hand_count  = 0,0,0,0,0,0,0,0,0
   
    for i in tqdm(combinations(deck_of_cards,5),total = 2598960 ):
        value , x, y= hand_value(list(i))
        if value == 1:
            pair_count += 1
        elif value == 2:
            two_pair_count += 1
        elif value == 3:
            three_count += 1
        elif value == 4:
            straight_count += 1
        elif value == 5:
            flush_count += 1
        elif value == 6:
            full_house_count += 1
        elif value == 7:
            four_count += 1
        elif value == 8:
            straight_flush_count += 1
        else:
            hand_count += 1

    print("Number of possible straights are: "+str(straight_count))
    print("Number of possible two pairs are: "+str(two_pair_count))
    print("Number of possible four of a kinds are : "+str(four_count))
    print("Number of possible three of a kinds are : "+str(three_count))
    print("Number of possible pairs are: "+str(pair_count))
    print("Number of possible flushes are: "+str(flush_count))
    print("Number of possible straight flushes "+str(straight_flush_count))
    print("Number of possible full houses are: "+str(full_house_count))
    print("The rest of the hands are: "+str(hand_count))


    for i in range(10):
        hand1 = set()
        hand2 = set()
        while len(hand1) != 5 or len(hand2) != 5:
            card1 = random.randint(1,51)
            card2 = random.randint(1,51)
            if len(hand1) < 5: hand1.add(card1)
            if len(hand2) < 5: hand2.add(card2)
        print(best_hand(list(hand1),list(hand2))+"\n")
