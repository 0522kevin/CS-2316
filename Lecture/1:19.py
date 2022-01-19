# 1/19

import math as m
print(m.sqrt(5))

# Print out the name of the script or module that currently running
print(__name__) # __main__ becuase it's running natively

def sort_by_last(names):
    return sorted(names, key  = lambda name : name.split()[-1])

def record_result(float1, float2):
    return "Record Brocken!" if float(float1) < float(float2) else "Record remains unchanged"

def count_unique(cities):
    return len(set(cities))

# ['John Adams', 'Abe Lincoln', 'George Washington']
print(sort_by_last(["George Washington", "John Adams", "Abe Lincoln"]))

# Record Brocken!
print(record_result(2.31, 2.32))

# 2
print(count_unique(["ATL","NYC","ATL"]))
