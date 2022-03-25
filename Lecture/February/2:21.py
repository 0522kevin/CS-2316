# 2/21

import requests
response = requests.get("http://ghibliapi.herokuapp.com/films")
print(response)
print(response.text)

length = 0
for movie in response:
    length += 1
print(length)

for movie in response.json():
    if movie.get("title") == "Princess Mononoke":
        print(movie.get("release_date"))
    else:
        pass

new_response = sorted(response.json(), key = lambda x : int(x.get("running_time")))[0]
print(new_response.get("title"))
