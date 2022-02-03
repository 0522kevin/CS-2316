# 1/21

import sys

# Exit the code immediately
# sys.exit() 

print(sys.argv) # Print out the arguments that were given when the file was run

for num in range(int(sys.argv[1])):
    print(num)

# List comprehension
# [expression for item in iterable if expression]
print([i * 2 for i in range(10) if i % 2 == 0]) # [0, 4, 8, 12, 16]
print([letter for letter in "jackets"]) # ['j', 'a', 'c', 'k', 'e', 't', 's']

old_list = [i * 2 for i in range(10) if i % 2 == 0] # [0, 4, 8, 12, 16]
new_list = [i for i in old_list if i % 3 == 0] # Included only if divisible by 3
print(new_list) # [0, 12]

# Use list comprehension
# A list of integers which specifies the length of each word in a sentence
# Exclude the word "the"
# Assune all words are lower case and no punctuation is present
sentence = "the best day of the week is friday"
print([len(i) for i in sentence.split() if i != "the"]) # [4, 3, 2, 4, 2, 6]

# Dictionary comprehension
print({ i : i ** 2 for i in range(5) }) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print({key : val for key, val in [(1,"a"), (2,"b"), (3,"c")]}) # {1: 'a', 2: 'b', 3: 'c'}

# Use dictionary comprehension
# A dictionary with the numbers from 1 to 5 as keys and strings of those numbers repeated as the values
print({i : str(i)*i for i in range(1, 6)}) # {1: '1', 2: '22', 3: '333', 4: '4444', 5: '55555'}

# A list comprehension that produces a list of the words in word_list that contain the same first and last letter
word_list = ["wow", "that", "is", "cool"]
print([s for s in word_list if s[0] == s[-1]])

# A list comprehension that produces a list of words where each word is a word from word_list with its first and last letters swapped
# Only works with list of strings that have more than one characters
print([s[-1] + s[1:-1] + s[0] for s in word_list])

# A dictionary comprehension to produce a dictionary that maps each of the letters in the word to its position in the word unless that letter is a vowel
word = "mcdaniel"
print({s : i for i, s in enumerate(word) if s != 'a' if s != 'e' if 'i' if 'o' if 'u'})

# Dictionary comprehension that produces a dictionary that maps each of the words to its indexed position in the phrase
phrase = "cs2316 is my favorite class"
print({s : i for i, s in enumerate(phrase.split())})
