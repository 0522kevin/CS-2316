# 3/2

from pprint import pprint
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("lecture16.html"), "html.parser")
# print(soup)
tag_list = soup.find_all("li")
# print(tag_list)
for tag in tag_list:
    print(tag.text)

response = requests.get("https://scrapethissite.com/pages/simple/")
soup = BeautifulSoup(response.text, "html.parser") 
country_tags = soup.find_all("h3")
for tag in country_tags:
#     print(tag.text.strip())
    pass

dic = {}
tags = soup.find_all("div", {"class" : "col-md-4 country"})
for tag in tags: # within the div tag you already found
    country_tag = tag.find("h3")
    population_tag = tag.find("span", {"class":"country-population"})
    dic[country_tag.text.strip()] = population_tag.text.strip()
pprint(dic)
