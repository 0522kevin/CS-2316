# 2/14

import csv

with open("countries.csv") as fin:
    reader = csv.reader(fin)
    data_list = list(reader)
print(data_list[0])

count = 0
for country in data_list:
    if "europe" in country[1].lower():
        count += 1
print(count)

average = 0
average_count = 0
for country in data_list:
    if "a" == country[0][0].lower():
        average_count += 1
        average += int(country[2])
average /= average_count
print(average)

with open("big_countries.csv", "w") as fout:
    writer = csv.writer(fout)
    writer.writerow(data_list[0])
    for country in data_list[1:]:
        if int(country[2]) >= 50000000:
            writer.writerow(country)

with open("country_basics.csv", "w") as fout:
    writer = csv.writer(fout)
    for country in data_list:
        writer.writerow([country[0], country[1], country[2], country[3], country[8]])
