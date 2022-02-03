# 1/19

import math as m
print(m.sqrt(5)) # 2.23606797749979

# Print out the name of the script or module that currently running
print(__name__) # __main__ becuase it's running natively

# Must contain one line of code only
# Returns a list sorted alphabetically by last name
def sort_by_last(names):
    return sorted(names, key  = lambda name : name.split()[-1])

# Must contain one line of code only
# Returns "Record Broken!" if the first parameter is less than the second parameter
# Returns "Record remains unchanged" otherwise
def record_result(float1, float2):
    return "Record Broken!" if float(float1) < float(float2) else "Record remains unchanged"

# Must contain one line of code only
# Returns a count of how many unique city names are included in a list of cities
def count_unique(cities):
    return len(set(cities))

print(sort_by_last(["George Washington", "John Adams", "Abe Lincoln"]))
# ['John Adams', 'Abe Lincoln', 'George Washington']

print(record_result(2.31, 2.32))
# Record Brocken!

print(count_unique(["ATL","NYC","ATL"]))
# 2
