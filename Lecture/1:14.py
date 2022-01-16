# 1/14

# Creates a dictionary from two lists using zip
list1 = [1, 2, 3, 4]
list2 = ["one", "two", "three", "four"]
def create_d(list1, list2):
    return dict(zip(list1, list2))
print(create_d(list1, list2)) # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

d = dict(zip("brxx","lmqrs"))
print(d) # {'b': 'l', 'r': 'm', 'x': 'r'}

# Takes a list of first and last names and sorts the names based on the last name
# If key parameter is present, the elements are transformed before sorting
# and sorts based on the return value

# In this case, each element is splitted by a space, which separates first name and last name
# Then, -1 indicates the last word , which would then be sorted based on the 
# first letter of the last name
def sort_names(names):
    return sorted(names, key = lambda name : name.split()[-1])
names = ["John Smith", "Kevin Ahn"]
print(sort_names(names)) # ['Kevin Ahn', 'John Smith']

def unique_cities(cities):
    return len(set(cities))
city_set = {"Atlanta", "Cumming", "Suwanee", "Atlanta"}
print(unique_cities(city_set))
