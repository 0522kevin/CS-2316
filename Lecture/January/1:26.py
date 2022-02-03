# 1/26

import copy
alist = [1,2,3,4,[5,6]]
blist = copy.copy(alist)
alist[0] = 9
alist[4][0] = 9
print(blist) # [1, 2, 3, 4, [9, 6]]

class Card:

    def __init__(self, rank, suit):
        
        # Assigns rank
        if str(rank).isdigit():
            self.rank = rank
        else:
            if rank == "Ace":
                self.rank = 1
            elif rank == "Jack":
                self.rank = 11
            elif rank == "Queen":
                self.rank = 12
            elif rank == "King":
                self.rank = 13
            else:
                # Should not be reached
                self.rank = 2

        # Assigns suit
        if suit == 1:
            self.suit = "Clubs"
        elif suit == 2:
            self.suit = "Diamonds"
        elif suit == 3:
            self.suit = "Hearts"
        elif suit == 4:
            self.suit = "Spades"
        else:
            # Should not be reached
            self.suit = "Clubs"

    def __repr__(self):
        if self.rank == 1 or self.rank == 11 or self.rank == 12 or self.rank == 13:
            if self.rank == 1:
                return "Ace of " + str(self.suit)
            elif self.rank == 11:
                return "Jack of " + str(self.suit)
            elif self.rank == 12:
                return "Queen of " + str(self.suit)
            elif self.rank == 13:
                return "King of " + str(self.suit)
        else:
            return str(self.rank) + " of " + str(self.suit)

    def __str__(self):
        if self.rank == 1 or self.rank == 11 or self.rank == 12 or self.rank == 13:
            if self.rank == 1:
                return "Ace of " + str(self.suit)
            elif self.rank == 11:
                return "Jack of " + str(self.suit)
            elif self.rank == 12:
                return "Queen of " + str(self.suit)
            elif self.rank == 13:
                return "King of " + str(self.suit)
        else:
            return str(self.rank) + " of " + str(self.suit)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if other.rank == 1:
            if self.rank == 1:
                if self.suit > other.suit:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if self.rank == 1:
                return True
            else:
                if self.rank > other.rank:
                    return True
                elif self.rank == other.rank:
                    if self.suit > other.suit:
                        return True
                    else:
                        return False
                else:
                    return False

card1 = Card(1, 4)
card2 = Card(1, 3)
print(card1 if card1 > card2 else card2)

card3 = Card(1, 2)
card4 = Card(1, 1)
card5 = Card(10, 3)
card_list = [card1, card2, card3, card4, card5]
print(sorted(card_list))
