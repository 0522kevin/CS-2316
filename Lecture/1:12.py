# 1/12

# For loop
for letter in [1, 2, 3, 4]:
    print(letter)
print()

# Enumerate
# Returns (index, iteration at certain index)
pixar = "PIXAR"
for index, char in enumerate(pixar):
    print(char, index)
print()

nums = [3,2,3,7,9]
for i, n in enumerate(nums): 
    print(i + 2 * n) # 6 because i == 0 and n == 3
    break
print()

# Join
# Uses the string as a separator between the iterations
pixar = ["P", "I", "X", "A", "R"]
pixar_string = "hi".join(pixar)
print(pixar_string) # "PhiIhiXhiAhiR"
print()

letters = ["a","b","c"]
astr = letters[0].join(letters)
print(astr) # "aabac"
print()

# Returns a new string containing all the words
# from a list of words joined by hyphens
def get_string(words):
    return "-".join(words)
print(get_string(["Yellow", "Jacket", "Basketball"])) # "Yellow-Jacket-Basketball"
print()

# Tuple
# Uses ()
# Collection of variables that are unchangeable
# Support slicing
# count() and index()
data = ('George P. Burdell', 92, 'ISyE')
name, age, major = data # tuple unpacking

print(len(data)) # 3
print()
print(data.count(92)) # 1
print()
print(data.index(92)) # 1
print()

# Tuples can be multiplied
newdata = data * 3
print(newdata) # "('George P. Burdell', 92, 'ISyE', 'George P. Burdell', 92, 'ISyE', 'George P. Burdell', 92, 'ISyE')"
print()

# List
# Uses []
# append(), sort(), count(), index()
a_list = [False, 1, 2.0, 'three', ['four']]
a_list[0] = int(a_list[0]) # [0, 1, 2.0, 'three', ['four']]
print(a_list)
print()

# Sort() sorts the list without returning a new list
# Sorted() returns a new list
b_list = [5, 4, 0, 2, 3, 1]
b_list.sort() # [0, 1, 2, 3, 4, 5]
c_list = sorted(b_list, reverse = True) # [5, 4, 3, 2, 1, 0]
print(b_list)
print()
print(c_list)
print()

# Takes a list of sublists and returns the list with all the sublists sorted
def sort_sublists(lists):
    for list1 in lists:
        list1.sort()
list2 = [[1,2],[5,3],[6,2]]
sort_sublists(list2)
print(list2) # [[1,2], [3,5], [2,6]]
print()

# Dictionary
# Uses {key: value}
# When keys are duplicated, values are replaced
# keys(), values(), items()
num1 = [1, 2, 6, 2, 1, 8]
num2 = (4, 5, 1, 2, 3, 4)
d = {}
for position in range(len(num1)):
    d[num1[position]] = num2[position]
print(d) # {1: 4, 2: 2, 6: 1, 4: 3, 8: 4}
print()

# Because all the floats are less than 1, int(num) == 0
# Keys duplicate, so only the last num will be saved in the dictionary
d = {}
for num in [.5,.7,.9]:
    d[int(num)] = num
print(len(d)) # 1
print()

# Takes in a string and returns a dictionary mapping
# each letter in the string to the number of occurrences of that letter
def letter_counts(s):
    dict = {}
    for index, letter in enumerate(s):
        dict[letter] = letter.count(s)
    return dict
print(letter_counts("string")) # {'s': 0, 't': 0, 'r': 0, 'i': 0, 'n': 0, 'g': 0}
