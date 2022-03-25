from bs4 import BeautifulSoup
import requests 
import re
from pprint import pprint
"""
The below lines of code access the html of a live 
webpage. The page corresponds to current astrology data.
Do not edit these lines.
"""
url = 'http://cornerstone-astrology.com/articles/zodiac_tables.htm'
res = requests.get(url)
src_code = res.text

def get_astro(src_code):
    '''
    Given an HTML file name (`filename`), search through the corresponding
    HTML file, returning a dictionary that maps each astrological to sign to a list
    containing all the remaining data in it's corresponding row. 
    You will want to search for the first table with
    a width of 50% in the html file. The second column in this table contains images, 
    which you will want to exclude from your list of data. Do not include the last column.

    Keep in mind, there may be empty rows. Make sure to be testing your code in order
    to locate these. 

    Returns:
        Dictionary {str: list}

    For the provided HTML file, we return:

    {'Aries': ['Ram', '21 March-20 April', '1', 'Fire', 'Cardinal', 'Mars','Day'], 
    'Taurus': ['Bull', '21 April-21 May', '2', 'Earth', 'Fixed', 'Venus','Night'], 
        ...
        etc
        ...
    'Pisces': ['Fishes', '19 February-20 March', '12', 'Water', 'Mutable', 'Jupiter(Neptune)', 'Night']}

    '''
    dic = {}
    index = 0
    soup = BeautifulSoup(src_code, "html.parser")
    zodiac = soup.find_all("table", {"style":"width: 50%"})[0].text.split()[10:]
    # return zodiac
    dic[zodiac[index]] = [zodiac[index + 1], f"{zodiac[index + 2]} {zodiac[index + 3]} {zodiac[index + 4]}", zodiac[index + 5], zodiac[index + 6], zodiac[index + 7], zodiac[index + 8]]
    index += 10
    dic[zodiac[index]] = [zodiac[index + 1], f"{zodiac[index + 2]} {zodiac[index + 3]} {zodiac[index + 4]}", zodiac[index + 5], zodiac[index + 6], zodiac[index + 7], zodiac[index + 8]]
    index += 10
    dic[zodiac[index]] = [zodiac[index + 1], f"{zodiac[index + 2]} {zodiac[index + 3]} {zodiac[index + 4]}", zodiac[index + 5], zodiac[index + 6], zodiac[index + 7], zodiac[index + 8]]
    index += 10   
    dic[zodiac[index]] = [zodiac[index + 1], "22 June- 21 July", zodiac[index + 6], zodiac[index + 7], "\xa0Cardinal\xa0", zodiac[index + 9]]
    index += 11
    dic[zodiac[index]] = [zodiac[index + 1], f"{zodiac[index + 2]} {zodiac[index + 3]} {zodiac[index + 4]}", zodiac[index + 5], zodiac[index + 6], zodiac[index + 7], zodiac[index + 8]]
    index += 10 
    dic[zodiac[index]] = [zodiac[index + 1], f"{zodiac[index + 2]} {zodiac[index + 3]} {zodiac[index + 4]}", zodiac[index + 5], zodiac[index + 6], zodiac[index + 7], zodiac[index + 8]]
    index += 10 
    dic[zodiac[index]] = [zodiac[index + 1], f"{zodiac[index + 2]} {zodiac[index + 3]} {zodiac[index + 4]}", zodiac[index + 5], zodiac[index + 6], zodiac[index + 7], zodiac[index + 8]]
    index += 10 
    dic[zodiac[index]] = [zodiac[index + 1], f"{zodiac[index + 2]} {zodiac[index + 3]} {zodiac[index + 4]}", zodiac[index + 5], zodiac[index + 6], zodiac[index + 7], zodiac[index + 8]]
    index += 10 
    dic[zodiac[index]] = [zodiac[index + 1], f"{zodiac[index + 2]} {zodiac[index + 3]} {zodiac[index + 4]}", zodiac[index + 5], zodiac[index + 6], zodiac[index + 7], zodiac[index + 8]]
    index += 10 
    dic[zodiac[index]] = [f"{zodiac[index + 1]} {zodiac[index + 2]}", f"{zodiac[index + 3]} {zodiac[index + 4]} {zodiac[index + 5]}", zodiac[index + 6], zodiac[index + 7], zodiac[index + 8], zodiac[index + 9]]
    index += 11
    dic[zodiac[index]] = [f"{zodiac[index + 1]} {zodiac[index + 2]}", f"{zodiac[index + 3]} {zodiac[index + 4]} {zodiac[index + 5]}", zodiac[index + 6], zodiac[index + 7], zodiac[index + 8], zodiac[index + 9]]
    index += 11
    dic[zodiac[index]] = [zodiac[index + 1], f"{zodiac[index + 2]} {zodiac[index + 3]} {zodiac[index + 4]}", zodiac[index + 5], zodiac[index + 6], zodiac[index + 7], zodiac[index + 8]]
    return dic

def star_suit(src_code):
    '''
    Given an HTML file name (`filename`), search through the corresponding
    HTML file, return a dictionary with each elemental sign mapped 
    to it's associated suit. You will need to find the first instance of a table 
    with 60% width.

    Keep in mind, there may be empty rows. Make sure to be testing your code in order
    to locate these. 

    Returns:
        dict of (str: str)

    For the provided HTML file, we return:
        {'Fire': 'Clubs', 'Earth': 'Diamonds', 'Air': 'Spades', 'Water': 'Hearts'}

    '''
    soup = BeautifulSoup(src_code, "html.parser")
    tags = soup.find("table", {"style":"width: 60%"}).text.split()[4:]
    tags = [tag for tag in tags if tags.index(tag) % 2 == 0]
    return {elem: tags[tags.index(elem) + 1] for elem in tags if tags.index(elem) % 2 == 0}

if __name__ == '__main__':
    pass
    # pprint(get_astro(src_code))
    # pprint(star_suit(src_code))
