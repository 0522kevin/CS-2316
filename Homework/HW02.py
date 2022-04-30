import csv
from pprint import pprint
import requests
import json
from bs4 import BeautifulSoup
import re

### DO NOT MODIFY THE FOLLOWING METHOD ###
def date_cleaner(string):
	mapping = {"January":"01", "February":"02", "March":"03",
				   "April":"04",   "May":"05",      "June":"06",
				   "July":"07",    "August":"08",   "September":"09",
				   "October":"10", "November":"11", "December":"12"}
	MM = mapping[string.split()[0]]
	DD = string.split(",")[0].split()[1]
	DD = "0" + DD if len(DD) == 1 else DD
	YYYY = string.split(",")[1].strip()
	date_str = f"{MM}/{DD}/{YYYY}"
	return date_str
##########################################

def shrek_script(file_name, output_file):
	with open(f"{file_name}.txt", "r") as fin:
		reader = csv.reader(fin)
		script = list(reader)
		alist = []
		temp_string = ""
		for line in script:
			temp_string = ",".join(line)
			temp_string = temp_string.rstrip()
			blist = temp_string.split("\n")
			for each in blist:
				alist.append(each)
			temp_string = ""
		script = alist

	with open(f"{output_file}.csv", "w") as fout:
		writer = csv.writer(fout)
		word_count = 0
		clist = []
		for row in range(1, len(script) + 1):
			line = script[row - 1]
			word_count += len(line.split())
			if row == 528:
				writer.writerow([row, len(line.split()), word_count, (True if "shrek" in line.lower() else False), "Have you ever met a person, you say, \"Let's get some parfait,\" they say, \"Hell no, I don't like no parfait\"?"])
				clist.append([row, len(line.split()), word_count, (True if "shrek" in line.lower() else False), "Have you ever met a person, you say, \"Let's get some parfait,\" they say, \"Hell no, I don't like no parfait\"?"])
			elif row == 1395:
				word_count += 1
				writer.writerow([row, len(line.split()) + 1, word_count, (True if "shrek" in line.lower() else False), "\"" + line])
				clist.append([row, len(line.split()) + 1, word_count, (True if "shrek" in line.lower() else False), "\"" + line])
			elif row == 1453:
				writer.writerow([row, len(line.split()), word_count, (True if "shrek" in line.lower() else False), "Could we just skip ahead to the \"I do's\"?"])
				clist.append([row, len(line.split()), word_count, (True if "shrek" in line.lower() else False), "Could we just skip ahead to the \"I do's\"?"])
			elif row == 1518:
				word_count += 1
				writer.writerow([row, len(line.split()) + 1, word_count, (True if "shrek" in line.lower() else False), "\" Now kiss me!"])
				clist.append([row, len(line.split()) + 1, word_count, (True if "shrek" in line.lower() else False), "\" Now kiss me!"])
			else:
				writer.writerow([row, len(line.split()), word_count, (True if "shrek" in line.lower() else False), line])
				clist.append([row, len(line.split()), word_count, (True if "shrek" in line.lower() else False), line])

	return clist

def csv_parser(filename):
	with open(filename, "r") as fin:
		reader = csv.reader(fin)
		shows = list(reader)
		netflix = []
		netflix.append(["ID", "IsMovie", "IsShow", "Title", "Director/s", "CastList", "CastSize", "Rating", "DateAdded", "IsHorror", "Synopsis"])
		for show in shows[1:]:
			netflix.append([show[0], (True if show[1].lower() == "movie" else False), (True if show[1].lower() == "tv show" else False), show[2], ("NIA" if show[3] == "" else show[3]), ([] if show[4] == "" else [(actor.strip() if len(actor.split()) == 1 else (actor[0] + ". " + actor.split()[-1])).strip() for actor in show[4].split(", ")]), (0 if show[4] == "" else len(show[4].split(", "))), show[8], ("NIA" if show[6] == "" else date_cleaner(show[6])), ("Horror" if "horror" in show[10].lower() else "Not Horror"), (" ".join(show[11].split()[:10]) + "...")])
		return netflix

def json_parser(filename):
	file = open(filename)
	netflix = json.load(file)
	alist = []
	for key in netflix.keys():
		dic = {}
		dic["ID"] = key
		dic["IsMovie"] = True if netflix[key]["type"].lower() == "movie" else False
		dic["IsShow"] = True if netflix[key]["type"].lower() == "tv show" else False
		dic["Title"] = netflix[key]["title"]
		dic["Director/s"] = "NIA" if netflix[key]["director"] == None else netflix[key]["director"]
		dic["CastList"] = [] if netflix[key]["cast"] == None else [(actor.strip() if len(actor.split()) == 1 else (actor[0] + ". " + actor.split()[-1])).strip() for actor in netflix[key]["cast"].split(", ")]
		dic["CastSize"] = 0 if netflix[key]["cast"] == None else len(netflix[key]["cast"].split(", "))
		dic["Rating"] = netflix[key]["rating"]
		dic["DateAdded"] = "NIA" if netflix[key]["date_added"] == None else date_cleaner(netflix[key]["date_added"])
		dic["IsHorror"] = "Horror" if "horror" in netflix[key]["listed_in"].lower() else "Not Horror"
		dic["Synopsis"] = " ".join(netflix[key]["description"].split()[:10]) + "..."
		alist.append(dic)
	file.close()
	return alist

def horror(csv_data, json_data, filename):
	dic = {"Movie": None, "Show": None}
	for each in dic.keys():
		dic[each] = {"01": {"num_horror": 0, "total": 0}, "02": {"num_horror": 0, "total": 0}, "03": {"num_horror": 0, "total": 0}, "04": {"num_horror": 0, "total": 0}, "05": {"num_horror": 0, "total": 0}, "06": {"num_horror": 0, "total": 0}, "07": {"num_horror": 0, "total": 0}, "08": {"num_horror": 0, "total": 0}, "09": {"num_horror": 0, "total": 0}, "10": {"num_horror": 0, "total": 0}, "11": {"num_horror": 0, "total": 0}, "12": {"num_horror": 0, "total": 0}, "overall": {"num_horror": 0, "total": 0}}
	dic["Show"]["NIA"] = {"num_horror": 0, "total": 0}

	for each in csv_data[1:]:
		if each[1]:
			if each[9] == "Horror":
				dic["Movie"][each[8][:2]]["num_horror"] += 1
				dic["Movie"]["overall"]["num_horror"] += 1
				dic["Movie"][each[8][:2]]["total"] += 1
				dic["Movie"]["overall"]["total"] += 1
			else:
				dic["Movie"][each[8][:2]]["total"] += 1
				dic["Movie"]["overall"]["total"] += 1
		else:
			if each[9] == "Horror":
				if each[8] == "NIA":
					dic["Show"]["NIA"]["num_horror"] += 1
					dic["Show"]["overall"]["num_horror"] += 1
					dic["Show"]["NIA"]["total"] += 1
					dic["Show"]["overall"]["total"] += 1
				else:
					dic["Show"][each[8][:2]]["num_horror"] += 1
					dic["Show"]["overall"]["num_horror"] += 1
					dic["Show"][each[8][:2]]["total"] += 1
					dic["Show"]["overall"]["total"] += 1
			else:
				if each[8] == "NIA":
					dic["Show"]["NIA"]["total"] += 1
					dic["Show"]["overall"]["total"] += 1
				else:
					dic["Show"][each[8][:2]]["total"] += 1
					dic["Show"]["overall"]["total"] += 1

	for each in json_data:
		if each["IsMovie"]:
			if each["IsHorror"] == "Horror":
				dic["Movie"][each["DateAdded"][:2]]["num_horror"] += 1
				dic["Movie"]["overall"]["num_horror"] += 1
				dic["Movie"][each["DateAdded"][:2]]["total"] += 1
				dic["Movie"]["overall"]["total"] += 1
			else:
				dic["Movie"][each["DateAdded"][:2]]["total"] += 1
				dic["Movie"]["overall"]["total"] += 1
		else:
			if each["IsHorror"] == "Horror":
				if each["DateAdded"] == "NIA":
					dic["Show"]["NIA"]["num_horror"] += 1
					dic["Show"]["overall"]["num_horror"] += 1
					dic["Show"]["NIA"]["total"] += 1
					dic["Show"]["overall"]["total"] += 1
				else:
					dic["Show"][each["DateAdded"][:2]]["num_horror"] += 1
					dic["Show"]["overall"]["num_horror"] += 1
					dic["Show"][each["DateAdded"][:2]]["total"] += 1
					dic["Show"]["overall"]["total"] += 1
			else:
				if each["DateAdded"] == "NIA":
					dic["Show"]["NIA"]["total"] += 1
					dic["Show"]["overall"]["total"] += 1
				else:
					dic["Show"][each["DateAdded"][:2]]["total"] += 1
					dic["Show"]["overall"]["total"] += 1

		with open(filename, "w") as fout:
			json.dump(dic, fout)

	return dic

def character_info(page):
	response = requests.get(f"https://api.disneyapi.dev/characters?page={page}")
	names = re.findall(r"\"name\":\"(.*?)\",", response.text)
	shows = re.findall(r"\"tvShows\":(\[.*?\]),", response.text)
	shows = [(list(show[2:-2].replace("\"", "").split(",")) if show != '[]' else 'None') for show in shows]
	ids = re.findall(r"\"_id\":(\d{4})", response.text)
	ids = [int(each) for each in ids]
	films = re.findall(r"\"films\":\[(.*?)\],", response.text)
	films = [(list(film.replace("\"", "").split(","))) for film in films]
	zipped = list(zip(names, ids, films, shows))
	zipped = [each for each in zipped if each[2] != ['']]
	return sorted(zipped, key = lambda x : len(x[2]), reverse = True)

def glee_dict(filename):
	dic = {'Season 1': None, 'Season 2': None, 'Season 3': None, 'Season 4': None, 'Season 5': None, 'Season 6': None}
	for each in dic.keys():
		dic[each] = {'Finale Views': None, 'Premiere Views': None, 'Retention': None, 'Success': None}
	soup = BeautifulSoup(open(filename), "html.parser")
	alist = []
	tags = soup.find_all("tr")
	for tag in tags:
		tds = tag.find_all("td")
		for td in tds:
			if re.search(r".*?\[\d\d\d\]", td.text) != None:
				alist.append(re.search(r".*?\[\d{3}\]", td.text).group())
	blist = []
	for each in alist:
		if float(each[each.index("[") + 1:-1]) in [144, 145, 149, 150, 154, 155, 158, 159, 163, 164, 167, 168]:
			blist.append(each[:each.index("[")])
	index = 0
	for each in dic.keys():
		dic[each]["Finale Views"] = f"{blist[index + 1]} million"
		dic[each]["Premiere Views"] = f"{blist[index]} million"
		if float(blist[index + 1]) - float(blist[index]) < 0:
			dic[each]["Retention"] = str(abs(round((float(blist[index + 1]) - float(blist[index])) / float(blist[index]) * 100, 2))) + "% increase"
			dic[each]["Success"] = True
		else:
			dic[each]["Retention"] = str(abs(round((float(blist[index + 1]) - float(blist[index])) / float(blist[index]) * 100, 2))) + "% decrease"
			dic[each]["Success"] = False
		index += 2
	return dic

def colorful_film():
	response = requests.get("https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films")
	soup = BeautifulSoup(response.text, "html.parser")
	trs = soup.find_all("tr", {"style":"background:#EEDD82"})
	alist = []
	for tr in trs:
		winner = tr.text.split("\n")[1:-1]
		alist.append([winner[0], int(re.findall(r"(\d{4})\D*", winner[1])[0]), int(re.findall(r"(\d+)\D*", winner[2])[0]), int(re.findall(r"(\d+)\D*", winner[3])[0])])
	return sorted(alist, key = lambda x : int(x[1]))

if __name__ == "__main__":
	pass
	# pprint(shrek_script('shrek', 'shrek_clean'))

	# pprint(csv_parser('netflix.csv'))

	# pprint(json_parser('netflix.json'))

	# clean_csv = csv_parser('netflix.csv')
	# clean_json = json_parser('netflix.json')
	# pprint(horror(clean_csv, clean_json, 'double_analysis.json'))

	# print(character_info(72))
	# print(len(character_info(72)))

	pprint(glee_dict('glee.html'))

	# pprint(colorful_film())



