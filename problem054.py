card_values = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def get_value(card: str):
    return int(card[:-1]) if card[:-1].isdigit() else card_values[card[:-1]]


# return highest card or highest 'pair'
def check_multiples(hand: list):
    card = 0
    count = 0
    super_count = 0
    for i in range(len(hand)):
        current_count = 1
        current_card = get_value(hand[i])
        for j in range(i + 1, len(hand)):
            if get_value(hand[j]) == current_card:
                current_count += 1
        if current_count > 1 and current_count == count:
            super_count += 1
        if current_count > count:
            count = current_count
            card = current_card
            super_count = 1
        elif current_count == count and current_card > card:
            card = current_card
    return count, card, super_count


# check for straight
def check_straight(hand: list):
    values = [get_value(card) for card in hand]
    values.sort()
    if values[0] == 2 and values[-1] == 14:
        values = [1] + values[:-1]
    for i in range(0, len(values) - 1):
        if values[i] + 1 != values[i + 1]:
            return False, None
    return True, values[-1]


# check for flush
def check_flush(hand: list):
    for i in range(len(hand) - 1):
        if hand[i][-1] != hand[i + 1][-1]:
            return False
    return True


# get highest_card and its position
def highest_card(hand: list):
    values = [get_value(card) for card in hand]
    return max(values), values.index(max(values))


# check Full House
def full_house(hand: list):
    count1, card1, super1 = check_multiples(hand)
    if count1 == 3:
        hand = [card for card in hand if get_value(card) != card1]
        count2, card2, super2 = check_multiples(hand)
        if count2 == 2:
            return True, card1, card2
        else:
            return False, None, None
    else:
        return False, None, None


# determine winner
def compare(hand1, hand2):
    full_house1, house11, house12 = full_house(hand1)
    full_house2, house21, house22 = full_house(hand2)
    flush1, flush2 = check_flush(hand1), check_flush(hand2)
    straight1, card_straight1 = check_straight(hand1)
    straight2, card_straight2 = check_straight(hand2)
    count1, card1, super1 = check_multiples(hand1)
    count2, card2, super2 = check_multiples(hand2)

    # first check for straight flush
    if (flush1 and straight1) and (not flush2 or not straight2):
        return 0
    if (not flush1 or not straight1) and (flush2 and straight2):
        return 1
    if flush1 and flush2 and straight1 and straight2:
        if card_straight1 == card_straight2:
            raise ValueError('Equivalent Straight Flush')
        return 0 if card_straight1 > card_straight2 else 1
        # check for four of a kind
    if count1 == 4 and count2 < 4:
        return 0
    if count2 == 4 and count1 < 4:
        return 1
    if count1 == 4 and count2 == 4:
        if card1 != card2:
            return 0 if card1 > card2 else 1
        else:
            card1 = [get_value(card) for card in hand1 if get_value(card) != card1][0]
            card2 = [get_value(card) for card in hand2 if get_value(card) != card2][0]
            return 0 if card1 > card2 else 1
    # check for full house
    if full_house1 and not full_house2:
        return 0
    if not full_house1 and full_house2:
        return 1
    if full_house1 and full_house2:
        if house11 != house21:
            return 0 if house11 > house21 else 1
        else:
            return 0 if house12 > house22 else 1
    # check for flush
    if flush1 and not flush2:
        return 0
    if not flush1 and flush2:
        return 1
    # if both have a flush it gets treated as no flush
    # check for straight
    if straight1 and not straight2:
        return 0
    if not straight1 and straight2:
        return 1
    if straight1 and straight2:
        return 0 if card_straight1 > card_straight2 else 1
    # check for multiples or highest card
    if count1 > count2:
        return 0
    elif count1 < count2:
        return 1
    elif super1 > super2:
        return 0
    elif super1 < super2:
        return 1
    else:
        if count1 > 1 and card1 == card2:
            hand1 = [card for card in hand1 if get_value(card) != card1]
            hand2 = [card for card in hand2 if get_value(card) != card1]
            count1, card1, super1 = check_multiples(hand1)
            count2, card2, super2 = check_multiples(hand2)
            if count1 > count2:
                return 0
            elif count1 < count2:
                return 1
        if card1 != card2:
            return 0 if card1 > card2 else 1
        else:
            while card1 == card2:
                hand1 = [card for card in hand1 if get_value(card) != card1]
                hand2 = [card for card in hand2 if get_value(card) != card1]
                card1, i1 = highest_card(hand1)
                card2, i2 = highest_card(hand2)
            return 0 if card1 > card2 else 1


with open('poker.txt', 'r') as f:
    lines = f.readlines()

count1 = 0
for line in lines:
    cards = line.split(' ')
    cards[-1] = cards[-1].replace('\n', '')
    if compare(cards[:5], cards[5:]) == 0:
        count1 += 1
print(count1)
