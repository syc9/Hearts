def suit(card):	
		check_suit = card/13
		if check_suit == 0:
			return "Clubs"
		elif check_suit == 1:
			return "Diamonds"
		elif check_suit == 2:
			return "Spades"
		elif check_suit == 3:
			return "Hearts"

def value(card):
		check_value = card%13
		if check_value <= 9:
			return str(check_value + 2)
		elif check_value == 10:
			return "Jack"
		elif check_value == 11:
			return "Queen"
		elif check_value == 12:
			return "King"
		elif check_value == 13:
			return "Ace"

def name_of_card(card):
		return value(card) + " of " + suit(card)

def pointValue(card):
	points = 0;
	if(card >= 39):
		points = 1;
	if(card == 36):
		points = 13;
	return points

def winner(cardList):
	card1 = cardList[0];
	cards = cardList[1:4];
	win = 0;
	for i in range(len(cards)):
		if suit(cards[i]) == suit(card1):
			if cards[i] > card1:
				win = i+1
	return win 
