########
#Part 1#
########

# Replace the pass with your code according to the instructions in the HW01 Prompt
# You can use the test cases at the bottom in order to test your code

def add_digits(int_list):
    string = ""
    for integer in int_list:
        string += str(integer)
    return int(string)

def string_modifier(str_list):
    temp_list = []
    for string in str_list:
        if string.isalpha() and string.islower():
            temp_list.append(string * len(string))
    return temp_list

def contacts(phone_numbers):
    temp_list = []
    for phone_number in phone_numbers:
        string = ""
        for character in phone_number:
            if character.isdigit():
                string += character
        temp_list.append(string)
    new_list = [number for number in temp_list if len(number) == 10 if number[:3] == "404"]
    return len(set(new_list))

def shelf_books(book_list):
    return [books[0] for books in sorted(book_list, key = lambda author : (author[1].split()[-1], author[0][0]))]

def classics(books, chapters, authors):
    return {book: (True if chapter >= 20 and author != "J. Joyce" else False) for book, chapter, author in zip(books, chapters, authors)}

def writers(authors, age_at_death):
    return {(index + 1): zipped[1] for index, zipped in enumerate(sorted(zip(age_at_death, authors), reverse = True))}

########
#Part 2#
########

# Create the Book and Library classes below as specified by the HW01 prompt
# You will need to use the correct function/method names!

class Book:
    
    def __init__(self, name, genre, year, pages):
        self.name = name
        self.genre = genre
        self.year = year
        self.pages = pages

    def __lt__(self, other):
        return True if self.year < other.year else False

    def __eq__(self, other):
        return True if (self.name == other.name and self.year == other.year and self.pages == other.pages) else False

    def __repr__(self):
        return f"{self.name} is a {self.pages} pages long {self.genre} book published in {self.year}."


class Library:
    
    def __init__(self, name, book_list):
        self.name = name
        self.book_list = []
        for book in book_list:
            self.book_list.append(Book(book[0], book[1], book[2], book[3]))
        self.num_fiction = 0
        for book in self.book_list:
            if book.genre == "Fiction":
                self.num_fiction += 1

    def __repr__(self):
        return f"{self.name} is a library where {self.num_fiction} of the {len(self.book_list)} books are fiction."

    def __lt__(self, other):
        return True if self.num_fiction < other.num_fiction else False

    def add_book(self, new_book):
        self.book_list.append(Book(new_book[0], new_book[1], new_book[2], new_book[3]))
        self.num_fiction = self.num_fiction + 1 if new_book[1] == "Fiction" else self.num_fiction

if __name__ == '__main__':
    #********************************************************************************************************************
    # Uncomment the necessary lines below to test specific functions and classes in command line or terminal            #
    # After you test your functions, MAKE SURE TO RE-COMMENT OUT ALL PRINT STATEMENTS BEFORE SUBMITTING IN GRADESCOPE   #
    #********************************************************************************************************************

    # Part 1: test add_digits
    # int_list = [1, 4, 3, 8, 1]
    # print(add_digits(int_list)) # 14381
    # int_list = [6, 1, 1, 1]
    # print(add_digits(int_list)) # 6111

    # Part 1: test string_modifier
    # str_list = ['ace', 'BLuE42', 'b4a', 'cs']
    # print(string_modifier(str_list)) # ['aceaceace', 'cscs']
    # str_list = ["qwerty", "Kevin", "dksrbals522", "whatif", "what if?"]
    # print(string_modifier(str_list)) # ['qwertyqwertyqwertyqwertyqwertyqwerty', 'whatifwhatifwhatifwhatifwhatifwhatif']

    # Part 1: test contacts
    # phone_numbers = ['4o04592,,,0000', '-%#3&0&3!0', '4!0!4!5!9!2!0!0!0!0!','908',
    #                  '4###04...-,,,,,78', '404$$$193--8173', '3^^0--,30']
    # print(contacts(phone_numbers)) # 2
    # phone_numbers = ['404567891', ')))404(((', '$379XD', '4o33,0', '714---615---0294']
    # print(contacts(phone_numbers)) # 0

    # Part 1: test shelf_books
    # book_list = [('It', 'Stephen King'), ('Gone Girl', 'Gillian Flynn'), ('Verity', 'Colleen Hoover')]
    # print(shelf_books(book_list)) # ['Gone Girl', 'Verity', 'It']
    # book_list = [('The Lightning Thief', 'Rick Riordan'), ('Divergent', 'Veronica Roth'),('The Hunger Games', 'Suzanne Colins'), ('Catching Fire', 'Suzanne Colins')]
    # print(shelf_books(book_list)) # ['Catching Fire', 'The Hunger Games', 'The Lightning Thief', 'Divergent']

    # Part 1: test classics
    # books = ['Around the Moon', 'Ulysses', '1984', 'Don Quixote']
    # chapters = [25, 45, 12, 90]
    # authors = ['J. Verne', 'J. Joyce', 'G. Orwell', 'M. Cervantes']
    # print(classics(books, chapters, authors)) # {'Around the Moon': True, 'Ulysses': True, '1984': False, 'Don Quixote': True}
    # print(classics(['Frankenstein', 'Araby', 'Doctor Sleep'], [30, 1, 20], ['M. Shelley', 'J. Joyce', 'S. King'])) # {'Frankenstein': True, 'Araby': False, 'Doctor Sleep': True}

    # Part 1: test writers
    # authors = ['J. Swift', 'T. Paine', 'C. Dickens', 'H. Melville']
    # age_at_death = [78, 73, 58, 72]
    # print(writers(authors, age_at_death)) # {1: 'J. Swift', 2: 'T. Paine', 3: 'H. Melville', 4: 'C. Dickens'}

    # Part 2: Class 1
    # Book1 = Book('Normal People', 'Fiction', 2018, 273) 
    # Book2 = Book('The Catcher in the Rye', 'Fiction', 1951, 234)
    # Book3 = Book('Normal People', 'Some unknown genre', 2018, 273) 
    # print(Book1.name) # Normal People
    # print(Book1.genre) # Fiction

    # print(Book1 < Book2) # False

    # print(Book1 == Book2) # False
    # print(Book1 == Book3) # True

    # print(Book1) # Normal People is a 273 pages long Fiction book published in 2018.

    # Part 2: Class 2
    book_list = [['Normal People', 'Fiction', 2018, 273],
                 ['The Catcher in the Rye', 'Fiction', 1951, 234],
                 ['The Goal', 'Fiction', 1984, 384],
                 ['How to Think Like a Computer Scientist', 'Textbook', 2002, 274]]
    # Bohongs_Library = Library('Bohong’s Books', book_list) 
    # print(Bohongs_Library.name)

    # print(Bohongs_Library)

    Erins_Library = Library('Erin’s Excellent Essays',[['Arriving Today: From Factory to Front Door', 'Nonfiction', 2021, 384]])
    # print(Bohongs_Library < Erins_Library)
 
    book1 = ['The Hunger Games', 'Fiction', 2008, 374] 
    # Bohongs_Library.add_book(book1) 
    # print(Bohongs_Library)
