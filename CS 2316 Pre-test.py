# Function called contains that takes a list of numbers and a query number
# Returns true if the list contains the query number, false otherwise
def contains(lists, query):
    if lists.count(query) > 0:
        return True
    else :
        return False    

# Function called num_evens that takes a list of numbers
# Returns the number of even numbers in the list
def num_evens(lists):
    temp_list = []
    for number in lists:
        if number % 2 == 0:
            temp_list.append(number)
    return temp_list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
query = 5

print(contains(numbers, query))
print()
print(num_evens(numbers))
print()

# Given a list[list[str]] of student grades where the first list is a header
# and subsequent lists have a name followed by grades
# Prints each student's name followed by their average score
# Prints the name of each graded item with the average score for that item

super_grades = [
    ['Thorny', '100', '90', '80'],
    ['Mac', '88', '99', '111'],
    ['Farva', '45', '56', '67'],
    ['Rabbit', '59', '61', '67'],
    ['Ursula', '73', '79', '83'],
    ['Foster', '89', '97', '101']
]

for super_grade in super_grades:
    average = int(super_grade[1]) + int(super_grade[2]) + int(super_grade[3])
    average = average / 3
    print(super_grade[0] + "'s average score is " + str(average))
print()

average = 0.0
for grade1 in super_grades:
    average = average + float(grade1[1])
average = average / len(super_grades)
print("Average score for Exam 1 is " + str(average))
print()

average = 0.0
for grade2 in super_grades:
    average = average + float(grade2[2])
average = average / len(super_grades)
print("Average score for Exam 2 is " + str(average))
print()

average = 0.0
for grade3 in super_grades:
    average = average + float(grade3[3])
average = average / len(super_grades)
print("Average score for Exam 3 is " + str(average))
