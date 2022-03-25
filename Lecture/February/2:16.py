# 2/16

import json

import json
astr = '{"cat":3,"dog":4}'
adict = json.loads(astr)
print(adict)

def get_keys(filename):
    try:
        return json.load(open(filename)).keys()
    except:
        return None
print(get_keys("book.json"))
