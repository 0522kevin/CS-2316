# 2/28

import re
text = "{START} Mary {END} had a {START} little lamb {END}"

# find the groupings in the string that start with {START} and end with {END}

pattern = "{START}.*?{END}"  # no question mark after the * so greedy

# greedy finds the longest match
# non-greedy (also called lazy) finds the shortest match

match = re.search(pattern,text)
print("None" if match == None else match.group())

text = "My cat’s favorite toy is a mouse with a 9 volt battery."
print(re.findall(r"(.)[a9]",text)) # [c, f,  ,  ,  b]
print(re.findall(r"v[a-z]+?",text)) # [vo, vo]
print(re.findall(r"v[a-z]+",text)) # [vorite, volt]

text = "Dr. Ángel Cabrera's phone number is 222-12-1234 and his address is 123 Tenth Street"
print(re.findall(r"\w{4,}", text))
print(re.findall(r"\d{3}-\d{2}-(\d{4})", text))
print(re.search(r"\d", text).start())
