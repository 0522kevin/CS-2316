# 2/25

import re

pattern = "he"
text = "The text might have multiple matches."
matches = re.finditer(pattern, text)
print(matches)
for match in matches:
    print('Found {}'.format(match))

phrase = "tttyttt"
print(re.findall("t*", phrase))

print(re.findall("[A-Z][a-z]+", "The big dog"))

print(re.findall("\w{4,}", "A huge rabbit"))

text = "I love CS2316."
pattern = r"[A-Z]"
replacement = "$"
newstring = re.sub(pattern, replacement, text)
print(newstring)

text = "Now is the time to go to cc.gatech.edu and use the apps find_gt or find_students to do the questions on pages 253."
print(re.findall(r"\w*_\w*", text))
print(re.findall(r"[A-Z]\w*", text))
print(re.findall(r"\w*\.\w*\.edu", text))

html_text = '<li>Coffee</li><li>Tea</li><br><br><br><img src="totoro.jpg" /img><li>Milk</li>'
print(re.findall(r"<li>(\w*)</li>", html_text))
print(re.findall(r"src=\"(\w*.jpg)", html_text))
