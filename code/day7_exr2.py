result = 0
card_pattern = f'([0-9A-Z]{5})'
num_pattern = f'([0-9]+)'
data = open('../text/day7', 'r')

cards = {}

high = []
pair = []
two_pairs = []
three = []
full_house = []
four_kind = []
five_kind = []

next = data.readline()

def count_the_cards(cards:str):
    amount = 1
    card_type = {}
    for c in cards:
        if c != 'J':
            if c in card_type:
                card_type[c] += 1
            else:
                card_type[c] = 1
    for key, value in card_type.items():
        if value == 1:
            continue
        if value > 1 and amount < 10:
            amount *= value * 10
        elif value == 3 and amount == 20:
            amount += 15
        else:
            amount += 5
    for c in cards:
        if c == 'J' and amount < 10:
            amount += 20
        elif c == 'J':
            amount += 10

    # print(amount)
    return amount

def card_value(card):
    values = { 'J': 0,'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'Q': 10, 'K': 11, 'A': 12}
    return values[card[0]]


def group_cards(cards:str, card_type:int):
    match card_type:
        case 61:
            five_kind.append(cards)
        case 51:
            five_kind.append(cards)
        case 50:
            five_kind.append(cards)
        case 41:
            four_kind.append(cards)
        case 40:
            four_kind.append(cards)
        case 35:
            full_house.append(cards)
        case 31:
            three.append(cards)
        case 30:
            three.append(cards)
        case 25:
            two_pairs.append(cards)
        case 21:
            pair.append(cards)
        case 20:
            pair.append(cards)
        case 1:
            high.append(cards)
        case _:
            high.append(cards)


while next:
    split = next.split(' ')
    deck = split[0]
    bid = split[1].strip()
    cards[deck] = bid
    group = count_the_cards(deck)
    group_cards(deck, group)
    next = data.readline()


sorted_high = sorted(high, key=lambda x: [card_value(c) for c in x])
sorted_pair = sorted(pair, key=lambda x: [card_value(c) for c in x])
sorted_2pair = sorted(two_pairs, key=lambda x: [card_value(c) for c in x])
sorted_three = sorted(three, key=lambda x: [card_value(c) for c in x])
sorted_full = sorted(full_house, key=lambda x: [card_value(c) for c in x])
sorted_four = sorted(four_kind, key=lambda x: [card_value(c) for c in x])
sorted_five = sorted(five_kind, key=lambda x: [card_value(c) for c in x])

all_cards = sorted_high + sorted_pair + sorted_2pair + sorted_three + sorted_full + sorted_four + sorted_five

for c in range(len(all_cards)):
    singe_result = (c+1) * int(cards[all_cards[c]])
    result += singe_result

print(sorted_high)

print(result)
data.close()