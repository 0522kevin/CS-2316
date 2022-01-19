##################################
#          Instructions          #
##################################
'''
For each of the following functions in PE01,
replace each `pass` statement with your solution code according
to the provided instructions. You may use the test cases
in the bottom `if __name__ == "__main__"` section of this file in
order to test your code.
'''

def spring_2022():
    """
    Question 0
    Print the exact string, "Welcome to CS2316"

    >>> spring_2022()
    'Welcome to CS2316'
    """
    print("Welcome to CS2316")


def remove_upper(provided_string):
    """
    Question 1
    Return a single string with *only* lowercase characters from the provided string.

    >>> remove_upper("ePnJcKrHHypFTtion")
    'encryption'
    >>> remove_upper("HHZreppinLIH404")
    'reppin'
    """
    temp = ""
    for letter in provided_string:
        if letter.isupper() == False:
            if letter.isalpha() == True:
                temp += letter
    return temp


def remove_duplicates(iterable):
    """
    Question 2
    Return a list of the non-duplicate items from the parameter 'iterable'.

    >>>  remove_duplicates(["Nate", "Nate", "Cassie", "Maddie", "Rue"])
    ["Nate", "Cassie", "Maddie", "Rue"]
    >>> remove_duplicates([1, 3, 1,  4, 1.0, True, 5])
    [1, 3, 4, 5]
    """
    temp_list = []
    for item in iterable:
        if item not in temp_list:
            temp_list.append(item)
    return temp_list


def sauce(sauce_dict, budget):
    """
    Question 3
    Given a dictionary of sauces with the sauce name as the key and the price as the value,
    return a list of the sauces names with a price less than your budget

    >>> sauce({'mayo': .50, 'chickfila sauce': 5.30, 'honey mustard': 3.15}, 3.00)
    ['mayo']
    """
    temp_list = []
    for key in list(sauce_dict.keys()):
        if float(sauce_dict[key]) <= float(budget):
            temp_list.append(key)
    return temp_list            


def lottery_winner(car_list):
    """
    Question 4
    You have just won the lottery and are looking to buy a rare hypercar.
    You care about exclusivity and so want the rarest car out there.
    Given a list of tuples ("car name", "price", production number, "release date") return a string with the car with the smallest production run.

    >>> car_list = [("Bugatti Chiron", "$3,000,000", 500, "June 2018"), ("Koenigsegg Regera", "$1,900,000", 80, "March 2016"),
                    ("Rimac Nevera", "$2,400,000", 150, "August 2021"),("Pagani Huayra", "$2,400,000", 40, "January 2011"),
                    ("Apollo Intensa Emozione", "$3,000,000", 10, "October 2017") ]
    >>> lottery_winner(car_list)
    'Apollo Intensa Emozione'
     """

    import sys as sys
    temp = sys.maxsize
    for car in car_list:
        if car[2] < temp:
            temp = car[2]
    for car2 in car_list:
        if temp == car2[2]:
            return car2[0]


def inventory_stock(ingredients_list):
    """
    Question 5
    Your local Chick-fil-A restaurant has a shipment of ingredients coming in.
    Being the inspiring programmer you are, you want to help list inventory while
    classifying each ingredient into categories.
    There are 3 categories you want to classify ingredients into:
        1. Greens
        2. Meat
        3. Seasoning
    Return a dictionary that keeps track of the number of ingredients that fall
    under each category ("Greens", "Meats", "Seasonings") for each ingredient 
    listed within `ingredients_list`.
    You may assume there will be at least 1 ingredient listed for each category.
    The category will always be included in the ingredient name.

    >>> ingredients_list = ["Lettuce Greens", "Chicken Meat", "Bacon Meat", 
                            "Romaine Greens", "Red Cabbage Greens",
                            "Sea Salt Seasoning", "Lemon Garlic Seasoning"]
    >>> stock = inventory_stock(ingredients_list)
    >>> stock
    {'Greens': 3, 'Meat': 2, 'Seasoning': 2}
    """
    ingredients_dict = {}
    int_greens = 0
    int_meat = 0
    int_seasoning = 0
    for ingredient in ingredients_list:
        if "Greens" in ingredient:
            int_greens += 1
        elif "Meat" in ingredient:
            int_meat += 1
        else:
            int_seasoning += 1
    ingredients_dict["Greens"] = int_greens
    ingredients_dict["Meat"] = int_meat
    ingredients_dict["Seasoning"] = int_seasoning
    return ingredients_dict




if __name__ == "__main__":
    #######################################
    #          Testing your code          #
    #######################################
    """
    To test your code locally, uncomment out the functions that you wish to test below.
    Once you have uncommented the functions you want to test, run this PE01.py file 
    via Terminal/Command Prompt in order to see the outputs. Confirm if the outputs
    make the correct solutions listed above.
    """


    ##### Question 0 #####
    spring_2022()


    ##### Question 1 #####
    print(remove_upper("ePnJcKrHHypFTtion"))
    print(remove_upper("HHZreppinLIH404"))


    ##### Question 2 #####
    print(remove_duplicates(["Nate", "Nate", "Cassie", "Maddie", "Rue"]))
    print(remove_duplicates([1, 3, 1,  4, 1.0, True, 5]))


    ##### Question 3 #####
    print(sauce({'mayo': .50, 'chickfila sauce': 5.30, 'honey mustard': 3.15}, 3.00))


    ##### Question 4 #####
    car_list = [("Bugatti Chiron", "$3,000,000", 500, "June 2018"),
                ("Koenigsegg Regera", "$1,900,000", 80, "March 2016"),
                ("Rimac Nevera", "$2,400,000", 150, "August 2021"),
                ("Pagani Huayra", "$2,400,000", 40, "January 2011"),
                ("Apollo Intensa Emozione", "$3,000,000", 10, "October 2017") ]
    print(lottery_winner(car_list))


    ##### Question 5 #####
    ingredients_list = ["Lettuce Greens", "Chicken Meat", "Bacon Meat", 
                        "Romaine Greens", "Red Cabbage Greens",
                        "Sea Salt Seasoning", "Lemon Garlic Seasoning"]
    print(inventory_stock(ingredients_list))
