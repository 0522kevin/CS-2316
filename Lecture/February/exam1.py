# Exam 1 Topic List

# enumerate() 
temp = ["a", "b", "c", "d", "e"]
for i in enumerate(temp):
    print(i) # (0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')
print()

# .join()
print("-".join(temp)) # a-b-c-d-e
print("-".join(["a"])) # a
print()

# String formatting with f-strings
temp = "Kevin Ahn"
print(f"My name is {temp}") # My name is Kevin Ahn
print()

# List comprehension
temp = ["a", "b", "c", "d", "e"]
print([char for char in temp if char.isalpha()]) # ['a', 'b', 'c', 'd', 'e']
print()

# List comprehension with nested for loop
temp = [enumerate(temp)]
print([i for t in temp for i, char in t]) # [0, 1, 2, 3, 4]
print()

# Dictionay comprehension
temp = ["a", "b", "c", "d", "e"]
temp2 = [1, 2, 3, 4, 5]
print({i: char for i, char in zip(temp2, temp)}) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print()

# Sets
temp = {1, 2, 3, 4, 1}
print(temp) # {1, 2, 3, 4}
print()

# Lambda functions
temp = lambda a, b : a * b
print(temp(2, 2)) # 4
print()

# One-line conditionals
print(True if 1 < 2 else False) # True
print()

# Sorting using lambda functions
temp = ["George Washington", "John Adams", "Abe Lincoln"]
print(sorted(temp, key = lambda name : name.split()[-1])) # ['John Adams', 'Abe Lincoln', 'George Washington']
print()

# Modules vs. Scripts
if __name__ == "__main__":
    print("This is a script")
else:
    print("This is a module")
print()

# sys.argv
import sys
print(sys.argv[1:]) # ['1', '2', '3', '4', '5']
print()

# copy vs. deepcopy
import copy
temp = [[1, 2, 3], [0, 5, 6], [7, 8, 9]]
assign = temp
shallow = copy.copy(temp)
deep = copy.deepcopy(temp)
temp.append([10, 11, 12])
print(str(assign)) # [[1, 2, 3], [0, 5, 6], [7, 8, 9], [10, 11, 12]]
print()
print(str(shallow)) # [[1, 2, 3], [0, 5, 6], [7, 8, 9]]
print()
print(str(deep)) # [[1, 2, 3], [0, 5, 6], [7, 8, 9]]
print()

temp[1][0] = 4
print(str(assign)) # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print()
print(str(shallow)) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print()
print(str(deep)) # [[1, 2, 3], [0, 5, 6], [7, 8, 9]]

# OOP terminology

# Class inheritance
# super().__init__

# GUIs with PyQT5
