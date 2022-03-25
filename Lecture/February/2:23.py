# 2/23

import re
pattern = "nn"
text = "Does the beginning of the text match?"
# match = re.match(pattern, text)
match = re.search(pattern, text)
print(match)  # a Match object or None
if match:
    s = match.start()
    e = match.end()
    print(match.group())

pattern = "3"
text = "Move the desks in rooms 123, 437, 329, 101, and 183."
substring_list = re.findall(pattern, text)
print(len(substring_list))
count = 0
for t in text:
    if t.lower() in "aeiou":
        count += 1
print(count)
count = 0
room = re.findall("\d\d\d", text)
print(len(room))
# for match in substring_list:
#     print(f'Found {match}')
