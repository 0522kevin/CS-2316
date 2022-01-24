# 1/24

class Phone:

    # Defines characteristics / attributes
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    # Defines behaviors / methods
    def drop_price(self): 
        self.price -= 25

phone1 = Phone("Apple", "iPhone XR", 999)
print(phone1.price) # 999

phone1.drop_price()
print(phone1.price) # 974

phone2 = Phone("Apple", "iPhone XR", 999)
print(phone1 == phone2) # False whether all variables are the same or not

phone1 = phone2
print(phone1 == phone2) # True because two objects point the same memory address

# Dunder methods
# __init__ assings attributes to an object
# __eq__ is called when the == and != operator are used comparing objects
# __lt__ is called when < operator is used to compare objects
    # Both sort() and sorted() uses __lt__ when sorting lists
# __repr is called when an object is printed or casted to a string
    # or when it is a part of a compound data structure that is printed or casted to a string
# __str__ is called when an object is printed or casted to a string

class Card:

    # Suits are defaulted to spades for now
    def __init__(self, rank):
        self.suit = "Spades"
        self.rank = rank

    def __rep_(self):
        print(f"{self.rank} of {self.suit}")

    # Two Card objects are equal if and only if their ranks and suits are equal to each other
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    # Only prints ranks of cards
    def __repr__(self):
        return str(self.rank)

    # Compares cards based on their ranks only
    def __lt__(self, other):
        if str(self.rank).isdigit() == False and str(other.rank).isdigit() == False:
            if other.rank == "Ace":
                return False
            elif other.rank == "King" and (self.rank == "King" or self.rank == "Queen" or self.rank == "Jack"):
                return False
            elif other.rank == "King" and self.rank == "Ace":
                return True
            elif other.rank == "Queen" and (self.rank == "Queen" or self.rank == "Jack"):
                return False
            elif other.rank == "Queen" and (self.rank == "Ace" or self.rank == "King"):
                return True
            elif other.rank == "Jack" and self.rank == "Jack":
                return False
            elif other.rank == "Jack" and (self.rank == "Ace" or self.rank == "King" or self.rank == "Queen"):
                return True
        elif str(self.rank).isdigit() and str(other.rank).isdigit() == False:
            return False
        elif str(self.rank).isdigit() == False and str(other.rank).isdigit():
            return True
        else:
            if int(self.rank) < int(other.rank):
                return True
            else:
                return False;

card1 = Card("Ace")
card2 = Card("Ace")

print(card1 == card2) # True because overridden __eq__() compares whether suits and ranks are the same

# Sorts the list of cards based on their ranks
card_list = [Card("2"), Card("King"), Card(9), Card("Queen"), Card("10"), Card("Jack"), Card("2"), Card(3), Card("4"), Card(5), Card("6"), Card("Ace"), Card(7), Card("8")]
print(sorted(card_list)) # [Ace, King, Queen, Jack, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
