# 1/28

class Card:
	ranks = ["Ace","2","3","4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
	suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __repr__(self):     
		return self.ranks[self.rank] + " of " + self.suits[self.suit]

	def __eq__(self,other):
		return self.rank == other.rank and self.suit == other.suit

	def __lt__(self,other):
		selfrank = 13 if self.rank == 0 else self.rank
		otherrank = 13 if other.rank == 0 else other.rank
		return selfrank < otherrank 

import random
class Deck:
	def __init__(self):
		self.cards = [Card(rank,suit) for rank in range(13) \
		for suit in range(4)]


	def __str__(self):
		return f"A deck of {len(self.cards)} cards."

	def print_all(self):
		print("Here is the deck of cards")
		for card in self.cards:
			print(card)

	def shuffle(self):
		num_cards = len(self.cards)
		for i in range(num_cards):
			j = random.randint(0, num_cards-1)
			(self.cards[i], self.cards[j]) = \
			(self.cards[j], self.cards[i]) 

	def deal_random(self):       # removes card after dealing
		random_place = random.randint(0, len(self.cards)-1)
		dealt_card = self.cards[random_place]
		del self.cards[random_place]
		return dealt_card

	def change_suit(self):
		for card in self.cards:
			card.suit = (card.suit + 1 if card.suit != 3 else 0)


mydeck = Deck()
print(mydeck)
print(mydeck.cards[:3])

my_hand = [card for card in [mydeck.deal_random(), mydeck.deal_random(), mydeck.deal_random(), mydeck.deal_random(), mydeck.deal_random()]]
print(my_hand)

mydeck.change_suit()
print(mydeck.print_all())

